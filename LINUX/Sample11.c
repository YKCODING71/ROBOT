#include <stdio.h>
#include <string.h>

int main(void)
{
   char str[100];

   printf("문자열(영문숫자)을 입력하세요. \n");

   scanf_s("%s", str, 100);

   printf("문자열 길이는 %d입니다. \n", strlen(str));

   return 0;
}
