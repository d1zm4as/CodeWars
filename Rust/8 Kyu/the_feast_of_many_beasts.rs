

fn feast(beast: &str, dish: &str) -> bool {
    let beast_chars: Vec<char> = beast.chars().collect();
    let dish_chars: Vec<char> = dish.chars().collect();
    
    beast_chars.first() == dish_chars.first() && beast_chars.last() == dish_chars.last()
}