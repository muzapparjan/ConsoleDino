#include <stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <stdlib.h>
#include <unistd.h>

void printBuffer(const char *buffer, int size) {
    fwrite(buffer, 1, size, stdout);
}

int main() {
    struct winsize size;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &size);

    // printf("Number of columns: %d\n", size.ws_col);
    // printf("Number of rows: %d\n", size.ws_row);
    if(size.ws_col < 100 || size.ws_row < 40){
        printf("shell window is too small !!\n");
        return 0;
    }
    int window_size = size.ws_col * size.ws_row;
    char* buffer;
    buffer = (char*)malloc(sizeof(char) * window_size);
    buffer[0] = 'a';
    for(int j = 0; j < size.ws_row - 1; j++){
        buffer[j*size.ws_row + size.ws_col -1] = '\n';
    }
    int i = 0;
    while(i < size.ws_row){
        system("clear"); 
        printBuffer(buffer, window_size);
        buffer[i*size.ws_col + i] = ' ';
        i++;
        buffer[i*size.ws_col + i] = 'a';
        sleep(1/60);
    }
    return 0;
}

// int main() {
//     char buffer[] = "Hello, World!";
//     int size = sizeof(buffer) - 1; // 减去末尾的空字符
    
//     printBuffer(buffer, size);

//     return 0;
// }