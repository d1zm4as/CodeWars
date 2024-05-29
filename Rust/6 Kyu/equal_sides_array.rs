fn find_even_index(arr: &[i32]) -> Option<usize> {
    let tam  = arr.len();
//     let menor=  xs.iter().min().unwrap();
    for x in 0..tam{
        
        if &arr[0..x].iter().sum::<i32>() == &arr[x+1..tam].iter().sum::<i32>() {
            return Some(x);
        }
    }
        None
}
