int recherche(int t[100], int n, int x) {
  int a, b, m;
  int p;

  a = 0;
  b = n - 1;
  m = (a + b) / 2;

  while (a < b) {
    if (t[m] < x) {
      a = m + 1;
    }
    else {
      b = m;
    }

    m = (a + b) / 2;
  }

  if (t[a] == x) {
    p = a;
  }
  else {
    p = -1;
  }

  return p;
}