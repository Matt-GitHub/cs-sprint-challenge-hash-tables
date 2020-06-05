def get_indices_of_item_weights(weights, length, limit):
    # weights is equal to an array =>  weights = [12, 18, 14, 4, 7, 9, 21]
    # limit is the desired comibined weight from a pair in weights
    checker = {}

    for i in range(len(weights)):
        if weights[i] not in checker:
            checker[weights[i]] = i

    for i in range(len(weights)):
        target = limit - weights[i]
        if target in checker:
            if checker[target] == i:
                pass
                # return [i + 1, checker[target]]
            elif checker[target] > i:
                return [checker[target], i]
            else:
                return [i, checker[target]]
    return None


# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]

# print(get_indices_of_item_weights(weights_4, len(weights_4), 22))

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# print(get_indices_of_item_weights(weights_4, 9, 7))

# weights_2 = [1, 2, 3, 3, 4, 2, 4]
# print(get_indices_of_item_weights(weights_2, 2, 8))
