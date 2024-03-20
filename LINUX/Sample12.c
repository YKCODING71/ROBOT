#include <stdio.h>
#include <string.h>

int main(void)
{
   char str1[10];
   char str2[10];

   strcpy_s(str1, 10, "Hello");
   strcpy_s(str2, 10, "Goodbye");

   printf("배열 str1는 %s입니다. \n", str1);
   printf("배열 str2는 %s입니다. \n", str2);

   return 0;
}
