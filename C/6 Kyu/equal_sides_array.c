int dunno(const int numbers[], int start, int finish){
  int soma = 0;
  while( start<finish){
    soma = soma+numbers[start];
    start++;
  }
  return soma;
}
int find_even_index(const int *numbers, int tam) {
  for(int i = 0;i<tam;i++){
    if (dunno(numbers,0,i) == dunno(numbers,i+1,tam)) {
      return i;
      
    }
  
  }
  return -1;
}