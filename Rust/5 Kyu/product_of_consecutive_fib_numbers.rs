fn product_fib(prod: u64) -> (u64, u64, bool) {
    let mut x:u64 = 0;
    let mut y:u64 = 1;
    let cond:bool;
    while prod> x*y{
        (x,y) = (y,y+x);
    }
    
    if prod == x*y{
        cond  = true;
    }else{
        cond  =false;
    }
    
    (x,y,cond)
}