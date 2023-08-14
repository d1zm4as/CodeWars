fn zeros(n: u64) -> u64 {
    let mut cont:u64 = 0;
    let mut lol = n;
    
    while lol >= 5{
        
        lol = lol/5;
        cont += lol;
    }
 
    cont
}