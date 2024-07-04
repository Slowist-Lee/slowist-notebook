#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "This is a test string";
    char *token;

    // 第一次调用 strtok，传入要分割的字符串
    token = strtok(str, " ");

    // 循环获取后续的令牌
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }

    return 0;
}

