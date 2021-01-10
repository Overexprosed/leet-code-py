"""
Remove Duplicates from Sorted List

Given the head of a sorted linked list.
Delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Do all job against auxiliary variable ('cur').
It will affect all internal variables (we work with the list).
Initial variable ('head') save its first link,
but inner links will be changed (if needed).
"""


def delete_duplicates(head):
    cur = head
    while cur:
        if cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
