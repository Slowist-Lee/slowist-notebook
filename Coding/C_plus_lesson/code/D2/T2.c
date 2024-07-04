#include<stdio.h>
#include<stdlib.h>

 //����һ������ڵ� 
struct Node {
		int data; //���
		struct Node* next; //ָ�룬ָ����һ���ڵ� 
};

// �����½ڵ�
struct Node* createNode(int data) {
    	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    	newNode->data = data;
    	newNode->next = NULL;
    	return newNode;
} 

// ����ڵ㵽����ͷ��
void insertAtHead(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

//����ѭ������
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
	temp->next = head; //ѭ��
	return head; 
}

int main(){
	int n;
	int m;
	printf("������n��m");
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
