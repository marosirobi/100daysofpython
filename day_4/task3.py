states = ["Delaware","New York","Georgia","Maryland"]

print(states)
print(states[-1] +"\n") #last index states[-1] == states[3]

states.append("Alaska")

print(states)
print(states[-1] +"\n")

states.extend(["Angelaland", "Jack Bauer Land","Florida"])
print(states)

num_of_states = len(states)

print(num_of_states)

good_states = ["Florida","Hawaii"]

all_states = [states, good_states]

print(all_states[1])
