#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current;
	if (head == NULL)
		return(NULL);
	newNode = malloc(sizeof(listint_t *));
	newNode->n = number;
	newNode->next = NULL;
	current = *head;
	while(current)
	{
		if(number > (current->n))
		{
			if(current->next == NULL)
			{
				current->next = newNode;
			}
			*head = current;
			current = current->next;
		}
		else
		{
			break;
		}
	}
	(*head)->next = newNode;
	newNode->next = current;
	return newNode;
}
