# Find the maximum and minimum of 5 numbers.

print('Enter 5 numbers:')

data_array = [0] * 5

count_min = 0
count_max = 0

index_min = []
index_max = []

for i in range(5):
    while True:
        a = input()
        try:
            int(a)
            break
        except ValueError:
            print('Invalid data. You must enter a number.')
    data_array[i] = int(a)

for i in range(5):
    if data_array[i] == min(data_array):
        index_min.append(i + 1)
        count_min += 1

    if data_array[i] == max(data_array):
        index_max.append(i + 1)
        count_max += 1

print('Min = ', min(data_array), '; Max = ', max(data_array))
print('Index: Min = ', index_min, '; Max = ', index_max)
print('Count: Min = ', count_min, '; Max = ', count_max)
