# Within range of 0 up to and including stop value

def halves(stop, step):
    start = 0
    while start <= stop:
        yield float(start)
        start += step

print(list(halves(10, 0.5)))

# Infinite range from 0
def halves(step):
    start = 0
    while True:
        yield float(start)
        start += step

for x in halves(0.5):
    print(x)
