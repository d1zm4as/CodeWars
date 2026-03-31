fn well(x: &[&str]) -> &'static str {
    match x.into_iter().filter(|&&s| s == "good").count() {
        0 => "Fail!",
        1 | 2 => "Publish!",
        _ => "I smell a series!",
    }
}