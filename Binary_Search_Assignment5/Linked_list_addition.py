class Node:
    def __init__(self,val):
        self.val  = val
        self.next = None

def insert(head,val):
    if head == None:
        head = Node(val)
    else:
        cur = head
        tmp = Node(val)
        while cur.next!= None:
            cur = cur.next
        cur.next= tmp
    return head

def sum_of_linked_list(l1,l2):
    carry =0
    prev = l1
    while l2!=None:
        l1.val = l1.val+l2.val+carry
        if l1.val > 9:
            carry = 1
            l1.val -= 10
        else:
            carry = 0
        prev = l1
        l1 = l1.next
        l2 = l2.next

    while l1!=None:
        l1.val = l1.val + carry
        if l1.val > 9:
            carry = 1
            l1.val -= 10
        else:
            carry = 0
        prev = l1
        l1 = l1.next
    if carry == 1:
        prev.next = Node(1)
    return l1

def print_linked_list(head):
    cur = head
    while cur!=None:
        print(cur.val,end= ' ')
        cur = cur.next
    print()
def main():
    n = int(input())
    m = int(input())
    l1 = None
    l2 = None

    for i in range(n):
        l1 = insert(l1,int(input()))
    for i in range(m):
        l2 = insert(l2,int(input()))

    print_linked_list(l1)
    print_linked_list(l2)
    if n>m:
        link_1 = l1
        link_2 = l2
    else:
        link_1 = l2
        link_2 = l1
    sum_of_linked_list(link_1,link_2)
    print_linked_list(link_1)
main()