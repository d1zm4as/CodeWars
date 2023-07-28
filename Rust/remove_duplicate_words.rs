// use std::collections::HashSet;
// fn remove_duplicate_words(s: &str) -> String {
//     format!("{}", s) // you code here
// }



fn main(){
        let a = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta";

        let mut copy = String::from("");


        for x in a.split(" "){
            if !copy.contains(x) {
                copy = copy.to_owned() + &String::from(x);
                copy = copy.to_owned() + &String::from(" ");
                
            }
    
        }
            
        
        println!("{}",copy.trim());
    
}


// use itertools::Itertools;

// fn remove_duplicate_words(s: &str) -> String {
//     s.split_whitespace().unique().join(" ")
// }