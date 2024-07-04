#include<stdio.h>
#include<stdlib.h>

 //定义一个链表节点 
struct Node {
		int data; //编号
		struct Node* next; //指针，指向下一个节点 
};

// 创建新节点
struct Node* createNode(int data) {
    	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    	newNode->data = data;
    	newNode->next = NULL;
    	return newNode;
} 

// 插入节点到链表头部
void insertAtHead(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

//创建循环链表
struct Node* createCircularList(int n) {
	struct Node* head = NULL;
	struct Node* temp;
	int i=n;
	for (i=n;i>=1;i--){
		insertAtHead(&head,i);
	} 
	temp = head;
	int cnt =0;
	while (temp->next != NULL){
		temp = temp->next;
	} 
	temp->next = head; //循环
	return head; 
}

int main(){
	int n;
	int m;
	printf("请输入n、m");
	scanf("%d %d",&n,&m);
	int cnt = 1;
	struct Node* head = createCircularList(n);
	struct Node* temp= head;
	struct Node* prev = NULL;
	while (head != head->next){
		for (cnt =1; cnt<m;cnt++){
			prev = temp;
			temp = temp->next;
		}
		if (head == temp){
			head = temp->next;	
		}	
		prev->next = temp->next;
		free(temp);	
		temp=prev->next;
	}
	printf("%d",head->data);
	return 0;
}
