fn closest_multiple_of_10(n: u32) -> u32 {
    let res = n%10;
    let diff = 10-res;
    if res>=5{
        n+diff
    } else{
        n-res
       
    }
}







