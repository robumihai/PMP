import random

def simulate(simulations=100000):
    red_count = 0
    colors = ['red', 'blue', 'black']

    for _ in range(simulations):
        # red,blue,black
        urn = [3, 4, 2]

        die = random.randint(1, 6)
        if die in [2, 3, 5]:  
            urn[2] += 1       # adauga bila neagra
        elif die == 6:
            urn[0] += 1       # adauga bila rosie
        else:  # 1 sau 4
            urn[1] += 1       # adauga bila albastra

        drawn = random.choices(range(len(colors)), weights=urn, k=1)[0]
        drawn_color = colors[drawn]
        
        if drawn_color == 'red':
            red_count += 1

    return red_count / simulations


prob = simulate()

print(f"Estimated probability: {prob}")