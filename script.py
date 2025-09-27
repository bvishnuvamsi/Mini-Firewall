from dataclasses import dataclass

@dataclass
class Packet:
    serial_no: int
    priority: int

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

def sort_batch(a):
    return a

def reading_file(filename, batch_size = 10):
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            all_packets = []
            header_skipped = False

            for ln, raw in enumerate(file,1):
                fields = split_fields(raw)
                if fields is None:
                    continue
                    
                if len(parts) !=2 :
                    if not header_skipped:
                        header_skipped = True
                        continue
                    print(f"Skipping invalid line {ln}: '{line}'. Non-integer values.")
                    continue

                try:
                    s = int(fields[0])
                    p = int(fields[1])
                except ValueError:
                    if not header_skipped:
                        header_skipped = True
                        continue
                    print(f"Skipping invalid line {ln}: '{raw.rstrip()}' (non-integer).")
                    continue


                all_packets.append(Packets(s,p))
                for pkt in batch:
                    print(f"{pkt.serial_no},{pkt.priority}")

            for i in range(0, len(all_packets), batch_size):
                batch = all_packets[i:i+batch_size]
                sort_batch(batch)
                for pkt in batch:
                    print(f"{pkt.serial_no},{pkt.priority}")


    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
