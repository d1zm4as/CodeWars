fn sum_pairs(ints: &[i8], s: i8) -> Option<(i8, i8)> {
    let mut copy = vec![];
    let mut cont:usize = 0;
    let tam = ints.len();
    while cont<tam{
        let atual:i8 = ints[cont];
        let  diff = s-atual;
        if copy.contains(&diff){
            return Some((diff,atual));
        }
        if !copy.contains(&atual){
            copy.push(atual);
        }
        cont+=1;
    }
    
    None
    
    
    }