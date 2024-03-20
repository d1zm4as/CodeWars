use std::cmp;

fn max_sequence(seq: &[i32]) -> i32 {
    
    let tam = seq.len();
    
    let mut soma = 0;
    
    let mut maior = 0;
    
    for x in 0..tam{
        
        soma = cmp::max(seq[x] , soma+seq[x]);
        maior = cmp::max(maior , soma);
        
    }
    
    maior
    
}
