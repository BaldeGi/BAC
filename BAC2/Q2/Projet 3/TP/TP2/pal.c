#include <stdio.h>
#include <string.h>


/*
* @return: returns true (1) if str is a palindrome, -1 if str is NULL, otherwise false (0).
*/
int pal(char *str) {

    if(str==NULL){
            return -1;
    }

    /*Fonction auxillaire*/
    int toUpper(char c) {
        if (c >= 'a' && c <= 'z')
            return c + ('A' - 'a');
        else
            return c;
    }

    int backward=strlen(str)-1;
    int i=0;
    while (i<strlen(str)){
        if(toUpper(str[i])!= ' ' && toUpper(str[backward])!=' '){
            if(toUpper(str[i])!=toUpper(str[backward])){
                return 0;
            }
            else{
                backward--;
                i++;
            }
        }
        else if(toUpper(str[i])==' '){
            i++;
            continue;
        }
        else{
            backward--;
        }
    }   
    return 1;
}

int pale(char *str) {   /* Fonction qui fonctionne sur inginious */
    if(str==NULL){
        return -1;
    }
    int backward=strlen(str)-1;
    int i=0;
    while (i<backward){
        if(str[i]==' '){
            i++;
        }
        if(str[backward]==' '){
            backward--;
        }
        if(str[i]!= ' ' && str[backward]!=' '){
            if(str[i]!=str[backward]){
                return 0;
            }
            backward--;
            i++;
        }
    }   
    return 1;
}




int main(){
    printf("Palindrome %d\n",pal(" KAyak"));
    printf("Palindrome %d\n",pal("k ayaka"));
    printf("Palindrome %d\n",pal("kaya k"));
    printf("Palindrome %d\n",pal("bayak"));
    printf("Palindrome %d\n",pal("ayaka"));
    return 0;
}