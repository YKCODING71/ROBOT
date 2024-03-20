#include <stdio.h>

int main(void)
{
   int test[5] = {80,60,55,22,75};

   printf("test[0]의 값은 %d입니다. \n", test[0]);
   printf("test[0]의 어드레스는 %p입니다. \n", &test[0]);
   printf("test[1]의 값은 %d입니다. \n", test[1]);
   printf("test[1]의 어드레스는 %p입니다. \n", &test[1]);

   return 0;
}
