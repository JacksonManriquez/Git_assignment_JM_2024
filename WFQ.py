from queue import Queue
# Input packets as a string, S=Stard, P=Priority, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
                 "E Sue"]

squeue = Queue(maxsize=10)
pqueue = Queue(maxsize=10)
equeue = Queue(maxsize=10)
for ind in input_packets:
    if ind[0] == "S":
        squeue.put(ind)
for ind in input_packets:
    if ind[0] == "P":
        pqueue.put(ind)
for ind in input_packets:
    if ind[0] == "E":
        equeue.put(ind)

while equeue.empty() is False:
    if pqueue.empty() is False:
        print(pqueue.get())
        print(pqueue.get())
        print(pqueue.get())
    if squeue.empty() is False:
        print(squeue.get())
        print(squeue.get())
    if equeue.empty() is False:
        print(equeue.get())
