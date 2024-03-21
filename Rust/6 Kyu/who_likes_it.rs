fn likes(names: &[&str]) -> String {
    let tam = names.len();
//     let _diff = tam-2;
    
    if tam ==0{
        
        return "no one likes this".to_string();
    }
    if tam ==1{
        return format!("{} likes this", names[0]);
    }
    if tam==2{
        return format!("{} and {} like this", names[0],names[1]);
        
    }
    if tam==3{
        return format!("{}, {} and {} like this", names[0],names[1],names[2]);
        
    }
    
    return format!("{}, {} and {} others like this", names[0],names[1],tam-2);
        