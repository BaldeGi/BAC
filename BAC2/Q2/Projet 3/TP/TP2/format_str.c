#include<stdio.h>

/* format_str, example:
 * format_str(buf, 42, "Olivier", 'B') will write into buf
 * the string "Mister Olivier B. has 42 eggs" (no line feed)
 * The given buffer is guaranteed to be big enough
 */
void format_str(char *buffer, unsigned int d, char *name, char initial) {
    sprintf(buffer,"Mister %s %c. has %d eggs",name,initial,d);
}

int main(){
    char buf[256];
    printf("res : %s",format_str(buf,23, "Olivier",'B'));
    return 0;
}