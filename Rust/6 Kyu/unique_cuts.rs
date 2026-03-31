// Task

// The function is given a string with lower-case characters. Split the string into as many non-empty substrings as possible, such that each character appears in only one substring. Return the list of lengths of the resulting substrings.
// Examples

// "abbccc" ➞ [1, 2, 3]
// # "a", "bb", "ccc"

// "abbacdceef" ➞ [4, 3, 2, 1]
// # "abba", "cdc", "ee", "f"

// "abacded" ➞ [3, 1, 3]
// # "aba", "c", "ded"

// "abcdea" ➞ [6]
// # "abcdea" because first letter is equal to the last letter.
use std::collections::HashMap;
fn split_unique_substrings(s: &str) -> Vec<usize> {
    let mut last_occurrence = HashMap::new();
    for (i, c) in s.chars().enumerate() {
        last_occurrence.insert(c, i);
    }

    let mut result = Vec::new();
    let mut start = 0;
    let mut end = 0;

    for (i, c) in s.chars().enumerate() {
        end = end.max(*last_occurrence.get(&c).unwrap());
        if i == end {
            result.push(end - start + 1);
            start = i + 1;
        }
    }

    result
}