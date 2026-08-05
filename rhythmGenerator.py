import random

def rhythm_generator(Time):
    AllowedTimeLaps = [0.5,1.0,1.5,2.0,4.0]
    GeneratedPattern = []
    total = 0.0
    counter = 0

    while(total < Time and counter < 1000):
        randomTime = random.choice(AllowedTimeLaps)
        if(randomTime + total < Time):
            GeneratedPattern.append(randomTime)
            total += randomTime

        elif(randomTime + total == Time):
            GeneratedPattern.append(randomTime)
            total += randomTime
            return GeneratedPattern
        else:
            continue
        counter += 1

    if total < Time:
        GeneratedPattern.append(Time - total)
    return GeneratedPattern

print(rhythm_generator(4))  
print(rhythm_generator(3))  
print(rhythm_generator(6))  
print(rhythm_generator(12))
print(rhythm_generator(2))  