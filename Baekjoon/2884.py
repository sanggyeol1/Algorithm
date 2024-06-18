H, M = input().split()

if(int(M) >= 45):
    nh = int(H)
    nm = int(M) - 45
else:
    nh = (int(H)+24 - 1)%24
    nm = (int(M)+60 - 45)%60

print(nh, nm)