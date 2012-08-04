#include <stdio.h>

int divisor(unsigned long num){
  int count = 0;
  long i, max = (long)(num / 2);

  for(i = 1; i <= max; i++){
    if(num % i == 0)
      count = count + 1;
  }
  return count + 1;
}

int main(){
  long i;
  unsigned long tri = 0;

  for(i = 1;;i++){
    tri = tri + i;
    //printf("%lu, %ld %d\n", tri, i, divisor(tri));
    if(divisor(tri) >= 501){
      printf("---------------------------------\n");
      printf("%lu, %ld %d\n", tri, i, divisor(tri));
      break;
    }
    if(i % 100 == 0)
      printf("%lu, %ld %d\n", tri, i, divisor(tri));
  }
}
