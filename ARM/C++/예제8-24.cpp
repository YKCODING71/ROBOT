#include <stdio.h>
void main()
{ 
  int i;

 for(i=1;i<=9;i+=1)
    printf("%d*%d=%2d ", 1, i, 1*i);

 printf("\n");

 for(i=1;i<=9;i+=1)
    printf("%d*%d=%2d ", 2, i, 2*i);
}
