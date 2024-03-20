#include <stdio.h>
#include <stdlib.h>

int main(void)
{
   char *str;
   int num, i;

   printf("몇 문자의 a를 준비할까요? \n");
   scanf_s("%d", &num);

   str = (char *) malloc (sizeof(char) * (num+1));
   if(!str){
      printf("메모리를 확보할 수 없었습니다. \n");
      return 1;
   }

   for(i=0; i<num; i++){
      *(str+i) = 'a';
   }
   *(str+num) = '\0';

   printf("%s을 준비했습니다. \n", str);

   free(str);

   return 0;
}
