def partition_no_ones(n, min_val=2):
    if n == 0:
        return [[]]

    partitions = []
    for i in range(min_val, n + 1):
        for p in partition_no_ones(n - i, i):
            if all(x >= 2 for x in [i] + p):  # Ensure no 1 in the partition
                partitions.append([i] + p)

    return partitions

n = 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorialn = factorial(n)

partitions = []
for i in range(2,n+1):
    partitions.append(partition_no_ones(i))

val2 = 0
for x in partitions:
    for y in x:
        z = factorialn
        val = 0
        for a in y:
            z = z*(a-1)
            val = val + a
            z = z/factorial(a)
        z = z * (val + len(y))
        val2 += z
print(val2)
