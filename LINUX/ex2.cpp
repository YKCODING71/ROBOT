#include <stdio.h>

int main(void)
{
   int test[5] = {80,60,55,22,75};

   printf("test[0] data =  %d. \n", test[0]);
   printf("test[0] address = %p. \n", &test[0]);
   printf("test[1] data =  %d. \n", test[1]);
   printf("test[1] address = %p. \n", &test[1]);

   return 0;
}
