fn is_prime(x: i64) -> bool {
    if x == 2 {return true};
    if x < 2 || x % 2 == 0 {return false};
    (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
}

fn next_prime(n: u64) -> u64 {
    let mut a = n+1;
    while !is_prime(a as i64){
        a+=1;
    }
    a
}