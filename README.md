# Mini Firewall (Priority Packet Scheduler)

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
10,1```

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
6,10```


(Explanation: priority `1` first → serials `3,10`; then priority `3` → serials `2,4`; etc.)

---

## Constraints & Assumptions

- Window size **K = 10** by default for implementation (configurable is OK).
- Inputs are well-formed integers for core tests.

---

## What to Build

- **Parser** for the input file.
- **Ordering logic** implementing: priority asc, then serial asc.
- **Emitter** printing `SerialNo,Priority` per line.
