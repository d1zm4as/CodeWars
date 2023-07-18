fn get_grade(s1: u16, s2: u16, s3: u16) -> char {
    let media:f64 = ((s1+s2+s3)/3).into();
    if media >=90.0{
        'A'
    }else if media>= 80.0 && media <90.0{
        'B'
    }else if media>= 70.0 && media <80.0{
        'C'
    }else if media>= 60.0 && media <70.0{
        'D'
    }else{
        'F'
    }
    
    
}