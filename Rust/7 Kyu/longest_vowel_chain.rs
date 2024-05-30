fn is_vowel(c: char) -> bool {
    match c {
        'a'  | 'e'  | 'i'  | 'o'  | 'u'  => true,
        _ => false,
    }
}


fn longest_vowel_chain(s: &str) -> usize {
    let mut maior = 0;
    let mut cont = 0;
    for x in s.chars(){
        if is_vowel(x){
            cont+=1;
        } 
        else {
            if cont>maior{ 
                maior = cont;
            }
            cont = 0 ;
       
        }   
    }
    if cont>maior{ 
        maior = cont;
    }

    maior
}



fn main(){
    let a = "eai";
    println!("{}",is_vowel('e'));

    println!("{}",longest_vowel_chain(a));

}