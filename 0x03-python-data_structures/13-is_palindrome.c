#include "lists.h"

/**
 * is_palindrome - chexk if a list is palindrome
 * @list: pointer to list
 * Return: 1 if true 0 otherwise
 */
int is_palindrome(listint_t **list)
{
	int len, i = 0;
	listint_t **reversed, h1, h2;

	if (!list)
		return (0);
	reversed = reverse_listint(list);
	return (1);
}

/**
 * reverse_listint - reverses a linked list
 * @h: head of the list
 *
 * Return: pointer to the reversed
 */
listint_t *reverse_listint(listint_t **h)
{
	listint_t *tmp2, *tmp1;

	if (!h || !(*h))
		return (NULL);
	tmp1 = (*h)->next;
	(*h)->next = NULL;
	while (tmp1)
	{
		tmp2 = *h;
		*h = tmp1;
		tmp1 = (*h)->next;
		(*h)->next = tmp2;
	}
	return (*h);
}
