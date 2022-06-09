#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @listint_t: node structure
 * @lists: singly linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node;

	/* an empty linked list is circular */
	if (list == NULL)
	{
	return (1);
	}

	/* next of head */
	node = list->next;

	/* This loop will stop in both cases */
	/* (1) if circular (2) not circular */
	while (node != NULL && node != list)
	node = node->next;

	/* if loop stop because of circular condition */
	return (node == list);

}
