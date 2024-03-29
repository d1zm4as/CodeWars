pub fn is_prime(x: u64) -> bool {
    if x == 2 {return true};
    if x < 2 || x % 2 == 0 {return false};
    (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
}

fn solve(n: u64) -> u64 {
    if is_prime(n){
        return n;
    }
    let mut prox = n+1;
    
    let mut ant = n-1;
    
    loop{
        if is_prime(ant){
            return ant;
        }
        if is_prime(prox){
            return prox;
        }
        prox+=1;
        ant-=1;
        
    
    }
    