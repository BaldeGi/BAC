int result;

void sum1(int a1, int b1) {
    a1 = a1 + b1;
}

/*
 * @post stores the sum of the values pointed by a and b in the memory pointed by r
 */
void sum3 (int *a, int *b, int *r) {
    *r= *a + *b;
}


void main(int argc, char **argv) {
    int a1 = 5, b1 = 6;

    sum1(a1, b1);
    printf("sum1: %d\n", a1);


    int a3 = 1, b3 = 8;
    int r;
    sum3(&a3, &b3, &r);
    printf("sum3: %d\n", r);
}