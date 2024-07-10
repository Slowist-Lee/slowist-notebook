#include<stdio.h>
#include <stdbool.h>
int main()
{
	int n;
	scanf("%d",&n);
	int i=0;
	int j=0;
	int k=0;
	bool flag=true;
	char a[n][15],b[n][15],c[n][15];
	int d[n];
	while(~scanf("%s %s %s",a[i],b[i],c[i]))
	{
		if((a[i][0]=='9'||a[i][2]=='0')&&(b[i][0]=='9'||b[i][2]=='0')&&(c[i][0]=='9'||c[i][2]=='0'))
		{
			flag=false;
			d[j]=i;
			j=j+1;
		}
		i=i+1;
	}
	if(flag)
	{
		printf("None.\n");
	}
	else
	{
		while(d[k]!=0)
		{
			printf("%d\n",d[k]);
			k=k+1;
		}
	}
	return 0;
}