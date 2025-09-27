import argparse
from firewall import emit_with_insertion_sort, emit_with_priority_queue

def main():
    ap = argparse.ArgumentParser(description="Mini firewall: insertion sort or priority queue.")
    ap.add_argument("file", help="Input CSV/TXT path")
    ap.add_argument("--impl", choices=["insert", "pq"], default="insert",
                    help="Algorithm: insertion sort ('insert') or priority queue ('pq')")
    ap.add_argument("--size", type=int, default=10,
                    help="Batch/window size (default: 10)")
    args = ap.parse_args()

    if args.impl == "insert":
        emit_with_insertion_sort(args.file, batch_size=args.size)
    else:
        emit_with_priority_queue(args.file, window_size=args.size)

if __name__ == "__main__":
    main()
