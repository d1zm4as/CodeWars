fn find_deleted_number(list: &[u16], mixed_list: &[u16]) -> Option<u16> {
    let a:u16 = list.iter().sum();
    let b:u16 = mixed_list.iter().sum();
    let soma:u16 = a-b;
    if soma ==0{
        return  None;
    }
    Some(soma)

}