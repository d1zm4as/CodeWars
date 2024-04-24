typedef struct Pair_Of_Ages { double oldest, youngest; } ages;

ages get_ages(int sum, int diff) { 
    ages result = {-1.0, -1.0};
    if(0 <= diff && diff <= sum) {
        result.oldest   = (sum + diff) / 2.0;
        result.youngest = (sum - diff) / 2.0;
    }
    return result;
}