/// Just to make code nicer
type Number = i32;
type Numbers = Vec<Number>;

/// Sums the numbers that are the same and consecutive.
fn sum_consecutives(numbers: &Numbers) -> Numbers {
    let copia  =  numbers;
    let mut lista = vec![];
    let mut atual  = copia[0];
    let mut copy = atual;
    
    for x  in &copia[1..]{
        if *x == atual{
            
            copy+=atual;
            atual = *x;
        }else{
            lista.push(copy);
            copy = 0;
            atual = *x;
            copy = *x;
            
        }
    }
    lista.push(copy);
    lista