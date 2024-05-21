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


def find_cycle_or_fixed_point(n):
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
    seen = {}
    sequence = []
    current = str(n)
    while current not in seen:
        seen[current] = len(sequence)
        sequence.append(current)
        current = count_and_say(current)
    cycle_start = seen[current]
    cycle = sequence[cycle_start:]
    return cycle
