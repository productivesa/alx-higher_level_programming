#include "lists.h"
/**
 * check_cycle  - checks singly linked list has cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle
 * 1 if there's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *po;
	listint_t *prev;

	po = list;
	prev = list;
	while (list && po && po->next)
	{
		list = list->next;
		po = po->next->next;

		if (list == po)
		{
			list = prev;
			prev = po;
			while (1)
			{
				po = prev;
				while (po->next != list && po->next != prev)
				{
					po = po->next;
				}
				if (po->next == list)
					break;

				list = list-> next;
			}
			return(1);
		}
	}
	return(0);
}
