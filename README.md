# Mini Firewall (Priority Packet Scheduler)

As a part of Week-3 Assignment for the Coding Bootcamp by Cybersecurity Professionalys led by Karan Dwivedi sir

Design a tiny “firewall” that **filters and forwards packets in priority order**.  
Each packet has:
- a **serial number** (`1, 2, 3, …`)
- a **priority** (`1`–`10`), where **1 is the highest** and **10 is the lowest**.

The firewall **processes up to 10 packets at a time** (default window size = 10).  
When deciding which packet to output next, it **always chooses**:
1. the packet with the **highest priority** (i.e., *lowest priority number*), then  
2. if priorities tie, the packet with the **lowest serial number**.

**Ordering key:** `(priority ASC, serial ASC)`.

---

## Problem Rules

- Packets arrive as pairs: `SerialNo,Priority`.
- Valid priorities are integers in **[1, 10]**; serials are positive integers starting at **1**.
- Within each 10-packet window, output packets sorted by **priority first**, then **serial**.
- Implementation modes:
  - **Batch:** read all input, sort by `(priority, serial)`, output all.
  - **Streaming/windowed:** read chunks of 10, output those in order, then the next 10.

> If your assignment specifies one interpretation, follow that; both are common variants.

---

## Input Format

A text/CSV file with one packet per line:

**Example input (header optional):**
```csv
1,5
2,3
3,1
4,3
5,7
6,10
9,5
10,1
```

## Output Format

Print the packets **in the order they would be forwarded**, as `SerialNo,Priority`, one per line.

**Example output for the input above:**
``` csv
3,1
10,1
2,3
4,3
1,5
9,5
5,7
6,10
```

(Explanation: priority `1` first → serials `3,10`; then priority `3` → serials `2,4`; etc.)
---

---

## Implementations Used

1) **Insertion Sort (manual, stable)**  
   - Sort each batch/window by `(priority, serial_no)` using in-place insertion sort.

2) **Priority Queue (manual min-heap)**  
   - Keep a window of up to `K` packets in a min-heap keyed by `(priority, serial_no)`; repeatedly pop the best and push the next from input.

---

## Repository Structure

- models.py # Minimal Packet class (serial_no, priority)
- file_reader.py # read_packets(): parse CSV/TXT, skip optional header, allow # comments
- sorting.py # sort_batch(): manual insertion sort (stable); sort_batch_builtin() optional
- priorityqueue.py # MinHeap: push(pkt), pop() — compares by (priority, serial_no)
- firewall.py # Orchestration: emit_with_insertion_sort(), emit_with_priority_queue()
- main.py # CLI entrypoint: choose algorithm and batch/window size


**File purposes**
- **models.py** — Defines `Packet` (simple class).
- **reader.py** — Robust line parsing (`1,5` or `1 5`), optional header, ignores blanks/`#`.
- **sorter.py** — Manual insertion sort that is stable with the required key.
- **pqueue.py** — Minimal binary heap used as a priority queue.
- **firewall.py** — Wiring to read → batch/window → sort/schedule → print.
- **main.py** — Command-line interface.

---

## How to Run

> Requires Python 3.8+.

### Insertion sort (batch/window)
```bash
python main.py <path-to-file> --impl insert --size 10
```

### Priority queue (windowed scheduling)
```bash
python main.py <path-to-file> --impl pq --size 10
```

### Input Format

- One packet per line: either serial,priority or serial priority.
- Optional single header line is allowed (e.g., Serial,Priority).
- Lines starting with # and blank lines are ignored.
- Constraints: serial_no >= 1, priority ∈ [1..10].

---

## Constraints & Assumptions

- Window size **K = 10** by default for implementation (configurable is OK).
- Inputs are well-formed integers for core tests.

---

## What to Build

- **Parser** for the input file.
- **Ordering logic** implementing: priority asc, then serial asc.
- **Emitter** printing `SerialNo,Priority` per line.
