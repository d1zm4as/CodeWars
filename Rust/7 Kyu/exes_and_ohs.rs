fn xo(string: &'static str) -> bool {
    let copy = string.to_lowercase();
    let mut contx=  0;
    let mut conto= 0;
    for x in copy.chars(){
        if x=='o'{
            contx+=1;
        }else if x== 'x'{
            conto+=1;
        }else{
            continue
        }
        
    }
    contx==conto
    
}