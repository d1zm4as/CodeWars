

int max(a,b){
  if( a>=b){
    return a;
  }else{
    return b;
  }
}


int maxSequence(const int* array, size_t n) {
  
    size_t i;
    
    int soma = 0;
    
    int maior = 0;
  
    for(i = 0; i<n;i++){
      
      soma = max(array[i],soma+array[i]);
      maior = max(maior,soma);
      
      
    }

  
  return maior;
}