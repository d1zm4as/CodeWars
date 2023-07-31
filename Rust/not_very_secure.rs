fn alphanumeric(password: &str) -> bool {
    if password == ""{
       return false
    }
    password.chars().all(|x| x.is_alphanumeric())
    
}