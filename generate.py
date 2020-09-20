import random, read_data

data, word_trans, next_cnt = read_data.read_data()
return_trans = dict()
for key, value in word_trans.items():
    return_trans[value] = key

seed = random.randint(0, len(word_trans) - 1)
length = int(input("Enter length of sequel: "))

result = [return_trans[seed]]

if length >= 20:
    print("You entered a large number")

for curr in range(1000):
    for i in range(0, length - 1):
        if seed == 0 or (not next_cnt.get(seed)):
            break
        next = random.randint(0, next_cnt[seed] - 1)
        sum = 0
        for key, value in data[seed].items():
            sum += value
            if next <= sum:
                seed = key
                break
        result.append(return_trans[seed])
    if len(result) == length:
        break

if len(result) != length:
    print("you entered a large number")
else:
    for string in result:
        print(string, end=' ')