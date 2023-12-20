import random

N, M = 1000, 30
c = [random.randint(50, 100) for i in range(M)]
d = [random.randint(min(c), max(c)) for i in range(N)]
k = 200000
conf = []
pairs = []

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        pairs.append([i, j])

for i in range(k):
    picked = random.choice(pairs)
    conf.append(picked)
    pairs.remove(picked)

# Writing data to a file
with open("data.txt", "w") as file:
    file.write(f"{N} {M}\n")
    file.write(" ".join(map(str, d)) + "\n")
    file.write(" ".join(map(str, c)) + "\n")
    file.write(f"{k}\n")
    
    for i in conf:
        file.write(" ".join(map(str, i)) + "\n")

print("Data written to data.txt")
