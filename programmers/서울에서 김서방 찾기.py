def solution(seoul):
    location = 0
    
    for i in seoul:
        if i == "Kim":
            break
        location+=1
    return (f"김서방은 {location}에 있다")