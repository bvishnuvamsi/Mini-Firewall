class Packet:
    def __init__(self, serial_no, priority):
        self.serial_no = serial_no
        self.priority = priority

def packet_key(pkt):  # ordering: priority ASC, then serial ASC
    return (pkt.priority, pkt.serial_no)

## Testing

#pkt = Packet(3, 1)
#print(pkt.serial_no, pkt.priority)        # 3 1
