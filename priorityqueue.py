from models import Packet

def key(pkt: Packet):
    # lower priority wins; tie → lower serial_no
    return (pkt.priority, pkt.serial_no)

class MinHeap:
    def __init__(self):
        self.a = []

    def push(self, pkt: Packet):
        a = self.a
        a.append(pkt)
        i = len(a) - 1
        while i > 0:
            p = (i - 1) // 2
            if key(a[p]) <= key(a[i]):
                break
            a[p], a[i] = a[i], a[p]
            i = p

    def pop(self) -> Packet:
        a = self.a
        if not a:
            raise IndexError("pop from empty heap")
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            i = 0
            n = len(a)
            # bubble down
            while True:
                l = 2*i + 1
                r = l + 1
                m = i
                if l < n and key(a[l]) < key(a[m]): m = l
                if r < n and key(a[r]) < key(a[m]): m = r
                if m == i: break
                a[i], a[m] = a[m], a[i]
                i = m
        return top
    
    def __bool__(self):
        return bool(self.a) 

'''
 # Testing this file   
from file_reader import reading_file
#from pqueue import MinHeap

packets = reading_file("list.txt")
heap = MinHeap()
for pkt in packets[:10]:        # seed window of 10
    heap.push(pkt)
i = 10
while heap:
    pkt = heap.pop()
    print(f"{pkt.serial_no},{pkt.priority}")
    if i < len(packets):        # keep filling from the rest
        heap.push(packets[i])
        i += 1
'''
