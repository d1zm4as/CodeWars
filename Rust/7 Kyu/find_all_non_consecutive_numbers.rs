fn all_non_consecutive(arr: &[i32]) -> Vec<(usize, i32)> {
    let mut lista = vec![];
    if arr.len()==0{
        return lista;
    }
    
    let mut atual = arr[0];
    
    let mut cont = 1;
    
    for  x in &arr[1..]{
        
        if x- atual != 1{
            
            lista.push((cont, *x ));
        }
        
        atual = *x;
        cont+=1;
    }
    
    
    lista
    
    }