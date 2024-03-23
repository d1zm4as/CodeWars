fn remove_exclamation_marks(input: &str) -> String {
    let mut copy = String::from("");
    
    for x in input.chars(){
        if x != '!'{
            copy  = copy.to_owned() + &String::from(x);
        }  
        
    }
        
    copy    
}