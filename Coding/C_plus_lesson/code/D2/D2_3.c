#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int TABLE_SIZE=8;

// 1 1 2 2 5 5 10 10 -1
// 1 2 3 5 1 6 9 10 -1
// // 定义哈希表条目
// typedef struct {
//     char* key;
//     int value;
// } KeyValuePair;

// void updateHashTable(KeyValuePair* hashTable, int id) {
//     if (id >= 0 && id < TABLE_SIZE) {
//         hashTable[id].value++;
//     }
// }

// // 初始化哈希表
// KeyValuePair* createHashTable() {
//     KeyValuePair* hashTable = (KeyValuePair*)malloc(TABLE_SIZE * sizeof(KeyValuePair));
//     char* keys[TABLE_SIZE] = {"tablewater", "coca", "milk", "beer", "orangejuice", "sprite", "oolong", "greentea"};
//     for (int i = 0; i < TABLE_SIZE; i++) {
//         hashTable[i].key = malloc(strlen(keys[i]) + 1);
//         if (!hashTable[i].key) {
//             printf("Memory allocation failed!\n");
//             exit(1);
//         }
//         strcpy(hashTable[i].key, keys[i]);
//         hashTable[i].value = 0;
//     }
//     return hashTable;
// }

// // 打印哈希表
// void printHashTable(KeyValuePair* hashTable) {
//     for (int i = 0; i < TABLE_SIZE; i++) {
//         printf("%s: %d\n", hashTable[i].key, hashTable[i].value);
//     }
// }

// // 释放哈希表
// void freeHashTable(KeyValuePair* hashTable) {
//     free(hashTable);
// }

int main() {
    char *lst[10000];
    int i = 0;

    // 先读取金额
    while (i < 10000) {
        char str[1000];
        if (fgets(str, sizeof(str), stdin) == NULL) {
            break;
        }

        // // 去掉换行符
        // str[strcspn(str, "\n")] = 0;

        // 为当前行分配内存并存储
        lst[i] = malloc(strlen(str) + 1);
        strcpy(lst[i], str);
        i++;

        // 如果检测到行中含有 "-1"，停止读取
        if (strstr(str, "-1") != NULL) {
            break;
        }
    }

    // 将所有面额加起来
    int total = 0;
    int j = 0;
    for (j = 0; j < i; j++) {
        char *rest = lst[j];
        char *token = strtok(rest, " ");
        while (token != NULL) {
            if (strcmp(token, "-1") == 0) {
                break;
            }
            total += atoi(token);
            token = strtok(NULL, " ");
        }
    }
    total++;
    int total1 = total;


    // 释放分配的内存
    for (int w = 0; w < i; w++) {
        free(lst[w]);
    }

    // 再读取商品
    char *stuff[10000];
    int i3 = 0;
    while (i3 < 10000) {
        char str3[1000];
        if (fgets(str3, sizeof(str3), stdin) == NULL) {
            break;
        }

        // // 去掉换行符
        // str3[strcspn(str3, "\n")] = 0;

        // 为当前行分配内存并存储
        stuff[i3] = malloc(strlen(str3) + 1);
        strcpy(stuff[i3], str3);
        i3++;

        // 如果检测到行中含有 "-1"，停止读取
        if (strstr(str3, "-1") != NULL) {
            break;
        }
    }

    int stuff_id[10000];
    int stufflen = i3;
    // printf("i3=%d",i3);
    int i4=0;
    char *rest4 = stuff[i4];
    char *token4 = strtok(rest4, " ");
    
    while (atoi(token4)!=-1){
        stuff_id[i4] = atoi(token4);
        // printf("stuff_id[%d]=%d    ", i4,stuff_id[i4]);
        token4 = strtok(NULL, " ");
        i4++;
    }

    // int stuff_id[10000];
    // // int id_index = 0;
    // // printf("sizeof(stuff_id)/sizeof(stuff_id[0])=%d",sizeof(stuff_id)/sizeof(stuff_id[0]));
    // for (int i4 = 0; i4 < sizeof(stuff_id)/sizeof(stuff_id[0]); i4++) {
    //     // printf("id=%d        ",i4);
    //     char *rest4 = stuff[i4];
    //     char *token4 = strtok(rest4, " ");
    //     while (token4 != NULL) {
    //         if (strcmp(token4, "-1") == 0) {
    //             break;
    //         }
    //         stuff_id[i4] = atoi(token4);
    //         printf("stuff_id[i4]=%d    ",stuff_id[i4]);
    //         token4 = strtok(NULL, " ");
    //         // id_index++;
    //     }
    // }


    int price[10] = {1, 1, 1, 2, 2, 3, 3, 3, 4, 4};
    int tablewater1=0;
    int tablewater2=0;
    int tablewater3=0;
    int coca =0;
    int milk=0;
    int beer=0;
    int orangejuice=0;
    int sprite=0;
    int oolong=0;
    int greentea=0;
    for (int id = 0; id < i4; id++) {
        if ((stuff_id[id])==1){
            tablewater1++;
        }
        else if((stuff_id[id])==2){
            tablewater2++;
        }
        else if((stuff_id[id])==3){
            tablewater3++;
        }
        else if((stuff_id[id])==4){
            coca++;
        }
        else if((stuff_id[id])==5){
            milk++;
        }
        else if((stuff_id[id])==6){
            beer++;
        }
        else if((stuff_id[id])==7){
            orangejuice++;
        }
        else if((stuff_id[id])==8){
            sprite++;
        }
        else if((stuff_id[id])==9){
            oolong++;
        }
        else{
            greentea++;
        }
        if (total >= 0) {
            // printf("id=%d,Price of item %d: %d\n", id,stuff_id[id], price[stuff_id[id] - 1]);
            total -= price[stuff_id[id] - 1];
            // printf("Total after purchase: %d\n", total);
        } else {
            printf("Insufficient money\n");
            break;
        }
    }
    if (total>=0){
        printf("Total:%dyuan,", total1);
        printf("change:%dyuan\n", total);
        printf("Table-water:%d;Table-water:%d;Table-water:%d;Milk:%d;Beer:%d;Oolong-Tea:%d;Green-Tea:%d;\n",tablewater1,tablewater2,tablewater3,milk,beer,oolong,greentea);
    }
    else{
        printf("Insufficient money\n");
    }



    // 释放分配的内存
    for (int j3 = 0; j3 < i3; j3++) {
        free(stuff[j3]);
    }

    return 0;
}

