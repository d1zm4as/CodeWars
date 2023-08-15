pub fn is_prime(x: u32) -> bool {
    if x == 2 {return true};
    if x < 2 || x % 2 == 0 {return false};
    (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
}






fn minimum_number(xs: &[u32]) -> u32 {
    let mut soma:u32 = xs.iter().sum();
    let mut cont:u32 = 0;
    
    while !is_prime(soma){
        soma+=1;
        cont+=1;
    }
    cont
}