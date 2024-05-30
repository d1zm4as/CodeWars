fn is_vowel(c: char) -> bool {
    match c {
        'a'  | 'e'  | 'i'  | 'o'  | 'u'  => true,
        _ => false,
    }
}



fn get_count(string: &str) -> usize {
    let mut cont: usize = 0;
    for x in string.chars(){
        if is_vowel(x){
            cont+=1;
        } 
    }
  // Do your magic here
  
  cont
}