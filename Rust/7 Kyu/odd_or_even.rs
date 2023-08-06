fn odd_or_even(numbers: Vec<i32>) -> String {
    let soma:&i32 = &numbers.iter().sum();
    if soma%2==0{
       return "even".to_string()
    }
        "odd".to_string()

}