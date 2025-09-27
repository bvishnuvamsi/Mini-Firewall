from models import Packet

def split_fields(line:str):
    line = line.strip()
    if not line or line.startswith("#"): # for blank or comment lines
        return None
    
    if "," in line :
        raw_parts = line.split(",")
    else:
        raw_parts = line.split()

    parts = []
    for p in raw_parts:
        p = p.strip()
        if p != "":
            parts.append(p)

    return parts    


def reading_file(filename, batch_size = 10):
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            all_packets = []
            header_skipped = False

            for ln, raw in enumerate(file,1):
                fields = split_fields(raw)
                if fields is None:
                    continue
                    
                if len(fields) !=2 : # we need only two numbers
                    if not header_skipped:
                        header_skipped = True
                        continue
                    print(f"Skipping invalid line {ln}: '{line}'. Non-integer values.")
                    continue

                try:
                    s = int(fields[0]) # we need integers
                    p = int(fields[1])
                except ValueError:
                    if not header_skipped:
                        header_skipped = True
                        continue
                    print(f"Skipping invalid line {ln}: '{raw.rstrip()}' (non-integer).")
                    continue

                if s < 1 or not (1 <= p <= 10): # Check the range of packets
                    print("Out of Range")
                    continue

                all_packets.append(Packet(s,p))
 #               for pkt in batch:
 #                   print(f"{pkt.serial_no},{pkt.priority}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return all_packets
'''
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python reader.py <file.csv|file.txt>")
        raise SystemExit(2)

    for pkt in reading_file(sys.argv[1]):
        print(f"{pkt.serial_no},{pkt.priority}")
'''