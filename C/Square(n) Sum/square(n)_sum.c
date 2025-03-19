#include <stdio.h>
#include <math.h>

int square_sum(const int values[], size_t count)
{
  int sum = 0;
  for (int i = 0; i < count; i++)
    {
    sum += pow(values[i], 2);
  }
	return sum;
}
