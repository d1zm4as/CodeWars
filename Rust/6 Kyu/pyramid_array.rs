
fn lol(n:usize) -> Vec<u32>{
    let mut lista = vec![];
    for x in 1..n+1{
        lista.push(1);
    }
    lista
    
}

fn pyramid(n: usize) -> Vec<Vec<u32>> {
    if n==0{
        return vec![] as Vec<Vec<u32>>;
    }
    let mut lista:Vec<Vec<u32>> = vec![];
    
    for x in 1 ..n+1{
        lista.push(lol(x));
    }
    lista
    
    
    
}