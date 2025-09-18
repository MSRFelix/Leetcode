#include <math.h>
#include <stdio.h>

int g_total_count = 0;
int g_n = 10;
int g_arr[10];

int	valid_pos(int row, int column)
{
for (int i = 0; i < row; i++) {
        if (g_arr[i] == column ||                             // Same column
            abs(g_arr[i] - column) == abs(i - row)) {         // Same diagonal
            return 0;
        }
    }
    return 1;
}

void	find_sol(int row)
{
	int	column;

	column = 0;
	if (row == g_n)
	{
		g_total_count++;
		return ;
	}
	while (column < g_n)
	{
		if (valid_pos(row, column)  == 1)
		{
			g_arr[row] = column;
			find_sol(row + 1);
		}
		column++;
	}
}


	
int	main(void)
{
	find_sol(0);
	printf("%d\n", g_total_count); 
	return (g_total_count);
}


