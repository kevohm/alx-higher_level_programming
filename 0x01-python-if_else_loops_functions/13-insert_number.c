#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current;
	listint_t *prev = NULL;
	if (head == NULL)
		return(NULL);
	newNode = malloc(sizeof(listint_t *));
	newNode->n = number;
	current = *head;
	while(current != NULL)
	{
		if(number > (current->n))
		{
			prev = current;
			current = current->next;
		}
		else
		{
			break;
		}
	}
	if(prev == NULL)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else if(current == NULL)
	{
		prev->next = newNode;
	}
	else
	{
		newNode->next = current;
		prev->next = newNode;
	}
	return newNode;
}
