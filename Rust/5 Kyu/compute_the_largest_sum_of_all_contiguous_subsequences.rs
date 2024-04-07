use std::cmp;

fn largest_sum(seq: &[i32]) -> i32 {
    
    if seq.is_empty(){
        return 0;
    }
    
    let tam = seq.len();
    
    let mut soma = 0;
    
    let mut maior = 0;
    
    for x in 0..tam{
        
        soma = cmp::max(seq[x] , soma+seq[x]);
        maior = cmp::max(maior , soma);
        
    }
    
    maior
}