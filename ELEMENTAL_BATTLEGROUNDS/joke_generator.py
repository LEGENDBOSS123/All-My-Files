import random

jokes = []
def make_joke(j,a):
    if j and a:
        jokes.append([j,a])
    
make_joke("Why did the chicken cross the road?","To get to the other side.")
make_joke("Why was 6 afraid of 7?","Because 7 8 9.")
make_joke("Why was the easter bunny so afraid?","He was having a bad hare day.")
make_joke("Should I tell you a joke about pizza?","Nevermind, its too cheesy.")
make_joke("Why did the children eat their homework?","Their teacher told them it was a piece of cake.")
make_joke("What did the fish say when he swam into a wall?","Dam.")
make_joke("What do you call a fish with no eyes?","A fsh.")
make_joke("What do you call a can opener that doesn’t work?","A can't opener.")
make_joke("Why did two 4's skip dinner?","Because they already 8.")
make_joke("Why can't you tell a joke to an egg?","It might crack up.")
make_joke("What do you call a sad strawberry?","A blueberry.")
make_joke("Why did a scarecrow win a Nobel prize?","He was outstanding in his field.")
make_joke("Why did the kid throw his clock out the window?","He wanted to see time fly.")
make_joke("Why are fish so smart?","Because they live in schools.")
make_joke("What do you call cheese that's not yours?","Nacho cheese.")
make_joke("What did one eye say to the other eye?","Between us, something smells.")


def generate_joke():
    j = random.choice(jokes)
    a = random.choice(jokes)
    while a == j:
        a = random.choice(jokes)
    j = j[0]
    a = a[1]
    return [j,a]
