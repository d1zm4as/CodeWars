fn alternate<'a>(n: usize, first_value: &'a str, second_value: &'a str) -> Vec<&'a str> {
    let mut cont = n as i32;
    let mut lista = vec![];
    while cont>0{
        lista.push(first_value);
        cont-=1;
        if cont==0{
            break
        }
        lista.push(second_value);
        cont-=1;
    }
    
    lista
}
