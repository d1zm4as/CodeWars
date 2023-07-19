fn number(bus:&[(i32,i32)]) -> i32 {
    let mut soma = 0;
    let mut diff = 0;
    for x in bus{
       
        soma+=x.0;
        diff+=x.1;
        
    }
    soma-diff
    
}