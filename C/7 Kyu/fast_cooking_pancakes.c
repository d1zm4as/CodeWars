unsigned cook_pancakes(unsigned n, unsigned m) {

    int menor;
    
    if (n>=m){
      menor = m;
    }else{
      menor = n;
      
    }
  
    return (2*n-1)/menor +1;

}