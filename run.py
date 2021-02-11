import psutil

# Cores print
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
print("")

# Freq print
cpu_freq = list(psutil.cpu_freq())
for count, i in enumerate(cpu_freq):
    i = i / 1000
    i = str(i)
    i = i[:3]
    if count == 0:
        print("Max Frequency: {}Ghz".format(i))
    if count == 1:
        print("Min Frequency: {}Ghz".format(i))
    if count == 2:
        print("Current Frequency: {}Ghz".format(i))

# Percent print
print("")
