fn solution(num: i32) -> i32 {
    let mut soma = 0;
    for x in 0..num{
        if x%3==0 || x%5==0{
            soma+=x
        }
    }
    soma
}