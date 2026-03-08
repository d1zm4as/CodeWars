
function sumArray(array) {
    if (!array || array.length < 3) {
        return 0;
    }
    return array.reduce((sum, val) => sum + val, 0);
}