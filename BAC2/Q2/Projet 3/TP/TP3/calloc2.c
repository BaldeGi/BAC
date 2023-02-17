#include <stdlib.h>

void *calloc2(size_t nmemb, size_t size) {
    if(nmemb==0||size==0){
        return NULL;
    }
    size_t *b;
    b =malloc(nmemb*size);
    return b;
}


int main(){
    return 0;
}