# Part 1
list1 = []
list2 = []

with open('input.txt', 'r') as text:
    for line in text:
        parts = line.split(maxsplit=1)
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

list1.sort()
list2.sort()

distances = []

for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    distances.append(diff)


total_distance = sum(distances)
print(f"Part 1 solution: {total_distance}")

# Part 2
sim_scores = []

for i in range(len(list1)):
    score = list1[i] * list2.count(list1[i])
    sim_scores.append(score)

total_sim_score = sum(sim_scores)
print(f"Part 2 solution: {total_sim_score}")
