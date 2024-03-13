
// def consecutive(arr):
//     return max(arr) - min(arr) + 1 - len(arr) if arr else 0
fn consecutive(xs: &[i16]) -> i16 {
    if xs.len()==0{
       0
   }else{
       let maior = xs.iter().max().unwrap();
       let menor=  xs.iter().min().unwrap();
       let r = maior - menor + 1 - xs.len() as i16;
       r
       
   }
}