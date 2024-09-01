#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_INPUT_SIZE 10000

char *read() {
    // 分配内存空间
    char *input = malloc(MAX_INPUT_SIZE);
    if (input == NULL) {
        perror("Failed to allocate memory");
        return NULL;
    }

    // Initialize input to an empty string
    input[0] = '\0';

    // Read lines until EOF or input exceeds MAX_INPUT_SIZE
    while (fgets(input + strlen(input), MAX_INPUT_SIZE - strlen(input), stdin) != NULL) {
        // 继续输入
    }

    // 调整内存空间
    input = realloc(input, strlen(input) + 1);
    if (input == NULL) {
        perror("Failed to reallocate memory");
        return NULL;
    }

    return input;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m); // 读取女歌星和男歌星的人数

    char fe_name[n][100];
    int fe_vote[n];
    for (int i = 0; i < n; i++) {
        scanf("%s %d", fe_name[i], &fe_vote[i]);
    }

    char ma_name[m][100];
    int ma_vote[m];
    for (int j = 0; j < m; j++) {
        scanf("%s %d", ma_name[j], &ma_vote[j]);
    }

    // 清除标准输入缓冲区
    getchar();

    while (1) {
        char *inputstring = read();
        if (strcmp(inputstring, "END") == 0) {
            free(inputstring);
            break;
        }

        if (strcmp(inputstring, "PK FEMALE") == 0) { // 女星排序
            for (int fi = 0; fi < n - 1; fi++) {
                for (int fj = fi + 1; fj < n; fj++) {
                    if (fe_vote[fj] > fe_vote[fi] || (fe_vote[fj] == fe_vote[fi] && strcmp(fe_name[fj], fe_name[fi]) < 0)) {
                        // 交换 fe_name 和 fe_vote
                        int temp_vote = fe_vote[fi];
                        fe_vote[fi] = fe_vote[fj];
                        fe_vote[fj] = temp_vote;

                        char temp_name[100];
                        strcpy(temp_name, fe_name[fi]);
                        strcpy(fe_name[fi], fe_name[fj]);
                        strcpy(fe_name[fj], temp_name);
                    }
                }
            }
            // 输出当前排名
            for (int out_fi = 0; out_fi < n; out_fi++) {
                printf("%d %s %d\n", out_fi + 1, fe_name[out_fi], fe_vote[out_fi]);
            }
        } else if (strcmp(inputstring, "PK MALE") == 0) { // 男星排序
            for (int mi = 0; mi < m - 1; mi++) {
                for (int mj = mi + 1; mj < m; mj++) {
                    if (ma_vote[mj] > ma_vote[mi] || (ma_vote[mj] == ma_vote[mi] && strcmp(ma_name[mj], ma_name[mi]) < 0)) {
                        // 交换 ma_name 和 ma_vote
                        int temp_vote = ma_vote[mi];
                        ma_vote[mi] = ma_vote[mj];
                        ma_vote[mj] = temp_vote;

                        char temp_name[100];
                        strcpy(temp_name, ma_name[mi]);
                        strcpy(ma_name[mi], ma_name[mj]);
                        strcpy(ma_name[mj], temp_name);
                    }
                }
            }
            // 输出当前排名
            for (int out_mi = 0; out_mi < m; out_mi++) {
                printf("%d %s %d\n", out_mi + 1, ma_name[out_mi], ma_vote[out_mi]);
            }
        } else {
            // 处理投票命令
            if (strncmp(inputstring, "VOTE ", 5) == 0) {
                int vote_i = inputstring[5] - '0';
                int vote_j = inputstring[7] - '0';
                fe_vote[vote_i]++;
                ma_vote[vote_j]++;
            }
        }

        free(inputstring);
    }

    // END命令后输出最后结果
    // 汇总姓名和得票数
    char all_name[n + m][100];
    int all_vote[n + m];
    for (int i = 0; i < n; i++) {
        strcpy(all_name[i], fe_name[i]);
        all_vote[i] = fe_vote[i];
    }
    for (int i = 0; i < m; i++) {
        strcpy(all_name[n + i], ma_name[i]);
        all_vote[n + i] = ma_vote[i];
    }

    // 排序
    for (int i = 0; i < n + m - 1; i++) {
        for (int j = i + 1; j < n + m; j++) {
            if (all_vote[j] > all_vote[i] || (all_vote[j] == all_vote[i] && strcmp(all_name[j], all_name[i]) < 0)) {
                // 交换 all_name 和 all_vote
                int temp_vote = all_vote[i];
                all_vote[i] = all_vote[j];
                all_vote[j] = temp_vote;

                char temp_name[100];
                strcpy(temp_name, all_name[i]);
                strcpy(all_name[i], all_name[j]);
                strcpy(all_name[j], temp_name);
            }
        }
    }

    // 输出最终排名
    for (int i = 0; i < n + m; i++) {
        printf("%d %s %d\n", i + 1, all_name[i], all_vote[i]);
    }

    return 0;
}
