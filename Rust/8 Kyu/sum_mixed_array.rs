use either::Either;

fn sum_mix(arr: &[Either<i32, String>]) -> i32 {
    let mut result = 0;
    for element in arr {
        match element {
            Either::Left(x) => result += x,
            Either::Right(x) => result += x.parse::<i32>().unwrap(),
        }
    }
    result
    
    // como a função está usando either é necessário usar match pra ver[
    // as possibilidades