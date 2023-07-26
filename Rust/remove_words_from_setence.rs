fn count(s:&str)->u32{
    let mut cont = 0;
    for x in s.chars(){
        if x=='!'{
            cont+=1
        }
    
    }
    cont
}


fn remove(s: &str) -> String {
    let sep = s.split(" ");
    let mut copy =String::from("");
    for x in sep{
        if count(x)==1{
            continue
        
        }else{
            copy = copy.to_owned() + &String::from(x);
            copy = copy.to_owned()+&String::from(" ");
        }
}
    copy.trim().to_string()
}

fn main(){

    let a = "eai xuxu!";
    println!("{}",remove(a));

}