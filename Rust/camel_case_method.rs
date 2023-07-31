


fn main(){

    let a = "hello case";
    let mut copy =String::from("");
    let b = a.split(" ");
    for x in b{
        println!("{:?}",x);
        copy = copy.to_owned() + &(x[0..1]).to_uppercase();
        copy = copy.to_owned()+&(x[1..]);
    }

    println!("{:?}",copy);

}