#include<stdio.h>

typedef struct {
  float values[100];
  int len;
} Liste;

int main() {
  Liste maListe;
  float val;
  int i;

  maListe.len = 0;
  printf("val : ");
  scanf("%f", &val);

  while(val > 0) {
    maListe.values[maListe.len] = val;
    maListe.len = maListe.len + 1;
    printf("val : ");
    scanf("%f", &val);
  }

  for (i = 0; i < maListe.len; i++) {
    printf("%f ", maListe.values[i]);
  }

  printf("\n");
  return 0;
}
