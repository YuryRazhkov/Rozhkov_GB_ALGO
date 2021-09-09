# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

num_list = [56, -1, 1, 1, 1, 6413233, -2225, 411, -222, 2, 222222222, -4, 1, 6, 7, 2, 1, 5]

min_el = 0
pose_el = 0
for i in range(len(num_list)):
    if num_list[i] < min_el:
        min_el = num_list[i]
        pose_el = i

print(f'min element is {min_el} on position {pose_el}')
