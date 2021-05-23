fishes = [
    [10,-1],[11,-1],[8,1],[5,1],[3,1],[4,-1],[6,-1],[9,-1],[2,-1],[1,-1],[8,1]
]

def isStackEmpty(stack):
    if stack: return False
    return True

def eatFish(fishes):
    stack = []
    for fish in fishes:
        if isStackEmpty(stack): stack.append(fish)
        elif stack[-1][1]==1 and fish[1]==-1:
            if abs(stack[-1][0])>abs(fish[0]):
                continue
            else:
                currentFish = fish
                while not isStackEmpty(stack) and stack[-1][1]!=1 and currentFish[1]!=-1:
                    topFish = stack.pop()
                    if abs(topFish[0])>abs(currentFish[0]):
                        currentFish = topFish
                stack.append(currentFish)
        else:
            stack.append(fish)
    return stack

print(eatFish(fishes))