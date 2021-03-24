import psutil

# Cores print
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
print("")

# Freq print
cpu_freq = list(psutil.cpu_freq())
for count, item in enumerate(cpu_freq):
    item = str(item / 1000)[:3]
    if count == 0:
        print("Max Frequency: {}Ghz".format(item))
    if count == 1:
        print("Min Frequency: {}Ghz".format(item))
    if count == 2:
        print("Current Frequency: {}Ghz".format(item))

# Percent print
print("")

while True:
    cpu_percent = list(psutil.cpu_percent(interval=1, percpu=True))

    for count, x in enumerate(cpu_percent):
        # ! Problem with updating percent correct
        print("CPU {}:   {}%".format(count, x), end="\r")

    print("")
