fn elevator_distance(floors: &[i16]) -> i16 {
    let mut ant = floors[0];
    let mut travel = 0;
    let mut index=  1;
    while index < floors.len(){
        travel += (ant-floors[index]).abs();
        ant = floors[index];
        index+=1;

    }
    travel
}




fn main(){
    // let a = [5,2,8];
    // let a = [7,1,7,1];
    let a = [3,3];

    // let a = [1,2,3];

    println!("{}",elevator_distance(&a))

}