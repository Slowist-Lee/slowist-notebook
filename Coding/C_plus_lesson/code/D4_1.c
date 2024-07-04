#include<stdio.h>
#include<string.h>
int main(){
    int n;
    int m;
    scanf("%d %d",&n,&m); //读取女歌星和男歌星的人数
    char fe_name[n][100];
    int fe_vote[n];
    for (int i=0;i<n;i++){
        scanf("%s %d",fe_name[i],&fe_vote[i]);
        //printf("%s %d\n",fe_name[i],fe_vote[i]); 测试语句
    }
    char ma_name[m][100];
    int ma_vote[m];
    for (int j=0;j<m;j++){
        scanf("%s %d",ma_name[j],&ma_vote[j]);
    }
    char inputstring[100];
    scanf("%s",inputstring);
    while (strcmp(inputstring,"END")!=0){
        if (strcmp(inputstring,"PK FEMALE")==0){ //女星排序
            printf("%s",inputstring);
            for (int fi=0; fi<n;fi++){
                int fk=fi;
                for (int fj=fi+1;fj<n;fj++){
                    if ((fe_vote[fj]>fe_vote[fk])||(fe_vote[fj]==fe_vote[fk]&&(int)fe_name[fj][0]<(int)fe_name[fk][0])){
                        fk=fj;
                }
                char fe_name_tmp[100];
                strcpy(fe_name_tmp, fe_name[fk]);
                strcpy(fe_name[fk], fe_name[fi]);
                strcpy(fe_name[fi], fe_name_tmp);
                }
            }
            //输出当前排名
            for (int out_fi=0;out_fi<n;out_fi++){
                printf("%d %s %d\n",out_fi+1,fe_name[out_fi],fe_vote[out_fi]);
            }
        }
        else if (strcmp(inputstring,"PK MALE")==0){ //男星排序
            printf("%s",inputstring);
            for (int mi=0; mi<m;mi++){
                int mk=mi;
                for (int mj=mi+1;mj<m;mj++){
                    if ((ma_vote[mj]>ma_vote[mk])||(ma_vote[mj]==ma_vote[mk]&&(int)ma_name[mj][0]<(int)ma_name[mk][0])){
                        mk=mj;
                    }
                }
                char ma_name_tmp[100];
                strcpy(ma_name_tmp, ma_name[mk]);
                strcpy(ma_name[mk], ma_name[mi]);
                strcpy(ma_name[mi], ma_name_tmp);
            }
            //输出当前排名
            for (int out_mi=0;out_mi<m;out_mi++){
                printf("%d %s %d\n",out_mi+1,ma_name[out_mi],ma_vote[out_mi]);
            }
        }
        else{
            int vote_i= inputstring[5]-'0';
            int vote_j= inputstring[7]-'0';
            fe_vote[vote_i]++;
            ma_vote[vote_j]++;
        }
        scanf("%s",inputstring);
    }
    //END命令后输出最后结果
    //先汇总姓名和得票数
    char all_name[n+m][100];
    int all_vote[n+m];
    //先放女星
    for (int f_all_i=0;f_all_i<n;f_all_i++){
        strcpy(all_name[f_all_i],fe_name[f_all_i]);
        all_vote[f_all_i]=fe_vote[f_all_i];
    }
   //再放男星
    for (int m_all_i=0;m_all_i<m;m_all_i++){
        strcpy(all_name[n+m_all_i],ma_name[m_all_i]);
        all_vote[n+m_all_i]=ma_vote[m_all_i];
    }

    //排序
    for (int endi=0; endi<n;endi++){
        int endk=endi;
        for (int endj=endi+1;endj<n+m;endj++){
            if ((all_vote[endj]>all_vote[endk])||(all_vote[endj]==all_vote[endk]&&(int)all_name[endj][0]<(int)all_name[endk][0])){
                endk=endj;
            }
            char all_name_tmp[100];
            strcpy(all_name_tmp, all_name[endk]);
            strcpy(all_name[endk], all_name[endi]);
            strcpy(all_name[endi], all_name_tmp);
                }
            }
            //输出当前排名
            for (int out_endi=0;out_endi<n;out_endi++){
                printf("%d %s %d\n",out_endi+1,all_name[out_endi],all_vote[out_endi]);
            }
    return 0;
}
