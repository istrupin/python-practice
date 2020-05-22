from linkedlist.linked_list_node import LinkedListNode


def reverse(head: LinkedListNode) -> None:
    if not head.next:
        return head
    prev = None
    current = head
    next = current.next

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c

reverse(a)
print(c.next.value)
print(b.next.value)
print(a.next)

