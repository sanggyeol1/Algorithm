n, k = map(int, input().split())

dict = {}


for _ in range(n):
    address, password = input().split()
    dict[address] = password
    
for _ in range(k):
    site = input()
    print(dict[site])
    
    
