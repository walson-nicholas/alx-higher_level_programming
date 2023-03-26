#include "lists.h"
<<<<<<< HEAD

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
=======
#include <stdlib.h>
#include <stdio.h>

/**
* is_palindrome - check is a linked list is palindrome
* @head: head of the list
* Return: 0 if not 1 if it is
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *prev, *next, *left_head, *right_head;
	int list_len = 0, i = 0, not_p = 0;

	if (*head == NULL || head == NULL)
		return (1);
	while (current != NULL)
		list_len++, current = current->next;
	if (list_len == 1)
		return (1);
	current = *head;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		else
			current->next = NULL;
		prev = current, current = next;
	}
	right_head = current, left_head = prev;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		if (list_len % 2 != 0 && i == 1)
			current = current->next;
		if (current->n != prev->n)
		{
			not_p = 1;
			break;
		}
		current = current->next, prev = prev->next;
	}
	current = left_head, prev = right_head;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		prev = current, current = next;
	}
	return (not_p == 1 ? 0 : 1);
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
}
