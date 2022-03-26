class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

    def add(self, list_node):
        if not isinstance(list_node, ListNode):
            list_node = ListNode(list_node)
        node = self
        while (next_ := node.next) is not None:
            node = next_
        node.next = list_node
        return self

    def remove(self):
        node = self
        while (next_ := node.next).next is not None:
            node = next_
        node.next = None
        return self


l = ListNode(1).add(2).add(3).add(4).add(5)


def reverse_linked_list(node):
    if node.next is None:
        return node
    curr_node = node
    prev_node = None

    while curr_node.next is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    curr_node.next = prev_node

    return curr_node


reverse_linked_list(l)
