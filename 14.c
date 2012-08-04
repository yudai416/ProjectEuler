#include <stdio.h>

// 途中でunsigned longの範囲を超える値が出る
unsigned long suretu(unsigned long n){
  if(n % 2 == 0)
    return n / 2;
  else
    return 3 * n + 1;
}

int count(int old_n){
  int count = 0;
  unsigned long n = (unsigned long)old_n;
  while(n > 1){
    n = suretu(n);
    count = count + 1;
    /*
    if(old_n == 626331)
      printf("%lu\n", n);
    */
  }
  /*
  if(old_n == 626331)
    printf("%d", count);
  if(n < 1)
    printf("%lu, %d\n", n, old_n);
  */
  return count;
}
  
int main(){
  int n, n_count, max_count = 0;
  for(n = 1; n < 1000000; n++){
    n_count = count(n);
    if(n_count > max_count){
      max_count = n_count;
      printf("n = %d, %d\n", n, max_count);
    }
  }
}
