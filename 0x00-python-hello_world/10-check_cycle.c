#include "lists.h"

/**
 * find_listint_loop - finds the index at which a loop starts
 * @head: list head
 *
 * Description: mdldndkdbfkml
 * Return: pointer to loop start
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = head, *slow = head;

	if (!head || !(head->next))
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
