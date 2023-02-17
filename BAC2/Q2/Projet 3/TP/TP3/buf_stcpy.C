#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
* Creates a buffer that has the same size as src, and copies the content of src to this buffer.
*
* @src: string to be copied
* @return: return pointer. if src == NULL or in case of error, return NULL
*
* Remember that strings are terminated with '\0' and that strlen("abc") returns 3 even if 4 bytes are required to store this string.
*/
char *buf_strcpy(const char *src) {
    size_t size=strlen(src);
    char *buffer = (char* )malloc(sizeof(char)*(size+1));
    if(buffer==NULL){
        return NULL;
    }

    for(int i=0; src[i]!='\0';i++){
        buffer[i] = src[i];
    }
    buffer[size] = '\0';

    return buffer;


}

int main(){
    const char *src="abcd";
    printf("%s",buf_strcpy(src));
    return 0;
}