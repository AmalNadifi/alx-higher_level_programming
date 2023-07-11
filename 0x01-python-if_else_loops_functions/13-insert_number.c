#include "lists.h"

/**
 * insert_node - the function inserts the provided number
 * into the sorted singly linked list.
 * @head: Double pointer to the linked list head
 * @number: the provided number to insert
 * Return: a pointer to the new node (success) or Null(failure)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	/*Allocate memory for the new node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	/*Handle case of empty list or number smaller than 1st element*/
	if (current == NULL || (current->n) >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	/*Traverse the list to find correct position to insert the new node*/
	while (current && current->next && current->next->n < number)
	{
		current = current->next;
	}
	/*Insert the new node in the correct position*/
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
