def earth():
    x = "Bangladesh"
    y = "Barbados"

    result = (x < y)
    print(f"The result of { x if x < y else y} comes first in the dictionary than { x if x > y else y} is {result}.")
    print(f"The result of { x if x >  y else y} comes first in the dictionary than { x if x < y else y} is {not result}.")
