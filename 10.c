#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#define MAX1 4294967295
#define MAX 2147483647
#define N 2000000
//#define N 100

int *init_nums(){
  int i;
  int *nums = (int *)malloc(sizeof(int)*(N+1));
  for(i = 2; i < N+1; i++){
    nums[i-2] = i;
  }
  return nums;
}

void compute(){
  int i, j, num;
  long sum = 0;
  int *nums = init_nums();

  for(i = 0; i < N-1; i++){
    if(nums[i] != -1){
      num = nums[i];
      if(num > (MAX - sum)){
	printf("%ld,", sum);
	sum = 0;
      }
      sum = sum + num;
      for(j = i+num; j < N-1; j = j + num){
	nums[j] = -1;
      }
    }
  }
  printf("%ld\n", sum);
}

int main(){
  compute();
}
