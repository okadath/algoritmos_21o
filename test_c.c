#include <stdio.h>

int array=0;
int recursion(int n, int k,int cadena,int stri) {
   // array=1;
   // return array;
//    if (k == 0 || k == n) {
//       return 1;
//    } else {
//       return recursion(n - 1, k) + recursion(n - 1, k - 1);
//    }
// def recursion(n,k,cadena,stri):
//    global array



   if (n<0){
      return 1;
   }
   if (k<0){
      return 1;
   }
   if (n==0) {//://#and k==0:
      if (stri==1){
         int asd=0;
      }
      else{
         if (cadena==0){
            k=0;
         }
         k=k-1;
      }
      if (k>=0){
         array=array+1;
      }
   }
   else{
      if (stri==1){
         cadena=1;
      }
      else{
         if (cadena==0){
            k=0;
         }
         cadena=0;
         k=k-1;
      }
      recursion(n-1,k,cadena,0);
      recursion(n-1,k,cadena,1);
   }
      // # else:





}

int main( ) {
   int n, k;
   scanf("%d%d", &n, &k);
   int aa=1;
   int bb=1;
   int c=0;
   int d=1;
   recursion(n-1,k,aa,c);
   recursion(n-1,k,bb,d);
   // printf("%d %d\n", formula(n, k), recursion(n, k));



   if (k==0 && n==0){
      printf("0");
   }
   else{

// recursion(int(n)-1,int(k),1,0)
// recursion(int(n)-1,int(k),1,1)
// # print(array)
      // printf("1");
printf("%d",array);
}
}
