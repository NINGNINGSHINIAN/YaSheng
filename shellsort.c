#include<stdio.h>

/*void shellsort(int v[], int n)
{
	int gap, i, j, temp;
	
	for (gap = n/2;gap > 0;gap = gap / 2)
		for(i = gap;i < n;i++)
			for(j = i - gap;j >= 0 && v[j] > v[j+gap];j = j - gap){
				temp = v[j];
				v[j] = v[j+gap];
				v[j+gap] = temp;
			}
}

void main()
{
	int i;
	int v[] = {1, 3, 5, 2, 8, 6};
	int n = sizeof(v) / sizeof(int);
	
	shellsort(v, n);
	for (i = 0;i < n;i++)
		printf("%d ", v[i]);
}

void bubblesort(int v[], int n)
{
	int i, j;
	
	for(i = 0; i < n;i++)
		for(j = 0;j < n - i ;j++)
		if (arr[j] > arr[j + 1]) 
		{temp = arr[j];
        arr[j] = arr[j + 1];
      	arr[j + 1] = temp;
                        }
}*/

#include <stdio.h>
void bubble_sort(int arr[], int len) {
        int i, j, temp;
        for (i = 0; i < len - 1; i++)
                for (j = 0; j < len - 1 - i; j++)
                        if (arr[j] > arr[j + 1]) {
                                temp = arr[j];
                                arr[j] = arr[j + 1];
                                arr[j + 1] = temp;
                        }
}

int main() 
{
        int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
        int len = (int) sizeof(arr) / sizeof(*arr);
        printf("%d ", len);
        bubble_sort(arr, len);
        
		int i;
        for (i = 0; i < len; i++)
                printf("%d ", arr[i]);
}
