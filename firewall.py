from file_reader import reading_file
from sorting import sort_batch
from priorityqueue import MinHeap

def emit_with_insertion_sort(filename: str, batch_size: int = 10) -> None:
    packets = reading_file(filename)
    for i in range(0, len(packets), batch_size):
        batch = packets[i:i + batch_size]
        sort_batch(batch)
        for pkt in batch:
            print(f"{pkt.serial_no},{pkt.priority}")

def emit_with_priority_queue(filename: str, window_size: int = 10) -> None:
    packets = reading_file(filename)

    it = iter(packets)
    heap = MinHeap()

    # seed up to window_size items
    for _ in range(window_size):
        try:
            heap.push(next(it))      
        except StopIteration:
            break

    # emit + refill
    while heap:
        pkt = heap.pop()            
        print(f"{pkt.serial_no},{pkt.priority}")
        try:
            heap.push(next(it))     
        except StopIteration:
            pass