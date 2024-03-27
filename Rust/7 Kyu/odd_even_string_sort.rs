fn sort_my_string(so: &str) -> String {
    let mut odd = String::new();
    let mut even = String::new();
    
    for (idx,x) in so.chars().enumerate(){
        if idx%2==0{
            even.push(x);
        }else{
            odd.push(x);
        }
    }
    
    format!("{} {}", even,odd)



}

