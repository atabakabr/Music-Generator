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

def next_rhythm(PreviousRhythm, rhythmsHistory, Time):
    NextRhythm = []
    if random.random() < 0.3: return PreviousRhythm
    else:
        action = random.choice(["simplify", "complicate", "randomize", "reuse"])
        if action == "simplify":
            NextRhythm = rhythm_simplification(PreviousRhythm)

        elif( action == "reuse" and len(rhythmsHistory) > 0):
            NextRhythm = random.choice(rhythmsHistory)

        elif action == "randomize":
            NextRhythm = rhythm_generator(Time)

        else :
            NextRhythm = rhythm_complication(PreviousRhythm)
    return NextRhythm

def rhythm_simplification(PreviousRhythm):
    Simplification_Rules = {(2.0, 2.0): [4.0],
        (1.0, 1.0): [2.0],
        (1.0, 0.5): [1.5],
        (0.5, 1.0): [2.0],
        (0.5, 0.5): [1.5],
        (1.5, 0.5): [2.0],
        (0.5, 1.5): [2.0],
    }
    for i in range(len(PreviousRhythm) - 1):
        if (PreviousRhythm[i] , PreviousRhythm[i+1]) in Simplification_Rules:
            split_notes = Simplification_Rules[PreviousRhythm[i], PreviousRhythm[i+1]]
            new_rhythm = PreviousRhythm[:i] + split_notes + PreviousRhythm[i + 2:]
            return new_rhythm
    return PreviousRhythm.copy()


def rhythm_complication(PreviousRhythm):
    Complication_Rules = {4.0 : [2.0, 2.0], 2.0 : [1.0, 1.0], 1.5 : [1.0, 0.5], 1.0 : [0.5, 0.5]}

    allowed_indices = [i for i, x in enumerate(PreviousRhythm) if x in Complication_Rules]
    if len(allowed_indices) == 0 : return PreviousRhythm
    target_index = random.choice(allowed_indices)
    split_notes = Complication_Rules[PreviousRhythm[target_index]]
    new_rhythm = PreviousRhythm[:target_index] + split_notes + PreviousRhythm[target_index + 1:]
    return new_rhythm


# ========== testcase ==========
print(rhythm_generator(4))  
print(rhythm_generator(3))  
print(rhythm_generator(6))  
print(rhythm_generator(12))
print(rhythm_generator(2))

