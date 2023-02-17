//
// Created by 32465 on 08-02-22.
//

#include <stdio.h>
#include <string.h>

char* strcat(char* dest, const char* src) {

    if(src[0]=='\0'){
       return dest;
    }
    else{
        int j =0;
        int longueur=0;
        for(int i=0;dest[i]!='\0';i++){
            longueur++;
            j++;

        }

        for(int i=0;src[i]!='\0';i++){
            dest[longueur+i]=src[i];
            j++;
        }
       
        dest[j+1]='\0';
        return dest;
    }
}




int main(){
    char dest[100] = {'b','o','n','j','o','u','r'};
    printf("Concatenation: %s\n", strcat(dest,"çava"));
    return 0;
}

