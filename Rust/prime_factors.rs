mod is_prime;
use is_prime::is_prime;
// fn is_prime(x: i64) -> bool {
//     if x == 2 {return true};
//     if x < 2 || x % 2 == 0 {return false};
//     (3..).step_by(2).take_while(|i| i*i <= x).all(|i| x % i != 0)
// }

fn main(){

    let mut a = 44;
    let mut lista = vec![];
    let mut cont = 0;
    
    let mut primes = vec![2];
    for x in 3..a{
        if is_prime(x){

            primes.push(x);
        }
    }
    println!("{:?}",primes);

    while a>1{
        let mut atual = primes[cont];
        if a%atual==0{
            println!("{}",a);
            a /=atual;
            lista.push(atual);
        }else{
            cont+=1;
        }

    }

    println!("{:?}",lista);
    






}