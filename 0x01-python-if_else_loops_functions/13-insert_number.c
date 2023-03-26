#include "lists.h"

/**
<<<<<<< HEAD
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
=======
* insert_node - Inserts a number into a sorted singly-linked list.
* @head: A pointer the head of the linked list.
* @number: The number to insert.
* Author - Gabriel Dan alias Zeus
* Return: If the function fails - NULL.
*         Otherwise - a pointer to the new node.
*/

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
