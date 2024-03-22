fn even_or_odd(number: i32) -> &'static str {
    if number % 2==0{
        return "Even";
    }
    "Odd"
}