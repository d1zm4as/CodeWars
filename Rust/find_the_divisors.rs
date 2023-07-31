fn is_prime(x: i64) -> bool {
    if x == 2 {return true};
    if x < 2 || x % 2 == 0 {return false};
    (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
}



fn divisors(integer: u32) -> Result<Vec<u32>, String> {
	let mut lista = vec![];
    let mut copy = integer.to_string();
    if is_prime(integer as i64){
        copy = copy.to_owned() + &String::from(" is prime");
        return Err(copy)
        //  	Err(format!("{} is prime", integer))

    }

    for x in 2..integer{
        if integer%x==0{
            lista.push(x)
        }
    }

    Ok(lista)
}