#ifndef LISTS_H
#define LISTS_H
<<<<<<< HEAD

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
=======
#include <stddef.h>

/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*
* Description: singly linked list node structure
* for ALX project
*/

typedef struct listint_s
{
    int n;
    struct listint_s *next;
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

<<<<<<< HEAD
void reverse_listint(listint_t **head);
=======
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
