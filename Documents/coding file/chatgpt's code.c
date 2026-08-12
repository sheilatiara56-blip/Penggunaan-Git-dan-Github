#include <stdio.h>

typedef struct {
    char nama[30];
    int umur;
    float ipk;
} Mahasiswa;

int main() {
    Mahasiswa m1 = {"Sheii", 19, 3.8};

    printf("Nama: %s\n", m1.nama);
    printf("Umur: %d\n", m1.umur);
    printf("IPK : %.2f\n", m1.ipk);

    return 0;
}
