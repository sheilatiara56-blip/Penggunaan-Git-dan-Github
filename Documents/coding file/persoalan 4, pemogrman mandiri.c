#include <stdio.h>
int main (){

int a,b,hasil;
printf("masukkan bilangan ganjil pertama:  ");
scanf ("%d",&a);
printf("masukkan bilangan ganjil kedua:  ");
scanf("%d",&b);
hasil=a-b;

    if (a % 2 != 0 && b % 2 != 0) {
printf("hasil : %d-%d= %d\n",a,b,hasil);

         } else {
          printf("hasil error,salah satu atau keduanya bukan bilangan ganjil");}

return 0;}
