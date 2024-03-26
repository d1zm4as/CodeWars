fn remove_parentheses(s: &str) -> String {
    
    let mut copy =String::from("");
    
    let mut cont = 0;
    let b = s;
    for x in b.chars(){
        if x != '(' && cont ==0{
            copy = copy.to_owned()+ &String::from(x);
        }else if x == '('{
            cont+=1;
            
        }else if x==')'{
            cont-=1;
        }
    }
    copy
    
}