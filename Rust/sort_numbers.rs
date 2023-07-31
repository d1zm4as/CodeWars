fn sort_numbers(arr: &Vec<i32>) -> Vec<i32> {
    let mut lista = vec![];
    for x in arr{
        lista.push(*x)
    }
    lista.sort();
    lista
    
}

// fn sort_numbers(arr: &Vec<i32>) -> Vec<i32> {
//     let mut answer = arr.clone();
//     answer.sort();
//     answer
// }