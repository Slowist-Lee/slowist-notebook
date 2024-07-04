#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include "../pstring.h"

/*
typedef struct {
	int length;
	char content[];
} PString;
*/

//check

//	create an object of PString with its content as s
PString* psCreate(const char* s){
    int len = strlen(s);
    PString* ps = (PString *)malloc(sizeof(int) + len * sizeof(char));
    int i = 0;
    while(s[i]){
        ps->content[i] = s[i];
        i++;
    }
    ps->length = len;
    return ps;
}

//check

//	release the object ps
void psFree(PString *ps){
    free(ps);
}

//check

//	print ps
void psPrint(const PString* ps){
    int i = 0;
    while(i < ps->length){
        putchar(ps->content[i]);
        i++;
    }
}

//	read a word, which is seperated by space
PString* psReadWord(){
    char *temp = (char *)malloc(1e10*sizeof(char));
    scanf("%s", temp);
    getchar();
    int len = strlen(temp);
    PString *ps = (PString *)malloc(sizeof(int) + len * sizeof(char));
    int i = 0;
    while(i < strlen(temp)){
        ps->content[i] = temp[i];
        i++;
    }
    ps->length = len;
    return ps;
}

//	read a line
PString* psReadLine(){
    char *temp = (char *)malloc(1e10*sizeof(char));
    char ch = getchar();
    int i = 0;
    while(ch != '\n'){
        temp[i] = ch;
        i++;
        ch = getchar();
    }
    int len = strlen(temp);
    PString *ps = (PString *)malloc(sizeof(int) + len * sizeof(char));
    i = 0;
    while(temp[i]){
        ps->content[i] = temp[i];
        i++;
    }
    ps->length = len;
    return ps;
}

//check

//	returns the number of characters in the PString object, i.e. the length of the string
int psLength(const PString* ps){
    return ps->length;
}

//check

//	clone a PString object
//	return the new one
PString* psClone(const PString *ps){
    PString* clone = (PString *)malloc(sizeof(int) + ps->length * sizeof(char)); 
    clone->length = ps->length;
    int i = 0;
    while(i < ps->length){
        clone->content[i] = ps->content[i];
        i++;
    }
    return clone;
}

//check

//	concat two PString into a new one
//	return the new one
PString* psConcat(const PString* ps1, const PString* ps2){
    int len = ps1->length + ps2->length;
    PString *new = (PString *)malloc(sizeof(int) + len * sizeof(char));
    int i = 0 , j = 0;
    while(i < ps1->length){
        new->content[i] = ps1->content[i];
        i++;
    }
    while(j < ps2->length){
        new->content[i + j] = ps2->content[j];
        j++;
    }
    new->length = len;
    return new;
}

//check

//	compare two PString objects
//	returns -1 if ps1 is < ps2; 0 if ps1 == ps2; 1 if ps1 > ps2
int psCompare(const PString* ps1, const PString* ps2){
    int i = 0;
    while (i < ps1->length && i < ps2->length)
    {
        if(ps1->content[i] > ps2->content[i]){
            return 1;
        }
        else if(ps1->content[i] < ps2->content[i]){
            return -1;
        }
        i++;
    }
    if(ps1->length > ps2->length) return 1;
    else if(ps1->length == ps2->length) return 0;
    else return -1;
}

//check

//	find the location of ch in the ps
//	return the location of the first ch in ps, -1 if ch is not in ps
int psFindChar(const PString* ps, char ch){
    int i = 0;
    while(i < ps->length){
        if(ps->content[i] == ch) return i;
        i++;
    }
    return -1;
}

//check

//	find the first location of ps2 in ps1
//	return the location, NULL is not found
int psFindString(const PString* ps1, const PString* ps2){   //there may be some bugs in this function 
   int len = ps2->length;
   int end = ps1->length - len;
   char *temp = (char *)malloc(1e10*sizeof(char));
  
   int i = 0;
   while(i <= end){
       int j = 0;
       while(j < len){
           temp[j] = ps1->content[i + j];
           j++;
       }
       temp[j] = '\0';
        PString *Temp = psCreate(temp);
        if(psCompare(ps2,Temp) == 0) return i;
        else i++;
   } 
   return -1;
 }

//check

//	get rid of the space at both end
//	return the new created string
PString* psTrim(const PString* ps){
    char *temp = (char *)malloc(1e10*sizeof(char));
    int i = 0, j = 0, flag = 0;
    while(i < ps->length){
        if(ps->content[i] == ' ' && flag == 0){
            i++;
        }
        else{
            temp[j] = ps->content[i];
            j++;
            i++;
            flag++;
        }
    }
    temp[i] = '\0';
    i = strlen(temp) - 1;
    while(temp[i] == ' ' && i >= 0){
        temp[i] = '\0';
        i--;
    }


    int len = strlen(temp);
    PString * new = (PString *)malloc(sizeof(int) + len * sizeof(char));
    i = 0;
    while(i < len){
        new->content[i] = temp[i];
        i++;
    }
    new->length = len;
    return new;
}

//check

//	turn every character in ps into lower case
//	return the new lowered string
PString* psLower(const PString* ps){
    int len = ps->length;
    PString* new = (PString *)malloc(sizeof(int) + len * sizeof(char));
    int i = 0;
    while(i < len){
        if(ps->content[i] <= 'Z' && ps->content[i] >= 'A'){
            new->content[i] = ps->content[i] - 'A' + 'a';
            i++;
        }
        else{
            new->content[i] = ps->content[i];
            i++;
        }
    }
    new->length = len;
    return new;
}

//check

//	turn every character in ps into upper case
//	return the new uppered string
PString* psUpper(const PString* ps){
    int len = ps->length;
    PString* new = (PString *)malloc(sizeof(int) + len * sizeof(char));
    int i = 0;
    while(i < len){
        if(ps->content[i] <= 'z' && ps->content[i] >= 'a'){
            new->content[i] = ps->content[i] - 'a' + 'A';
            i++;
        }
        else{
            new->content[i] = ps->content[i];
            i++;
        }
    }
    new->length = len;
    return new;
}

//check

//	take a subset of the string ps. The subset is from begin to end.
//	For example, psSubstring(psCreate(“0123456789”), 3,5) returns a PString as “345”
//	return the new extracted string
PString* psSubstring(const PString* ps, int begin, int end){
    int len;
    len = end - begin;
    PString * new = (PString *)malloc(sizeof(int) + len * sizeof(char));
    new->length = len;
    int i = begin , j = 0;
    while(i < end){
        new->content[j++] = ps->content[i++];
    }
    return new;
}

//check

//	replace every ch1 in ps with ch2
//	return the replaced string
PString* psReplace(const PString* ps, char ch1, char ch2){
    PString * new = (PString *)malloc(sizeof(int) + ps->length * sizeof(char));
    int i = 0;
    while(i < ps->length){
        if(ps->content[i] == ch1){
            new->content[i] =ch2;
            i++;
        }
        else{
            new->content[i] = ps->content[i];
            i++;
        }
    } 
    new->length = ps->length;
    return new;
}

//check

//	return the char at the index
char psChar(const PString* ps, int index){
    return ps->content[index];
}

//check

//	return 1 if the ps1 begins with ps2, 0 otherwise
int psBeginWith(const PString* ps1, const PString* ps2){
    int i = 0;
    if(ps2->length > ps1->length)return 0;
    while(i < ps2->length){
        if(ps1->content[i] != ps2->content[i]){
            return 0;
        }
        i++;
    }
    return 1;
}
