from linkedlist.linked_list_node import LinkedListNode


def k_from_last(head: LinkedListNode, k: int) -> LinkedListNode:
    beg = head
    end = head
    for i in range(k):
        end = end.next
        check_for_none(end)
    while end.next:
        beg = beg.next
        end = end.next
    return beg


def check_for_none(node):
    if not node:
        raise ValueError("list is shorter than k")


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
a.next = b
b.next = c

print(k_from_last(a, 1).value)
print(k_from_last(a, 0).value)
print(k_from_last(a, 2).value)
print(k_from_last(a, 3).value)