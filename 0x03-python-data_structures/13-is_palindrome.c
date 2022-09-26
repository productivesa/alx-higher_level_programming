#include "lists.h"
/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the start node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
void reverse(listint_t **head)
{
	listint_t *prv;
	listint_t *crr;
	listint_t *nxt;

	prv = NULL;
	crr = *head;

	while (crr != NULL)
	{
		nxt = crr->next;
		crr->next = prv;
		prv = crr;
		crr = nxt;
	}

	*head = prv;
}
/**
 * compare - compares each int of the list
 * @head1: head of the first half
 * @head2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *head1, listint_t *head2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = head1;
	tmp2 = head2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}
/**
 * is_palindrome - This checks if a singly-linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: If the linked list is not a palindrome - 0 else -1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
