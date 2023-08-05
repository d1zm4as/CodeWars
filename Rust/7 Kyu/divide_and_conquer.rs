use either::Either;

fn div_con(arr: &[Either<i32, String>]) -> i32 {
    let mut somaInt:i32 = 0;
    let mut somaStr:i32 = 0;
    for x in arr{
        match x{
            Either::Left(x)=> somaInt+=x,
            Either::Right(x)=> somaStr+=x.parse::<i32>().unwrap(),
            
        }
    }
    somaInt - somaStr
}
