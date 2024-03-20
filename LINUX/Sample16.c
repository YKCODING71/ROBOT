#include <stdio.h>

/* max 함수의 선언 */
int max(int x, int y);

int main(void)
{
   int num1, num2, ans;
   int (*pM)(int x, int y);
   pM = max;
   printf("1번째 수치를 입력하세요. \n");
   scanf_s("%d",&num1);

   printf("2번째 수치를 입력하세요. \n");
   scanf_s("%d",&num2);

   ans = (*pM)(num1, num2);
   
   printf("최대값은 %d입니다. \n", ans);

   return 0;
}

/* max 함수의 정의 */
int max(int x, int y)
{
   if (x > y)
      return x;
   else 
      return y;
}
