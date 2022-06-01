#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(listint *), *_head = *head;
	listint_t *prev = _head;
	
	if(newNode == NULL)
		return(NULL);
	newNode->n = number;
	if(_head == NULL)
	{
		newNode->next = _head, _head = newNode;
		return(newNode);
	}
	while(_head->next)
	{
		if(_head->n > number)
		{
			prev = _head;
			_head = _head->next;
		}
		else
		{
			break;
		}
	}
	if(_head->next)
	{
		newNode->next = _head;
	}
	prev->next = newNode;
}
