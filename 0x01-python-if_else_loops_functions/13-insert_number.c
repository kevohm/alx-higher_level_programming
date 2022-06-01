#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	if (head == NULL)
		return(NULL);
	listint_t *newNode = malloc(sizeof(listint_t *));
	newNode->n = number;
	newNode->next = *head;
	*head = newNode;
	return newNode;
}
