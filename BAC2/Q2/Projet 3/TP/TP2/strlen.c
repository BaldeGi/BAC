//
// Created by 32465 on 08-02-22.
//
#include <stdio.h>

size_t strlen(const char* s) {
    int i =0;
    while(s[i]!='\0'){
        i++;
    }
    return i;
}

