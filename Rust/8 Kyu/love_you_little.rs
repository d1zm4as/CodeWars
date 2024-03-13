fn how_much_i_love_you(nb_petals: u16) -> &'static str {
    let a = nb_petals%6;
    
    match a {
        1=> return "I love you",
        2=> return "a little",
        3=> return "a lot",
        4=> return "passionately",
        5=> return "madly",
        _=> return "not at all"
        
        
    }
    
    
    
    
    
    
    
}
