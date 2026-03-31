use std::collections::HashMap;

pub fn dont_give_me_five(start: i64, end: i64) -> usize {
    // Count valid numbers in the range [start, end]
    let mut count = 0;
    
    // Handle negative range [start, -1] or [start, end] where end < 0
    if start < 0 {
        let neg_end = if end < 0 { end } else { -1 };
        // Count numbers from start to neg_end (both negative)
        // These correspond to [-end, -start] when we flip their absolute values
        count += count_positive_range(-neg_end, -start);
    }
    
    // Handle positive range [0, end] or [start, end] where start >= 0
    if end >= 0 {
        let pos_start = if start >= 0 { start } else { 0 };
        count += count_positive_range(pos_start, end);
    }
    
    count as usize
}

fn count_positive_range(start: i64, end: i64) -> i64 {
    count_up_to(end) - count_up_to(start - 1)
}

fn count_up_to(n: i64) -> i64 {
    if n < 0 {
        return 0;
    }
    if n == 0 {
        return 1; // Just 0
    }
    
    let s = n.to_string();
    let digits: Vec<u32> = s.chars().map(|c| c.to_digit(10).unwrap()).collect();
    let mut memo = HashMap::new();
    
    fn dfs(
        pos: usize,
        tight: bool,
        digits: &[u32],
        memo: &mut HashMap<(usize, bool), i64>,
    ) -> i64 {
        if pos == digits.len() {
            return 1; // Successfully formed a valid number
        }
        
        if let Some(&res) = memo.get(&(pos, tight)) {
            return res;
        }
        
        let limit = if tight { digits[pos] } else { 9 };
        let mut res = 0;
        
        for d in 0..=limit {
            if d == 5 {
                continue; // Skip the digit 5
            }
            let new_tight = tight && (d == limit);
            res += dfs(pos + 1, new_tight, digits, memo);
        }
        
        memo.insert((pos, tight), res);
        res
    }
    
    dfs(0, true, &digits, &mut memo)
}
