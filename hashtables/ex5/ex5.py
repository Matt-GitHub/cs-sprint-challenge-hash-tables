# Your code here


def finder(files, queries):
    cache = {}
    for file in files:
        # print(file.split('/'))
        split = file.split('/')
        for x in split:
            if x in cache:
                cache[x] = [cache[x], file]
            else:
                cache[x] = file
    solution = []
    for value in queries:
        if value in cache:
            solution.append(cache[value])
    answer = []

    def final(arr):
        for i in arr:
            final(i) if isinstance(i, list) else answer.append(i)
    final(solution)
    return answer


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz",
        "bin"
    ]
    print(finder(files, queries))
