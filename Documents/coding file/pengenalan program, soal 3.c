#include <stdio.h>
int main ()
{

    float r,K;
    const float phi= 3.14;
    printf("masukkan jari-jari:  ");
    scanf("%f",&r);


    K=2*phi*r;
    printf("keliling lingkaran:  2*%.2f*%.2f= %.2f\n",r,phi,K);



    return 0;
}
