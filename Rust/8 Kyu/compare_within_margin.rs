fn close_compare(a: f64, b: f64, margin: f64) -> i8 {
    
    
    let diff = (a-b).abs();
    if diff<=margin{
       return 0;
    }else if a>b{
        return 1;
    }   else{
        return -1;
    }
    
    
} 
