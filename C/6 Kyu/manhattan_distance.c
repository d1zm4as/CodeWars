// a and b contain coordinate points
// both are guaranteed to be size 2

int manhattan_distance(int *a, int *b) {

    int soma  = abs(a[0]-b[0]) + abs(a[1]-b[1]);
    return soma;

}