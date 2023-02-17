//
// Created by 32465 on 08-02-22.
//

#include <stdio.h>
#include <string.h>

int strcasecmpe(const char *s1, const char *s2) {
    int result1=0;
    int result2=0;
    int upper(char c) {
        if (c >= 'a' && c <= 'z')
            return c + ('A' - 'a');
        else
            return c;
    }
    for(int i=0;i<strlen(s1);i++){
        result1+= upper(s1[i]);
    }

    for(int j=0;j<strlen(s2);j++){
        result2+=upper(s2[j]);
    }
    return result1-result2;

}


int strcasecmpe2(const char *s1, const char *s2) {   /* fonctionne sur inginious*/
    int result=0;
    int upper(char c) {
        if (c >= 'a' && c <= 'z')
            return c + ('A' - 'a');
        else
            return c;
    }
    for(int i=0;i<strlen(s1)+strlen(s2);i++){
        result+= upper(s1[i])-upper(s2[i]);
        if(s1[i]=='\0'&&s2[i]=='\0'){
            return result;
        }
        else if(s1[i]=='\0'){
            result-=upper(s2[i]);
        }
        else if (s2[i]=='\0'){
            result+=upper(s1[i]);
        }
    }
    return result;
}



int main(){
    printf("Concatenation %d\n", strcasecmpe("SALUT","SALUTcava"));
    printf("Concatenation %d\n", strcasecmpe("Saluthahhahad","cavaSaluthahhahad"));
    printf("Concatenation %d\n", strcasecmpe("Salut","cava"));
    printf("\n");
    printf("Concatenation %d\n", strcasecmpe2("SALUT","SALUTcava"));
    printf("Concatenation %d\n", strcasecmpe2("Saluthahhahad","cavaSaluthahhahad"));
    printf("Concatenation %d\n", strcasecmpe2("Salut","cava"));
    printf("\n");
    printf("Concatenation %d\n", strcasecmp("SALUT","SALUTcava"));
    printf("Concatenation %d\n", strcasecmp("Saluthahhahad","cavaSaluthahhahad"));
    printf("Concatenation %d\n", strcasecmp("Salut","cava"));
    return 0;
}

