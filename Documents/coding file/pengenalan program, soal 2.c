#include <stdio.h>

int main() {
    int airMendidih = 1
    int miMatang = 1
    int miMerata = 1

    printf("siapkan mi, air, panci, sendok, arpu, kompor, mangkok, bumbu\n");
    printf("masukkan air ke dalam panci\n");
    printf("nyalakan kompor\n");
    printf("rebus air..\n");

    if (airMendidih == 1){
        printf("ar sudah mendidih, masukkan mi ke dalam panci\n");
    } else {
        printf("air belum mendidih, tunggu dulu\n");
    }

    printf("aduk mi \n");

    if (miMatang == 1) {
        printf("mi sudah matang, tiriskan dan letakkan ke mangkok\n");
    } else {
        printf("mi belum matang tunggu sebentar lagi....\n");
    }

    printf("masukkan bunbu ke dalam mangkok\n");
    printf("aduk mi dengan bumbu\n");

    if (miMerata == 1){
        printf("mi siap disajikan\n");
    } else {
        printf("bumbu belum merata , aduk lagi...\n");
    }

    return 0;
}


