use std::collections::HashMap;
fn encode(msg: String, k: i32) -> Vec<i32> 
{
    let map = HashMap::from([
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5),
    ('f', 6),
    ('g', 7),
    ('h', 8),
    ('i', 9),
    ('j', 10),
    ('k', 11),
    ('l', 12),
    ('m', 13),
    ('n', 14),
    ('o', 15),
    ('p', 16),
    ('q', 17),
    ('r', 18),
    ('s', 19),
    ('t', 20),
    ('u', 21),
    ('v', 22),
    ('w', 23),
    ('x', 24),
    ('y', 25),
    ('z', 26)
    ]);

    let chave = k.to_string();
    
    let mut soma:Vec<i32> = vec![];
    
    let mut cont = 0;

    for x in msg.chars(){

        let c = map.get(&x).unwrap();
        // let slice = &chave[cont as usize].parse::<u32>().unwrap();
        let slice = &chave[cont..cont+1].parse::<i32>().unwrap();

        soma.push(c+slice);
        cont +=1;
        if cont>=chave.len(){
            cont = 0;
        }

    }

    soma

}

fn main(){
let a = "scout";
println!("{:?}",encode(a.to_string(),1939));

}