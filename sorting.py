from models import Packet

def sort_batch(batch): #In-place stable sort using insertion sort.
    for i in range(1, len(batch)):
        x = batch[i]
        j = i - 1
        while j >= 0 and (batch[j].priority, batch[j].serial_no) > (x.priority, x.serial_no):
            batch[j + 1] = batch[j]
            j -= 1
        batch[j + 1] = x
    return batch

'''
#  self-test (run: python sorter.py)
if __name__ == "__main__":
    sample = [Packet(1,5), Packet(2,3), Packet(3,1), Packet(10,1)]
    print("Before:", [f"{p.serial_no},{p.priority}" for p in sample])
    sort_batch(sample)  # or: sort_batch_builtin(sample)
    print("After: ", [f"{p.serial_no},{p.priority}" for p in sample])
'''