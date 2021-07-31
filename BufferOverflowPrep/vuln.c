#include<stdio.h>
#include<string.h>

int main(int argc, char** argv) {
    char buffer[500];
    printf("Length of ARGV[1]: %d\n", strlen(argv[1]));
    memcpy(buffer, argv[1], strlen(argv[1]));

    printf("%s\n", buffer);
    return 0;
}