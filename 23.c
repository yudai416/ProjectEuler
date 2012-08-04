#include <stdio.h>
#include <stdlib.h>

int *make_sums_diviror(int size){
  int *sums = (int*)malloc(sizeof(int)*size);
  int i, n, sum;
  sums[0] = 0;
  
  for(n = 1; n < size; n++){
    sum = 0;
    for(i = 1; i < n/2+1; i++){
      if(n % i == 0)
	sum = sum + i;
    }
    sums[n] = sum;
  }
  return sums;
}

int match(int num, int *ab, int ab_size){
  int i, j;
  for(i = 0; i < ab_size; i++){
    for(j = i; j < ab_size; j++){
      if(num == (ab[i] + ab[j]))
	return 0;
    }
  }
  return num;
}

int main(){
  int i, ab_size, nab_sum, max = 28124;
  int *sums = make_sums_diviror(max);
  int *abundants = (int*)malloc(sizeof(int)*max);  
  nab_sum = 0;
  ab_size = 0;

  for(i = 1; i < max; i++){
    if(i < sums[i]){
      abundants[ab_size] = i;
      ab_size = ab_size + 1;
    }
    nab_sum = nab_sum + match(i, abundants, ab_size);
    //printf("%d, %d, %d\n", i, nab_sum, ab_size);
  }
  printf("%d\n", ab_size);
  printf("%d\n", nab_sum);

  free(sums);
  free(abundants);
}
