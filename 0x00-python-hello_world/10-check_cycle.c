#include "lists.h"

/**
 * check_cycle - the functions checks if a singly linked list
 * has a cycle
 * @list: The pointer to the list
 * Return: 0 (no cycle) or 1 (there is a cycle)
 */

int check_cycle(listint_t *list)
{
	if (list == NULL) /* if the list is empty, there is no cycle*/
		return (0);
	listint_t *ptr1 = list; /* initialize the first pointer
				   to the head of the list*/
	listint_t *ptr2 = list; /* initialize the second pointer
				   to the head of the list*/

	while (ptr1 && ptr2->next)
	{
		ptr1 = ptr1->next; /* move the 1st pointer one node at a time*/
		ptr2 = ptr2->next->next; /*move the 2nd pointer two nodes
					   at a time*/
		if (ptr1 == ptr2) /* if the two pointers meet, there is a cycle*/
			return (1);
	}
	return (0); /*no cycle is found*/
}
