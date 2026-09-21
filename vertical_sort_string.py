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

############################## REFACTOR ##################################

from itertools import zip_longest

def vertically_sort_improved(text):
    # Mantemos a sua checagem defensiva de tipo
    if not isinstance(text, str):
        return []

    # Separamos as palavras
    words = text.split(" ")
    
    # O zip_longest vai pegar a primeira letra de cada palavra, 
    # depois a segunda, etc. Se faltar letra em uma palavra curta, ele usa o "$"
    # O asterisco (*) serve para "desempacotar" a lista de palavras como argumentos separados
    transposed = zip_longest(*words, fillvalue="$")
    
    # Agora só precisamos juntar as tuplas de letras de volta em strings
    return ["".join(chars) for chars in transposed]


# Seus testes continuam passando perfeitamente!
assert vertically_sort_improved("HOW ARE YOU") == ["HAY", "ORO", "WEU"]
assert vertically_sort_improved("TIME WAITS FOR NONE") == ["TWFN", "IAOO", "MIRN", "ET$E", "$S$$"]
assert vertically_sort_improved("A B C D") == ["ABCD"]
assert vertically_sort_improved(1234) == []
