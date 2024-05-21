import csv
from tqdm import tqdm


def count_and_say(n):
    n_str = str(n)
    count_dict = {}
    for digit in n_str:
        if digit in count_dict:
            count_dict[digit] += 1
        else:
            count_dict[digit] = 1
    say = ""
    for digit in sorted(count_dict.keys()):
        say += str(count_dict[digit]) + digit
    return say


def find_cycle_or_fixed_point(n, only_fixed_points=False):
    seen = {}
    sequence = []
    current = str(n)

    while current not in seen:
        seen[current] = len(sequence)
        sequence.append(current)
        current = count_and_say(current)

    cycle_start = seen[current]
    cycle = sequence[cycle_start:]

    if only_fixed_points:
        # 从循环中找到不动点
        fixed_points = [x for x in cycle if count_and_say(x) == x]
        return fixed_points
    return cycle


def find_all_cycles_and_fixed_points(digit_count, output_csv, only_fixed_points=False):
    max_number = 10**digit_count
    seen = set()

    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Initial Number", "Fixed Point"])

        for number in tqdm(range(max_number), desc="Processing"):
            number_str = str(number)
            if number_str in seen:
                continue

            result = find_cycle_or_fixed_point(number_str, only_fixed_points)
            if only_fixed_points and result:
                for fixed_point in result:
                    if fixed_point not in seen:
                        writer.writerow([number_str, fixed_point])
                        seen.add(fixed_point)
            elif not only_fixed_points:
                for item in result:
                    seen.add(item)
                writer.writerow([number_str] + result)


def print_iterations_and_check_cycle(n):
    seen = {}
    sequence = []
    current = str(n)
    iteration = 0

    while current not in seen:
        seen[current] = iteration
        sequence.append(current)
        print(current)
        current = count_and_say(current)
        iteration += 1

    cycle_start = seen[current]
    cycle = sequence[cycle_start:]

    if any(count_and_say(x) == x for x in cycle):
        fixed_points = [x for x in cycle if count_and_say(x) == x]
        fixed_point = fixed_points[0]
        print(fixed_point + " *")
        print(f"数字{n}存在不动点{fixed_point}")
    else:
        print("<----loop---->")
        for i in range(cycle_start, len(sequence)):
            print(sequence[cycle_start + i - cycle_start])
        print("<----loop---->")
        print(f"数字{n}存在循环")


# 示例调用
print("调用 count_and_say(1000000000000):")
print(count_and_say(1000000000000))

print("\n调用 find_cycle_or_fixed_point(1):")
print(find_cycle_or_fixed_point(1))

print("\n调用 print_iterations_and_check_cycle(1):")
print_iterations_and_check_cycle(1)

print("\n调用 print_iterations_and_check_cycle(1000000000000):")
print_iterations_and_check_cycle(1000000000000)

# 下面调用需要时间较长，先注释，有需要可以执行。
# print("\n调用 find_all_cycles_and_fixed_points(7, 'fixed_points.csv', only_fixed_points=True):")
# find_all_cycles_and_fixed_points(7, 'fixed_points.csv', only_fixed_points=True)
