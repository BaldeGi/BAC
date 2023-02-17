#include <stdio.h>
#include <strings.h>
#include <string.h>
#include <stdint-gcc.h>

float minimum(){
#define L 2
#define C 3
    float matriceR[L][C] = { {1.0,2.0,3.0},
                             {-4.0,5.0,6.0} };
    int i, j;
    const float FLT_MAX;
    float min = FLT_MAX;
    for (i = 0; i < L; i++)
        for (j = 0; j < C; j++)
            if (matriceR[i][j] < min)
                min=matriceR[i][j];

    return min;
}

// conversion de minuscules en majuscules
int toUpper(char c) {
    if (c >= 'a' && c <= 'z')
        return c + ('A' - 'a');
    else
        return c;
}

/* print_digit
 * @n: an integer
 *
 * result: print to stdout "The magic number is NUMBER.\n"
 */
int print_digit(int number) {
    printf("The magic number is %d.\n",number);
}

void print_foo() {
    printf("foo\n");
}

/* format_str, example:
 * format_str(buf, 42, "Olivier", 'B') will write into buf
 * the string "Mister Olivier B. has 42 eggs" (no line feed)
 * The given buffer is guaranteed to be big enough
 */


size_t strlen(const char* s) {
    int i =0;
    while(s[i]!='\0'){
        i++;
    }
    return i;
}

int strcasecmp(const char *s1, const char *s2) {
    int s=0;
    int a =0;
    for(int i = 0; s1[i]!='\0';i++){
        s = s+s1[i];
    }
    for(int i = 0; s2[i]!='\0';i++){
        s = s+s2[i];
    }
    if(s<a){
        return -1;
    }
    else if (s>a){
        return 1;
    }
    else{
        return 0;
    }
}

int main() {
    printf("Hello, World!\n");
    printf("La plus petite valeur est %lf \n", minimum());
    printf("La majuscule correspondante est %c\n", toUpper('b'));
    char c= 'b';
    printf("L'adresse de la variable %p",&c);
    print_digit(3);
    float PI = 3.1415926;
    printf("pi = %.4f \n", PI);
    print_foo();
   
    printf("%d",strlen("bonjours"));
    return 0;
}











