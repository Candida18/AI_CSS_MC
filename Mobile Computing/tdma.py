slots = []
delay = []
ts1 = 0
ts2 = 417
for i in range(10):
    d = input("Enter the delay for channel "+str(i+1)+": ")
    delay.append(int(d))

for i in range(10):
    if(delay[i]<10):
        slots.append(1)
    else:
        slots.append(0)

print("\nCycle 1")
for i in range(10):
    if(slots[i] == 1):
        print("Channel "+str(i+1)+" has been assigned slot "+str(ts1)+" to "+str(ts2))
        ts1 = ts2 + 1
        ts2 = ts1 + 417
    else:
        print("Channel "+str(i+1)+" has not been assigned any slot")

ts1 = 0
ts2 = 417
print("\nCycle 2")
for i in range(10):
    if(slots[i] == 0):
        print("Channel "+str(i+1)+" has been assigned slot "+str(ts1)+" to "+str(ts2))
    else:
        print("Time slot "+str(ts1)+" to "+str(ts2)+": Idle")
    ts1 = ts2 + 1
    ts2 = ts1 + 417
