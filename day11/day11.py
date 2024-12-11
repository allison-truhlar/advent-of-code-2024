def get_list_from_line():
    with open("input.txt", "r") as file:
        for line in file:
            input_list = line.strip().split(" ")
        return input_list
        
stones = get_list_from_line()

def remove_extra_zeros(string):
    if string.count("0") == len(string):
        return "0"
    else:
        return string.lstrip("0")

for i in range(1,76):
    print(f"blink: {i}")
    new_stones=[]
    for stone in stones:
        # print("running...")
        # print(f"curr index: {curr_ind}")
        # print(f"current stones: {stones}")
        if int(stone) == 0:
            # print("replace with 1")
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            # print("split")
            firstpart, secondpart = stone[:len(stone)//2], stone[len(stone)//2:]
            new_stones.append(remove_extra_zeros(firstpart))
            new_stones.append(remove_extra_zeros(secondpart))
        else:
            # print("mult by 2024")
            num = int(stone) * 2024
            new_stones.append(str(num))
    stones = new_stones
    # print(f"blink = {i}")
    # print(f"resulting stones = {stones}")


# print(stones)
print(len(stones))