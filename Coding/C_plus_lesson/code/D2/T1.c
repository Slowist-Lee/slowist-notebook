#include <stdio.h>
#include <stdlib.h>
#define N 100
#define M 5
int decode(char**s);
int main()
{

    char *s[M];
    int i;
    int key;
    for(i=0; i<M; i++){
        s[i] = (char *)malloc((N+1)*sizeof(char));
        gets(s[i]);
    }


    key = decode(s);
    printf("%04d",key);
    for(i=0; i<M; i++){
        free(s[i]);
    }
    
    return 0;
}
int decode(char**s){ 
	int passcode[M-1];    //�������룬����Ϊ����-1 
	int pass_num =0 ; //���ķ���ֵ 
	char lastline[N];
	int i=0;
	for (i=0;i<N-1 && s[M-1][i] != '\0';i++){
		lastline[i]=s[M-1][i];
	} //�Ȱ����һ�е��ַ��Ž�һ���ַ�����
	int j=0;
	for (j=0;j<M-1;j++){
		int cnt=0;
		int p=0;
		for (p=0;p<N-1 && s[M-1][p] != '\0';p++){
			int k=0;
			for (k=0;k<N-1 && s[M-1][k] != '\0';k++)
				if (lastline[p]==s[j][k]){
					cnt++;
				}
		} 
	passcode [j] = cnt;
	}
	//������Ӧ���ַ����Ҵ�����������
	for (i=0;i<M-1;i++){
		pass_num= pass_num*10+passcode[i];
	}
	return pass_num;
} 
