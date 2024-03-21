unsigned short sale_hotdogs(unsigned short n) {
    return n * (n < 5 ? 100 : n < 10 ? 95 : 90);
}
