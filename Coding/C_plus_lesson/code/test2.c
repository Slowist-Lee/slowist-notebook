#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "This is a test string";
    char *token;

    // ��һ�ε��� strtok������Ҫ�ָ���ַ���
    token = strtok(str, " ");

    // ѭ����ȡ����������
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }

    return 0;
}

