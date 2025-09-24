/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode  dummy;
    struct ListNode *sol = &dummy;
    while (list1 != 0 && list2 != 0)
    {
        if ((*list1).val > (*list2).val)
        {
            (*sol).next = list2;
            list2 = (*list2).next;
        }
        else
        {
            (*sol).next = list1;
            list1 = (*list1).next;
        }
        sol = (*sol).next;
    }
    if (list1 != 0)
    {
        while (list2 != 0)
        {
            (*sol).next = list2;
            list2 = (*list2).next; 
            sol = (*sol).next;

        }
    }
    else
        while (list1 != 0)
        {
            (*sol).next = list1;
            list1 = (*list1).next;
            sol = (*sol).next;

        }
    if (list1 != 0)
        (*sol).next = list1;
    else
        (*sol).next = list2; 
    return (dummy.next);
}

// Merge two sorted lists in ascending order
