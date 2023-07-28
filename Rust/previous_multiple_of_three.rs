fn prev_mult_of_three(n: i32) -> i32 {
    let mut res = n;
    while res>0{
        if res%3==0{
            return res
        }else{
            res = res/10;
        }
    }
    -1
}
