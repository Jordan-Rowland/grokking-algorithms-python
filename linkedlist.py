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


l = ListNode(1).add(2).add(5).add(11).remove()
