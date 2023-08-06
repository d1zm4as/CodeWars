fn generate_pairs(m: i16, n: i16) -> Vec<(i16, i16)> {
    let mut lista = vec![];
    for i in m..n+1{
        for x in m..i+1{
            lista.push((x,i));
        }
    } 
    lista.sort();
    lista 
}
