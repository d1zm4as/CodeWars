pub fn is_prime(x: u64) -> bool {
    if x == 2 {return true};
    if x < 2 || x % 2 == 0 {return false};
    (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
}


fn gap(g: i32, m: u64, n: u64) -> Option<(u64, u64)> {
    let mut ant:u64 = 0;
    let g  = g as u64;
    let mut x:u64 = m;
    while x <= n{
        if is_prime(x){
            
            if x -ant==g as u64{
                
              return Some((ant,x));
            }
            ant = x;
        }
        x+=1;
    }
    None
}