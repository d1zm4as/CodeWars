fn positive_sum(slice: &[i32]) -> i32 {
    let tam  = slice.len();
    if tam==0{
        return 0;
    }
    let mut soma = 0;
    for x in slice{
        if x > &0{
            soma+=x
        }
    }
    soma
}