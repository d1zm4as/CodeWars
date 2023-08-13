fn sum_cubes(n: u32) -> u32 {
    let mut cont = 0;
    let  mut total = 0;
    while cont <= n{
        let a = cont*cont*cont;
        total+=a;
        cont+=1;
    }
    total
}