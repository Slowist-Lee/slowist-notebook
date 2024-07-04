#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <ctype.h>

bool is_number(char *str) {
    while (*str) {
        if (!isdigit(*str)) {
            return false;
        }
        str++;
    }
    return true;
}

bool judge_pr_failed(char *a, char *b) {
    int a1;
    int b1;
    char *endptr;
    if (is_number(a)) {
        a1 = strtol(a, &endptr, 10);
    } else {
        a1 = 0;
    }
    if (is_number(b)) {
        b1 = strtol(b, &endptr, 10);
    } else {
        b1 = 0;
    }
    if (a1 < 10.0 && b1 < 15.0) {
        return false;
    } else {
        return true;
    }
}

int min(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int main(void) {
    char *lst[10000];
    int i = 0;

    while (i < 10000) {
        char str[1000]; 
        if (fgets(str, sizeof(str), stdin) == NULL) {
            break;
        }

        
        lst[i] = malloc(strlen(str) + 1);
        strcpy(lst[i], str);
        i++;
    }

    char *name[i];
    char *id[i];
    char *attendence[i];
    char *homework[i];
    char *quiz[i];
    char *th_test[i];
    char *pr_test1[i];
    char *pr_test2[i];
    char *pr_atest1[i];
    char *pr_atest2[i];
    char *endptr;
    bool pass = true;
    for (int j = 1; j < i; j++) {
        char *rest = lst[j];
        name[j] = strtok(rest, " "); // ��ȡ����
        id[j] = strtok(NULL, " "); // ��ȡѧ�� 
        attendence[j] = strtok(NULL, " "); // ���ڳɼ� 
        homework[j] = strtok(NULL, " "); // ��ҵ�ɼ� 
        quiz[j] = strtok(NULL, " "); // С��ɼ�
        th_test[j] = strtok(NULL, " "); // ���ۿ��Գɼ�
        pr_test1[j] = strtok(NULL, " "); // ʵ�鿼�Գɼ� 1
        pr_test2[j] = strtok(NULL, " "); // ʵ�鿼�Գɼ� 2
        pr_atest1[j] = strtok(NULL, " "); // ʵ�鲹���ɼ� 1
        pr_atest2[j] = strtok(NULL, " "); // ʵ�鲹���ɼ� 2
    }
    double grade[i];
    int n = 0;
    double Att;
    double Hom;
    double Quiz;
    double Th_test;
    double Pr_test = 0.0;
    for (n = 1; n < i; n++) {
        Att = strtod(attendence[n], &endptr);
        grade[n] = Att;

        Hom = strtod(homework[n], &endptr);
        grade[n] += 0.2 * Hom;

        if (is_number(quiz[n])) {
            Quiz = strtod(quiz[n], &endptr);
            grade[n] += 0.25 * Quiz;
        }
        // // ���ӵ�����Ϣ
        // printf("Student: %s, ID: %s\n", name[n], id[n]);
        // printf("Initial grade: %.2f\n", grade[n]);

        if (is_number(pr_test1[n]) || is_number(pr_test2[n])){
            if (judge_pr_failed(pr_test1[n], pr_test2[n])) {
                pass = true;
                Pr_test=0.0;
                Pr_test += strtod(pr_test1[n], &endptr);
                Pr_test += strtod(pr_test2[n], &endptr);
                Pr_test = 10.0 + sqrt(Pr_test);
                grade[n] += Pr_test; // ��һ�ξ͹��ˣ���������ʵ��÷�
                // printf("Passed first experiment, Pr_test: %.2f\n", Pr_test);
            } else {
                // ��һ��û������Ҫ�жϵڶ�����û�й�
                if (judge_pr_failed(pr_atest1[n], pr_atest2[n])) {
                    pass = true;
                    grade[n] += 9; // �ڶ��ι��ˣ��̶���9��
                    // printf("Passed second experiment, fixed Pr_test: 9\n");
                } else {
                    Pr_test=0.0;
                    pass = false; // ֱ�ӹҿ�
                    if (is_number(pr_test1[n])) {
                        Pr_test += strtod(pr_test1[n], &endptr);
                    }
                    if (is_number(pr_test2[n])) {
                        Pr_test += strtod(pr_test2[n], &endptr);
                    }
                    Pr_test = 10.0 + sqrt(Pr_test);
                    grade[n] += Pr_test; // Ҳ��������ʵ��÷�
                    // printf("Failed both experiments, Pr_test: %.2f\n", Pr_test);
                }
            }
        }
        else{
            if (is_number(pr_atest1[n]) || is_number(pr_atest2[n])){
            // ��һ��û������Ҫ�жϵڶ�����û�й�
                if (judge_pr_failed(pr_atest1[n], pr_atest2[n])) {
                    pass = true;
                    grade[n] += 9; // �ڶ��ι��ˣ��̶���9��
                    // printf("Passed second experiment, fixed Pr_test: 9\n");
                } else {
                    Pr_test=0.0;
                    pass = false; // ֱ�ӹҿ�
                    if (is_number(pr_test1[n])) {
                        Pr_test += strtod(pr_test1[n], &endptr);
                    }
                    if (is_number(pr_test2[n])) {
                        Pr_test += strtod(pr_test2[n], &endptr);
                    }
                    Pr_test = 10.0 + sqrt(Pr_test);
                    grade[n] += Pr_test; // Ҳ��������ʵ��÷�
                    // printf("Failed both experiments, Pr_test: %.2f\n", Pr_test);
                }  
            }
        }
        Th_test = strtod(th_test[n], &endptr);
        grade[n] += 0.35 * Th_test;
        // printf("Theory test: %.2f, Total grade so far: %.2f\n", Th_test, grade[n]);
        if (Th_test < 50) {
            pass = false;
            // printf("Theory test failed, score < 50\n");
        }
        if (pass == false) {
             grade[n] = min(59, round(grade[n]));
            // printf("Final grade adjusted to minimum of 59 or current total\n");
        }
    }

    // ���ÿ���б���ֵ
    for (int x = 1; x < i; x++) {
        printf("%s %s %.0f\n", name[x], id[x], round(grade[x]));
    }

    // �ͷŶ�̬������ڴ�
    for (int s = 0; s < i; s++) {
        free(lst[s]);
    }

    return 0;
}

