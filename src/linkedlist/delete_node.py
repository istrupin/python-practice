from linkedlist.linked_list_node import LinkedListNode


def delete_node(node: LinkedListNode) -> None:
    node.value = node.next.value
    node.next = node.next.next
    return


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c

delete_node(b)

print(a.value)
print(a.next.value)