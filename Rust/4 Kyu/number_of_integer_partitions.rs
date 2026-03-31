fn partitions(n: u32) -> u32 {
    let n = n as usize;
    let mut dp = vec![0u64; n + 1];
    dp[0] = 1; // one way to partition 0 (empty partition)
    
    // For each possible value k that can appear in partitions
    for k in 1..=n {
        // Update all sums that can include k
        for i in k..=n {
            dp[i] += dp[i - k];
        }
    }
    
    dp[n] as u32
}
