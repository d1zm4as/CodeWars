use itertools::Itertools;
fn solve(vecs: &[Vec<i32>]) -> i32 {
    vecs.iter()
        .multi_cartesian_product() //returns an iterator of iterators where the
        //subiterators taken together contain all possible combinations of taking
        //one number from each inner vector in vecs.
        .map(|x| x.into_iter().product())
        .max()
        .expect("invalid argument vecs")
}