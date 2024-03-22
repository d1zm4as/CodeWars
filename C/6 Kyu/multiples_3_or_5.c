int solution(int number) {
    
    int i,soma;
  
    
    
    soma = 0;
    
    for(i =  0; i< number;i++){
      if (i % 3 == 0 || i % 5 == 0){
            soma+=i;
        }
      
    }
  return soma;
}