#include <stdio.h>
#include <math.h>

int	g_total_count;

int		check_comb(int row, int column, int g_n, int g_arr[]);
void	find_comb(int column, int g_n, int g_arr[]);

void	find_comb(int column, int g_n, int g_arr[])
{
	int	row;

	row = 0;
	if (column == g_n)
	{
		g_total_count++;
		return ;
	}
	while (row < g_n)
	{
		if (check_comb(row, column, g_n, g_arr) == 1)
		{
			g_arr[column] = row;
			find_comb(column + 1, g_n, g_arr);
		}
		row++;
	}
}

int	check_comb(int row, int column, int g_n, int g_arr[])
{
int	i;

	i = 0;
	while (i < column)
	{
        	if (g_arr[i] == row || g_arr[i] - i == row - column || g_arr[i] + i == row + column)
			return 0;
		i++;
    	}
	return 1;
}

int	main(int argc, char *argv[])
{
	int	n;
	int	g_arr[n];

	if (argc > 1)
	{
		if (*argv[1] >= '0' && *argv[1] <= 60)
			n = *argv[1] - 48;
		else
			n = 4;
	}
	else
		n = 4;
	find_comb(0, n, g_arr);
	printf("%d\n", g_total_count);
	return (0);
}
