double find_average(const double array[/* length */], unsigned length)
{
    if(!length){
      return 0;
    }
    double total = 0.0;
	  for(int i = 0; i< length; i++){
      total+=array[i];
    }
  return total/length;
}