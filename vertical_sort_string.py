"""
Vertical sort strings and add '$' on empty strings. Example:

Input: "HOW ARE YOU"
Output: ["HAY", "ORO", "WEU"]

Input: "TIME WAITS FOR NONE"
Output: ["TWFN", "IAOO", "MIRN", "ET$E", "$S$$"]
"""

def vertically_sort(input):
    if not isinstance(input, str):
        return []

    words = input.split(" ")
    max_length = max(len(word) for word in words)
    matrix = ["" for _ in range(max_length)]

    for index in range(0, max_length):
        for word in words:
            if index >= len(word):
                matrix[index] = matrix[index] + "$"
                continue

            matrix[index] = matrix[index] + word[index]
    return matrix


assert vertically_sort("HOW ARE YOU") == ["HAY", "ORO", "WEU"]
assert vertically_sort("TIME WAITS FOR NONE") == ["TWFN", "IAOO", "MIRN", "ET$E", "$S$$"]
assert vertically_sort("A B C D") == ["ABCD"]
assert vertically_sort(1234) == []
