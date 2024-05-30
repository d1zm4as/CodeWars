fn is_vowel(c: char) -> bool {
    match c {
        'a' | 'A' | 'e' | 'E' | 'i' | 'I' | 'o' | 'O' | 'u' | 'U' => true,
        _ => false,
    }
}


fn disemvowel(s: &str) -> String {
    let mut copy = String::from("");
    for x in s.chars(){
        if !is_vowel(x){
            copy+=&x.to_string();
        }
    
    }
    copy
}