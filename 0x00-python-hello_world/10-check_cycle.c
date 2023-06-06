/*
 * Filename: 10-check_cycle.c
 * Author: Talent C Gwizhi
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if singly-linked list contains a cycle.
 * @list: singly-linked list.
 *
 * Return: If there is no cycle - 0. Otherwise - 1.
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list, *fast = list;

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1);
}

return (0);
}
