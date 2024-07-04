#include <stdio.h>

int main(void){
    int m;
    int w;
    scanf("%d %d",&m,&w);
    if (m>=9 && m<=12 || m==1){
        if (w == 1){ 
            printf("星期一，有C语言课程要完成"); //第一周
        }
        else if (w>=2 && w<=7)
        {
            printf("其他课程");
        }
        else{
            printf("对于week变量，请输入1-7的整数！");
        }
    }
    else if (m == 2){
        printf("寒假！");
    }
    else if (m>=3 && m<=6){
        printf("大一下学期了！");
    }
    else if (m==7 || m== 8 ){
        printf("暑假！");
    }
    else{
        printf("对于month变量，请输入1-12的整数！");
    }

}


