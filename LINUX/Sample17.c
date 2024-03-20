#include <stdio.h>

/* 함수 선언 */
void show0(void);
void show1(void);
void show2(void);

int main(void)
{
   void (*pM[3])(void);
   int num;

   pM[0] = show0;
   pM[1] = show1;
   pM[2] = show2;

   printf("무엇을 호출할까요? (0:승용차 1:승합차 2:화물차) \n");
   scanf_s("%d",&num);

   if(0<= num && num <= 2)
      (*pM[num])();
   
   return 0;
}

/* 함수 정의 */
void show0(void)
{
    printf("승용차입니다. \n");
}
void show1(void)
{
    printf("승합차입니다. \n");
}
void show2(void)
{
    printf("화물차입니다. \n");
}
