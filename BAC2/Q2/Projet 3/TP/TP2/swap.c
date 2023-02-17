#include <stdio.h>


struct fract_t{
    int num;
    int denum;
};


void swap(struct fract_t *a, struct fract_t *b){

   
    struct fract_t temp = *a;
    a->num = b->num;
    a->denum = b->denum;
    b->num = temp.num;
    b->denum = temp.denum;

    
    
    
}




int main() {
    
    return 0;
}
