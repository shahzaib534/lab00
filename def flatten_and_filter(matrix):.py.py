def flatten_and_filter(matrix):
    result = []

    for row in matrix:
        for item in row:
            if isinstance(item, int) and item % 2 == 0:
                result.append(item ** 3)

    return result


def collatz_steps(n):
    steps = 0

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1

        steps += 1

    return steps


def nucleotide_count(sequence):
    counts = {}

    for nucleotide in sequence:
        counts[nucleotide] = counts.get(nucleotide, 0) + 1

    return counts


def compare_enrollments(roster_a, roster_b):
    set_a = set(roster_a)
    set_b = set(roster_b)

    return {
        "both": set_a & set_b,
        "only_a": set_a - set_b,
        "only_b": set_b - set_a,
        "all_unique": set_a | set_b
    }


# Test cases

print("Part 1:")
print(flatten_and_filter([[1, 2, 3], [4, 5, 6], [8, 9]]))
# Expected: [8, 64, 216, 512]

print("\nPart 2:")
print(collatz_steps(6))
# Expected: 8

print("\nPart 3:")
print(nucleotide_count("GATTACA"))
# Expected: {'G': 1, 'A': 3, 'T': 2, 'C': 1}

print("\nPart 4:")
print(compare_enrollments(
    [1001, 1002, 1003, 1004],
    [1003, 1004, 1005, 1006]
))