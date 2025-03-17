#include <stdbool.h>

bool narcissistic(int num)
{
  int digits = 0;
  int n = num;
  int m = num;
  int sum = 0;
  
  while (n > 0)
    {
      n = n / 10;
      digits++;
    }
  
  for (int i = 0; i < digits; i++)
    {
      sum += pow((m % 10), digits);
      m = m / 10;
    }
  if (num == sum)
    {
      return true;
    }
  else
    {
      return false;
    } 
}
