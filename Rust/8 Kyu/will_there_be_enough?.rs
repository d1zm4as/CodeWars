fn enough(cap: i32, on: i32, wait: i32) -> i32 {
    let soma:i32 = wait +on;
    if soma>cap{
        soma-cap
    }else{
        0
    }
}