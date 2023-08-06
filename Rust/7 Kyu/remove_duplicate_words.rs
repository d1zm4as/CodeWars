fn remove_duplicate_words(s: &str) -> String {
    let mut copy = String::from("");


        for x in s.split(" "){
            if !copy.contains(x) {
                copy = copy.to_owned() + &String::from(x);
                copy = copy.to_owned() + &String::from(" ");
                
            }
    
        }
            
        
        copy.trim().to_string()
            
        }