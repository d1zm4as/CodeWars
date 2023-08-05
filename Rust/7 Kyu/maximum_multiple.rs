fn max_multiple(divisor: u32, bound: u32) -> u32 {
    let mut maior = 0;
    
    for x in divisor..bound+1{
        if x%divisor==0 && x!=0{
            if x>maior{
                maior = x;
            }
        }
    
    }
    maior
}