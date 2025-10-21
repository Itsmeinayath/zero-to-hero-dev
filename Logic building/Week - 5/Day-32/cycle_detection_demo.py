class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def attach_cycle(head, pos):
    """Attach tail to node at 0-based index `pos`. Pass -1 for no cycle."""
    if pos < 0 or not head:
        return head
    tail = head
    idx = 0
    join = None
    while tail.next:
        if idx == pos:
            join = tail
        tail = tail.next
        idx += 1
    if idx == pos:
        join = tail
    if join:
        tail.next = join
    return head


def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detect_cycle_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


def main():
    # Example 1: cycle at index 1 (value 2)
    h = make_list([3, 2, 0, -4])
    attach_cycle(h, 1)
    print("Has cycle?", has_cycle(h))  # True
    start = detect_cycle_start(h)
    print("Cycle starts at:", start.val if start else None)  # 2

    # Example 2: no cycle
    h2 = make_list([1, 2])
    print("Has cycle?", has_cycle(h2))  # False
    print("Cycle starts at:", detect_cycle_start(h2))  # None


if __name__ == "__main__":
    main()
