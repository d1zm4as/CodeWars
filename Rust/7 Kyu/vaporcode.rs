fn vaporcode(s: &str) -> String {
    let mut copy =String::from("");
    for x in s.chars(){
       if x==' '{
            continue
            
       } else{    
            copy = copy.to_owned() + &String::from(x.to_ascii_uppercase());
            copy = copy.to_owned()+&String::from("  ");
        }
        
}
    copy.trim().to_string()
}








fn main(){
    let a = "eai";
    println!("{}",vaporcode(a));

}