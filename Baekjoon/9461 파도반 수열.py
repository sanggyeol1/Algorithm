t = int(input())



for _ in range(t):
    wave_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    index = int(input())
    
    if index <= 10:
        print(wave_list[index-1])
    else:
        for i in range(10, index):
            wave_list.append(wave_list[i-1]+ wave_list[i-5])

        print(wave_list[index-1])
    
