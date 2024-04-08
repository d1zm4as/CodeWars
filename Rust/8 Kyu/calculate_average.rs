fn find_average(slice: &[f64]) -> f64 {
    let tam = slice.len() as f64;
    if tam ==0.0{
        return 0.0;
    }
    let mut soma:f64 = 0.0;
    for x in slice{
        soma+=x;
        
    }
    soma/tam
}