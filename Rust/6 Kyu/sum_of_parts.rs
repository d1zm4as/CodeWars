fn parts_sums(ls: &[u64]) -> Vec<u64> {
    let mut soma:u64 = ls.iter().sum();
    let mut lista = vec![];
    let mut cont:u64 = 0;
    lista.push(soma);
    for x in ls.iter(){
        cont+=x;
        let a = soma-cont;
        lista.push(a);
    
    }
    lista
}
