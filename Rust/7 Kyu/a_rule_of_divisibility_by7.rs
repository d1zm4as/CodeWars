fn seven(n: i64) -> (i64, i32) {
    let mut steps = 0;
    let mut m = n;
    
    while m >= 100 {
        let x = m / 10;
        let y = m % 10;
        m = x - 2 * y;
        steps += 1;
    }
    
    (m, steps)
}