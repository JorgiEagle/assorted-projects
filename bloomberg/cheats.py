from itertools import product
# Enter your code here. Read input from STDIN. Print output to STDOUT
k, m = map(int, input().split())
N = []
for _ in range(k):
    N.append([n**2 for n in list(map(int, input().split()))[1:]])
big_product = N[0]
for i in range(1, len(N)):
    big_product = [sum(entry) for entry in product(big_product, N[i])]
mod_product = [entry % m for entry in big_product]
print(max(mod_product))
