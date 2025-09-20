int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    #include <stdlib.h>
    #include <stdio.h>
    int i = 0;
    *returnSize = 2;
    int j;
    int *sol = (int*)malloc(2 * sizeof(int));
    while (i < numsSize -1)
    {
        j = i + 1;
        while (j < numsSize )
        {
            if (nums[i] + nums[j] == target)
            {
                sol[0] = i;
                sol[1] = j;
                return sol;
            }
            j++;
        }
        i++;
    }
    *returnSize = 0;
    return NULL;

// n² time complexity
