# Part 1
safe_diffs = [1, 2, 3]
safe_lists = []

with open('input.txt', 'r') as text:
    for line in text:
        orginal_num_arr = line.split()
        safe_dampened_lists = []

        for i in range(len(orginal_num_arr)):
            numArr = orginal_num_arr.copy()
            numArr.pop(i)

            # Evaluate numArr
            diffs = []
            is_diff_safe = True
            is_monotonic = True
            count_pos = 0
            count_neg = 0

            for i in range(len(numArr)-1):
                diff = int(numArr[i]) - int(numArr[i+1])
                if abs(diff) not in safe_diffs:
                    is_diff_safe = False
                diffs.append(diff)
                
            for i in range(len(diffs)):
                        
                if diffs[i] > 0:
                    count_pos +=1 
                elif diffs[i]<0:
                    count_neg += 1
                if count_neg > 0 and count_pos > 0:
                    is_monotonic = False
                elif count_neg == 0 and count_pos == 0:
                    is_monotonic = False

            if is_diff_safe and is_monotonic:
                safe_dampened_lists.append(True)
            else:
                safe_dampened_lists.append(False)


        if True in safe_dampened_lists:
            safe_lists.append(True)
        else:
            safe_lists.append(False)

print(safe_lists.count(True))


