use std::collections::HashMap;
fn to_leet_speak(s: &str) -> String {
    let mut copy =String::from("");
    let map = HashMap::from([
        ("A","@"),
        ("B","8"),
        ("C","("),
        ("D","D"),
        ("E","3"),
        ("F","F"),
        ("G","6"),
        ("H","#"),
        ("I","!"),
        ("J","J"),
        ("K","K"),
        ("L","1"),
        ("M","M"),
        ("N","N"),
        ("O","0"),
        ("P","P"),
        ("Q","Q"),
        ("R","R"),
        ("S","$"),
        ("T","7"),
        ("U","U"),
        ("V","V"),
        ("W","W"),
        ("X","X"),
        ("Y","Y"),
        ("Z","2"),
        
        
    ]);
    for x in s.chars(){
        // let c = map.get::<str>(&x.to_string()).unwrap();
        if x.is_alphabetic() && x.is_uppercase(){
            let c = map.get::<str>(&x.to_string()).unwrap();
            copy = copy.to_owned()+ &c;
        }else{
            copy = copy.to_owned()+&String::from(x);
        }
            
        }
        
        copy.to_string()
    }
    /*
    fn to_leet_speak(s: &str) -> String {
    s.chars().map(|x| match x {
      'A' => '@',
      'B' => '8',
      'C' => '(',
      'D' => 'D',
      'E' => '3',
      'F' => 'F',
      'G' => '6',
      'H' => '#',
      'I' => '!',
      'J' => 'J',
      'K' => 'K',
      'L' => '1',
      'M' => 'M',
      'N' => 'N',
      'O' => '0',
      'P' => 'P',
      'Q' => 'Q',
      'R' => 'R',
      'S' => '$',
      'T' => '7',
      'U' => 'U',
      'V' => 'V',
      'W' => 'W',
      'X' => 'X',
      'Y' => 'Y',
      'Z' => '2',
      ' ' => ' ',
      _ => x,
      }).collect::<String>()
}
    */


fn main(){
    let a  = "EAI";
    println!("{}",to_leet_speak(a));
}