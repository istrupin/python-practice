from linkedlist.linked_list_node import LinkedListNode


def has_cycle(head: LinkedListNode) -> bool:
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
    

cycle = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
cycle.next = b
b.next = c
c.next = b
print(has_cycle(cycle))

not_cycle = LinkedListNode(1)
d = LinkedListNode(2)
e = LinkedListNode(3)
not_cycle.next = d
d.next = e
print(has_cycle(not_cycle))

print(has_cycle(LinkedListNode(1)))