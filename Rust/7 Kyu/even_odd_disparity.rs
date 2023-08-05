fn solve(v: &Vec<String>) -> i32 {
    let mut even = 0;
    let mut odd = 0;

    for i in v {
        match i.parse::<i32>() {
            Ok(x) => {
                if x % 2 == 0 {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
            Err(_) => continue,
        }
    }

    even - odd
}