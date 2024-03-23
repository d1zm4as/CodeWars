fn fib(n:u32)->u32{
    let mut x:u32= 0;
    let mut y:u32= 1;
    let mut cont = 1;
    while  cont <= n{
        (x,y) = (y,x+y);
        cont+=1;
        
    }
    
    x
}