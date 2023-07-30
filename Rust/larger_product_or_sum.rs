// fn sum_or_product(list: &[i64], n: usize) -> String {
//     todo!();
// }



fn main(){
    // soma dos 3 maiores
    //produto dos 3 menores
    let mut lista  = [10, 41, 8, 16, 20, 36, 9, 13, 20];
    lista.sort();
    let tam = (lista.len() as i32 -3) as usize;
    let prod:&i32 = &lista[0..3].iter().product();
    let soma:&i32 = &lista[tam..].iter().sum();


    println!("{:?}",prod);
    println!("{:?}",soma);
    println!("{:?}",lista);

}