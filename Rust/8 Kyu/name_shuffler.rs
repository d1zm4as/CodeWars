use itertools::Itertools;

fn name_shuffler(s: &str) -> String {
    s.split_whitespace().rev().join(" ")
}