fn alphanumeric(password: &str) -> bool {
    if password == ""{
       return false
    }// usar is_empity na proxima
    password.chars().all(|x| x.is_alphanumeric())
    
}