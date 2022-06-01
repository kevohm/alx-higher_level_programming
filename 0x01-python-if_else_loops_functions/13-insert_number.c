#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current;
	listint_t *prev;
	if (*head == NULL)
		*head = newNode;
		return(NULL);
	newNode = malloc(sizeof(listint_t *));
	newNode->n = number;
	newNode->next = NULL;
	current = *head;
	while(current)
	{
		if(number > (current->n))
		{
			if(!current->next && current != *head)
			{
				current->next = newNode;
				return (newNode);
			}
			prev = current;
			current = current->next;
		}
		else
		{
			break;
		}
	}
	if(prev->next)
	{
		prev->next = newNode;
	}
	else
	{
		*head = newNode;
	}
	newNode->next = current;
	return newNode;
}
