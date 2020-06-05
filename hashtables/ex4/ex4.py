def has_negatives(a):
    result = {}
    answer = []
    for num in a:
        if num * -1 not in result:
            result[num] = num
        else:
            answer.append(abs(num))
    return answer


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
