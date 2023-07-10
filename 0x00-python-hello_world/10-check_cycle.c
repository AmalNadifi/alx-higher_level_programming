#include "lists.h"

/**
 * check_cycle - the functions checks if a singly linked list
 * has a cycle
 * @list: The pointer to the list
 * Return: 0 (no cycle) or 1 (there is a cycle)
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;

	if (list == NULL) /* if the list is empty, there is no cycle*/
                return (0);
	ptr1 = list; /* initialize 1st pointer to the list head*/
	ptr2 = list; /* initialize 2nd pointer to list head*/
	while (ptr1 && ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next; /* move the 1st pointer one node at a time*/
		ptr2 = ptr2->next->next; /*move 2nd pointer 2nodes each time*/
		if (ptr1 == ptr2) /* if the two pointers meet, there is a cycle*/
			return (1);
	}
	return (0); /*no cycle is found*/
}
