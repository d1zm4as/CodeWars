fn solve(a: &str, b: &str) -> String {
    let mut copy = String::from("");


    for x in a.chars(){
        if !b.contains(x) {
            copy = copy.to_owned() + &String::from(x);
            
        }

    }
    for x in b.chars(){
        if !a.contains(x) {
            copy = copy.to_owned() + &String::from(x);
            
        }

    }
    copy
}

// fn solve(a: &str, b: &str) -> String {
//     [
//         a.chars().filter(|c| !b.contains(*c)).collect::<String>(),
//         b.chars().filter(|c| !a.contains(*c)).collect::<String>(),
//     ].concat()
// }