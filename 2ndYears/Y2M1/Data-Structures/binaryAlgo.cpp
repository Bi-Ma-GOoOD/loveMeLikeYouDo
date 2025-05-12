#include <stdio.h>

/* structure for a node */
struct Node
{
	int data;
	struct Node *next;
};

/* การสร้าง Node เพื่อเก็บข้อมูลเลขจำนวน */
void insertNum(struct Node **start_ref, int data);
/* Function นี้คือการใช้ Algorithm ที่ชื่อว่ Bubble ในการ sort ตัวเลข */
void sortBubble(struct Node *start);
/* Node ที่ทำการสลับ */
void swap(struct Node *a, struct Node *b);
/* print List ที่ sort และนำไปเข้า binarySearch ต่อเลย */
void printList(struct Node *start);
/* parameter ที่เราต้องการ คือ Array, ตัวเลขที่ต้องการ, จุดเริ่มต้นของ Array, จุดสุดท้ายของ Array*/
int binarySearch(int a[], int want, int s, int l, int *ptr_count);
void choice(int answer, int target_number, int rounds);

int main()
{
	struct Node *start = NULL;
	int value;

	while(1){
		scanf("%d",&value);
		if(value == -1) {break;}
		else{
			insertNum(&start, value);
		}
	}

	sortBubble(start);
	printf("\n");
	printList(start);
}


void insertNum(struct Node **start_ref, int data)
{
	Node *ptr1 = new Node();
	ptr1->data = data;
	ptr1->next = *start_ref;
	*start_ref = ptr1;
}

void printList(struct Node *start)
{
	struct Node *temp = start;
	int sorted[] = {0};
	int index = 0;
	int count = 0;
	int target_number = 0;
	printf("After sort:\n");
	while (temp!=NULL)
	{
		sorted[index] = temp->data;
		printf("%d ", temp->data);
		temp = temp->next;
		index++;
	}
	printf("\n- - - - - - - - - - - - - - -\n");
	int find_index1 = binarySearch(sorted, 5, 0, 15, &count);
    target_number = 5;
    choice(find_index1, target_number, count);

	printf("- - - - - - - - - - - - - - -\n");

    count = 0;
    int index2 = binarySearch(sorted, 90, 0, 15, &count);
    target_number = 90;
    choice(index2, target_number, count);
}

void sortBubble(struct Node *start)
{
	int swapped, i;
	struct Node *ptr1;
	struct Node *lptr = NULL;

	/* Checking for empty list */
	if (start == NULL)
		return;

	do
	{
		swapped = 0;
		ptr1 = start;

		while (ptr1->next != lptr)
		{
			if (ptr1->data > ptr1->next->data)
			{
				swap(ptr1, ptr1->next);
				swapped = 1;
			}
			ptr1 = ptr1->next;
		}
		lptr = ptr1;
	}
	while (swapped);
}

void swap(struct Node *a, struct Node *b)
{
	int temp = a->data;
	a->data = b->data;
	b->data = temp;
}

int binarySearch(int a[], int numWant, int left, int right, int *ptr_count){
    *ptr_count = (*ptr_count) + 1; // นับ รอบว่าหาทั้งหมดกี่ครั้ง
    int mid_point = left + (right-left) / 2;// ทำการค้นหาตัวตรงกลาง เพื่อเป็นการที่ว่าจะเลือกตัดซ้าย หรือ ขวา ของ Array

    if(left > right) return -1;

    // ถ้าหากตัวตรงกลาง มีค่าเท่ากับ ตัวเลข เลย ก็ให้คืน ค่านั้น
    if(a[mid_point] == numWant) return mid_point;

    /*ถ้าหากว่า ค่าตรงกลางมีค่ามากกว่า ตัวเลขที่เราต้องการเราจะ recursion โดยส่งค่า 
    Array, ตัวเลขที่เราต้องการ, ตำแหน่งซ้ายสุด, และตำแหน่งที่มากที่สุด คือ mid -1 ในตอนนี้ 
    เหตุผลที่ต้อง mid -1 เพราะว่า เรารู้ว่า ค่า mid เรามากว่า เลขที่เราต้องการ ดังนั้นเราจึงลดค่า mid ลง 1 ตำแหน่ง*/
    else if(a[mid_point] > numWant) return binarySearch(a, numWant, left, mid_point-1, ptr_count);

    /* ถ้าหากว่า ตำแหน่งตรงกลาง น้อยกว่า ตัวเลขที่เราต้องการ เราก็จะส่ง Array, mid +1, ตำแหน่งขวาสุด 
    เหตุผลที่ ค่าน้อยที่สุดของเราเปลี่ยนเป็น mid + 1 เพราะว่า เรารู้ว่า ค่าตรงกลางมันน้อยกว่า ซึ่งหมายความว่าค่าที่อยู่
    ก่อนนห้าตรงกลางทั้งหมดรวมถึงตรงกลางเองก็ต้องน้อยกว่าด้วย ดังนั้นเราจึงปรับค่า mid ให้สูงขึ้นอีก 1 คับผม*/
    else
        return binarySearch(a, numWant, mid_point + 1, right, ptr_count);
}

void choice (int answer, int target_number, int rounds){
    if(answer != -1) printf("index of %d is %d\nAnd use %d Rounds to find it.\n", target_number, answer, rounds);
    else
        printf("We trying for %d rounds to find index of %d. But not found....", rounds, target_number);
}