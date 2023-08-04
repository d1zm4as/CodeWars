fn camel_case(str: &str) -> String {
    if str == ""{
        return str.to_string()
    }
    let mut copy =String::from("");
    let b = str.trim().split(" ");
    for x in b{
        copy = copy.to_owned() + &(x[0..1]).to_uppercase();
        copy = copy.to_owned()+&(x[1..]);
    }
    copy.to_string()
}