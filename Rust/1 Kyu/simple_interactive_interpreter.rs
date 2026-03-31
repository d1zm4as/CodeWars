use std::collections::HashMap;

#[derive(Debug, Clone)]
enum Expr {
    Number(f32),
    Identifier(String),
    BinOp {
        op: char,
        left: Box<Expr>,
        right: Box<Expr>,
    },
    Assignment {
        name: String,
        value: Box<Expr>,
    },
    FunctionCall {
        name: String,
        args: Vec<Expr>,
    },
}

struct Interpreter {
    variables: HashMap<String, f32>,
    functions: HashMap<String, (Vec<String>, Expr)>,
}

impl Interpreter {
    fn new() -> Interpreter {
        Interpreter {
            variables: HashMap::new(),
            functions: HashMap::new(),
        }
    }

    fn input(&mut self, input: &str) -> Result<Option<f32>, String> {
        let trimmed = input.trim();
        if trimmed.is_empty() {
            return Ok(None);
        }

        let tokens = tokenize(trimmed)?;
        if tokens.is_empty() {
            return Ok(None);
        }

        // Check if it's a function declaration
        if tokens[0] == "fn" {
            let (func_def, pos) = parse_function(&tokens, 0)?;
            if pos != tokens.len() {
                return Err("ERROR: Unexpected tokens after function definition.".to_string());
            }
            self.apply_function_def(func_def)?;
            Ok(None)
        } else {
            let (expr, pos) = parse_expression(&tokens, 0)?;
            if pos != tokens.len() {
                return Err("ERROR: Unexpected tokens after expression.".to_string());
            }
            let result = self.eval_expr_mut(&expr, &HashMap::new())?;
            Ok(Some(result))
        }
    }

    fn apply_function_def(&mut self, (name, params, body): (String, Vec<String>, Expr)) -> Result<(), String> {
        // Check for name conflicts with variables
        if self.variables.contains_key(&name) {
            return Err(format!("ERROR: Function name '{}' conflicts with existing variable.", name));
        }
        self.functions.insert(name, (params, body));
        Ok(())
    }

    fn eval_expr_mut(&mut self, expr: &Expr, local_vars: &HashMap<String, f32>) -> Result<f32, String> {
        match expr {
            Expr::Number(n) => Ok(*n),
            Expr::Identifier(name) => {
                if let Some(val) = local_vars.get(name) {
                    Ok(*val)
                } else if let Some((params, body)) = self.functions.get(name).cloned() {
                    // Call zero-argument function
                    if !params.is_empty() {
                        return Err(format!("ERROR: Function '{}' expects {} arguments, got 0", name, params.len()));
                    }
                    self.eval_expr_mut(&body, local_vars)
                } else if let Some(val) = self.variables.get(name) {
                    Ok(*val)
                } else {
                    Err(format!("ERROR: Invalid identifier. No variable with name '{}' was found.", name))
                }
            }
            Expr::BinOp { op, left, right } => {
                let left_val = self.eval_expr_mut(left, local_vars)?;
                let right_val = self.eval_expr_mut(right, local_vars)?;
                match op {
                    '+' => Ok(left_val + right_val),
                    '-' => Ok(left_val - right_val),
                    '*' => Ok(left_val * right_val),
                    '/' => Ok(left_val / right_val),
                    '%' => Ok(left_val % right_val),
                    _ => Err(format!("Unknown operator: {}", op)),
                }
            }
            Expr::Assignment { name, value } => {
                if local_vars.contains_key(name) {
                    return Err(format!("ERROR: Cannot assign to parameter '{}'", name));
                }
                if self.functions.contains_key(name) {
                    return Err(format!("ERROR: Cannot assign to function '{}'", name));
                }
                let val = self.eval_expr_mut(value, local_vars)?;
                self.variables.insert(name.clone(), val);
                Ok(val)
            }
            Expr::FunctionCall { name, args } => {
                if let Some((params, body)) = self.functions.get(name).cloned() {
                    if args.len() != params.len() {
                        return Err(format!("ERROR: Function '{}' expects {} arguments, got {}", 
                            name, params.len(), args.len()));
                    }
                    let mut local = local_vars.clone();
                    for (param, arg) in params.iter().zip(args.iter()) {
                        let val = self.eval_expr_mut(arg, local_vars)?;
                        local.insert(param.clone(), val);
                    }
                    self.eval_expr_mut(&body, &local)
                } else {
                    Err(format!("ERROR: Unknown function '{}'", name))
                }
            }
        }
    }
}

fn tokenize(input: &str) -> Result<Vec<String>, String> {
    let mut tokens = Vec::new();
    let mut current = String::new();
    let mut chars = input.chars().peekable();

    while let Some(&ch) = chars.peek() {
        if ch.is_whitespace() {
            if !current.is_empty() {
                tokens.push(current);
                current = String::new();
            }
            chars.next();
        } else if "()=+*/%".contains(ch) {
            if !current.is_empty() {
                tokens.push(current);
                current = String::new();
            }
            if ch == '=' && chars.clone().nth(1) == Some('>') {
                chars.next();
                chars.next();
                tokens.push("=>".to_string());
            } else {
                tokens.push(ch.to_string());
                chars.next();
            }
        } else if ch == '-' {
            if !current.is_empty() {
                tokens.push(current);
                current = String::new();
            }
            
            // Check if this is a unary minus (negative number) or binary minus (subtraction)
            // Binary minus: after a number, identifier, or closing paren
            // Unary minus: after operators, opening paren, or at start
            let is_unary = tokens.is_empty() || 
                matches!(tokens.last().map(|s| s.as_str()), Some("(" | "=>" | "=" | "+" | "-" | "*" | "/" | "%"));
            
            chars.next();
            let next = chars.peek();
            
            if is_unary && next.map_or(false, |c| c.is_numeric() || *c == '.') {
                // It's a unary minus (negative number)
                current.push('-');
                while let Some(&c) = chars.peek() {
                    if c.is_numeric() || c == '.' {
                        current.push(c);
                        chars.next();
                    } else {
                        break;
                    }
                }
                tokens.push(current);
                current = String::new();
            } else {
                // It's a binary minus (subtraction operator)
                tokens.push("-".to_string());
            }
        } else if ch.is_numeric() || ch == '.' {
            current.push(ch);
            chars.next();
        } else if ch.is_alphabetic() || ch == '_' {
            current.push(ch);
            chars.next();
        } else {
            return Err(format!("ERROR: Invalid character: {}", ch));
        }
    }

    if !current.is_empty() {
        tokens.push(current);
    }

    Ok(tokens)
}

fn parse_function(tokens: &[String], mut pos: usize) -> Result<((String, Vec<String>, Expr), usize), String> {
    if pos >= tokens.len() || tokens[pos] != "fn" {
        return Err("Expected 'fn'".to_string());
    }
    pos += 1;

    if pos >= tokens.len() {
        return Err("Expected function name".to_string());
    }
    let name = tokens[pos].clone();
    pos += 1;

    let mut params = Vec::new();
    while pos < tokens.len() && tokens[pos] != "=>" {
        if is_identifier(&tokens[pos]) {
            let param = tokens[pos].clone();
            // Check for duplicate parameters
            if params.contains(&param) {
                return Err(format!("ERROR: Duplicate parameter '{}' in function definition.", param));
            }
            params.push(param);
            pos += 1;
        } else {
            return Err("Expected identifier in parameter list".to_string());
        }
    }

    if pos >= tokens.len() || tokens[pos] != "=>" {
        return Err("Expected '=>'".to_string());
    }
    pos += 1;

    if pos >= tokens.len() {
        return Err("Expected expression after '=>'".to_string());
    }

    let (body, pos) = parse_expression(tokens, pos)?;
    validate_function_body(&body, &params)?;

    Ok(((name, params, body), pos))
}

fn validate_function_body(expr: &Expr, params: &[String]) -> Result<(), String> {
    match expr {
        Expr::Number(_) => Ok(()),
        Expr::Identifier(name) => {
            if !params.contains(name) {
                Err(format!("ERROR: Invalid identifier '{}' in function body.", name))
            } else {
                Ok(())
            }
        }
        Expr::BinOp { left, right, .. } => {
            validate_function_body(left, params)?;
            validate_function_body(right, params)?;
            Ok(())
        }
        Expr::Assignment { name, value } => {
            // Assignment target must be a parameter
            if !params.contains(name) {
                return Err(format!("ERROR: Cannot assign to non-parameter '{}' in function body.", name));
            }
            // All identifiers in the value expression must be parameters
            validate_function_body(value, params)
        }
        Expr::FunctionCall { args, .. } => {
            for arg in args {
                validate_function_body(arg, params)?;
            }
            Ok(())
        }
    }
}

fn parse_expression(tokens: &[String], pos: usize) -> Result<(Expr, usize), String> {
    parse_assignment(tokens, pos)
}

fn parse_assignment(tokens: &[String], pos: usize) -> Result<(Expr, usize), String> {
    let (mut expr, mut pos) = parse_additive(tokens, pos)?;

    if pos < tokens.len() && tokens[pos] == "=" {
        if let Expr::Identifier(name) = expr {
            pos += 1;
            if pos >= tokens.len() {
                return Err("Expected expression after '='".to_string());
            }
            let (value, pos) = parse_assignment(tokens, pos)?; // Right associative
            expr = Expr::Assignment {
                name,
                value: Box::new(value),
            };
            Ok((expr, pos))
        } else {
            Err("ERROR: Invalid assignment target. Only identifiers can be assigned to.".to_string())
        }
    } else {
        Ok((expr, pos))
    }
}

fn parse_additive(tokens: &[String], pos: usize) -> Result<(Expr, usize), String> {
    let (mut expr, mut pos) = parse_multiplicative(tokens, pos)?;

    while pos < tokens.len() && (tokens[pos] == "+" || tokens[pos] == "-") {
        let op = tokens[pos].chars().next().unwrap();
        pos += 1;
        let (right, new_pos) = parse_multiplicative(tokens, pos)?;
        expr = Expr::BinOp {
            op,
            left: Box::new(expr),
            right: Box::new(right),
        };
        pos = new_pos;
    }

    Ok((expr, pos))
}

fn parse_multiplicative(tokens: &[String], pos: usize) -> Result<(Expr, usize), String> {
    let (mut expr, mut pos) = parse_function_call(tokens, pos)?;

    while pos < tokens.len() && (tokens[pos] == "*" || tokens[pos] == "/" || tokens[pos] == "%") {
        let op = tokens[pos].chars().next().unwrap();
        pos += 1;
        let (right, new_pos) = parse_function_call(tokens, pos)?;
        expr = Expr::BinOp {
            op,
            left: Box::new(expr),
            right: Box::new(right),
        };
        pos = new_pos;
    }

    Ok((expr, pos))
}

fn parse_function_call(tokens: &[String], pos: usize) -> Result<(Expr, usize), String> {
    let (expr, mut pos) = parse_factor(tokens, pos)?;

    // If expr is an identifier and next token could be an argument, parse as function call
    let expr = if let Expr::Identifier(name) = expr {
        let mut args = Vec::new();
        
        // Keep parsing arguments until we hit an operator or something that can't be an argument
        while pos < tokens.len() && could_be_argument(&tokens[pos]) {
            let (arg, new_pos) = parse_function_call(tokens, pos)?;
            args.push(arg.clone());
            pos = new_pos;
            
            // Check if next token could continue as an argument
            if pos >= tokens.len() || !could_be_argument(&tokens[pos]) {
                break;
            }
            
            // IMPORTANT: Only apply lookahead break for simple arguments (not function calls)
            // This allows "add echo 4 echo 3" to parse as add(echo(4), echo(3))
            // but "echo 4 echo 3" would parse as echo(4) leaving "echo 3" separate
            if !matches!(arg, Expr::FunctionCall { .. }) && 
               is_identifier(&tokens[pos]) && pos + 1 < tokens.len() && could_be_argument(&tokens[pos + 1]) {
                break;
            }
        }
        
        // If we found any arguments, create a function call, otherwise keep as identifier
        if !args.is_empty() {
            Expr::FunctionCall { name, args }
        } else {
            Expr::Identifier(name)
        }
    } else {
        expr
    };

    Ok((expr, pos))
}

fn could_be_argument(token: &str) -> bool {
    // Check if token is definitely an operator or keyword
    if matches!(token, "=" | "=>" | "+" | "*" | "/" | "%" | ")" | "fn") {
        return false;
    }
    // "-" by itself (length 1) is an operator, but negative numbers have length > 1
    if token == "-" {
        return false;
    }
    
    // Otherwise it could be an argument (identifier, number, or paren)
    token == "(" || 
    is_identifier(token) || 
    token.starts_with('-') ||  // negative number
    token.chars().next().map_or(false, |c| c.is_numeric())
}

fn parse_factor(tokens: &[String], pos: usize) -> Result<(Expr, usize), String> {
    if pos >= tokens.len() {
        return Err("ERROR: Unexpected end of input".to_string());
    }

    let token = &tokens[pos];

    if token == "(" {
        let (expr, pos) = parse_expression(tokens, pos + 1)?;
        if pos >= tokens.len() || tokens[pos] != ")" {
            return Err("ERROR: Expected ')'".to_string());
        }
        Ok((expr, pos + 1))
    } else if token == "." {
        return Err("ERROR: Unexpected '.'".to_string());
    } else if token.starts_with('-') || token.chars().next().map_or(false, |c| c.is_numeric()) {
        let num = token.parse::<f32>()
            .map_err(|_| "ERROR: Invalid number format".to_string())?;
        Ok((Expr::Number(num), pos + 1))
    } else if token.chars().next().map_or(false, |c| c.is_alphabetic() || c == '_') {
        let name = token.clone();
        Ok((Expr::Identifier(name), pos + 1))
    } else {
        Err(format!("ERROR: Unexpected token: {}", token))
    }
}

fn is_identifier(token: &str) -> bool {
    token.chars().next().map_or(false, |c| c.is_alphabetic() || c == '_')
}