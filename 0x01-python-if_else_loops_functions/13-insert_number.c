#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - Inserts number into sorted singly-linked list.
 * @head: pointer the head of linked list.
 * @number: number to insert.
 *
 * Return: If function fails - NULL, Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));

if (new_node == NULL)
{
return (NULL);
}
new_node->data = number;
new_node->next = NULL;

if (*head == NULL || number < (*head)->data)
{
new_node->next = *head;
*head = new_node;
}
else
{
listint_t *current = *head;
while (current->next != NULL && number > current->next->data)
{
current = current->next;
}
new_node->next = current->next;
current->next = new_node;
}
return (new_node);
}
