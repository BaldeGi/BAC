int first(void *ptr) {
    int *a = ptr+3*sizeof(int);     // equivaut à ptr+12
    return *a;
}

char second(void *ptr){
    char *a = ptr+6*sizeof(char);
    return *a;
}


int third(void *ptr) {
    int *a = ptr+11*sizeof(int)+1;
    return *a;
}



int main(){

    int ptre = 4;
    printf("%d\n",first(&ptre));

    int ptree = 4;
    printf("%d\n",third(&ptree));
    
    char ptr = 'a';
    printf("%c",second(&ptr));
    return 0;
}