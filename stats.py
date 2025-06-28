def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    characters = list(text)
    uniques = dict()

    for char in characters:
        l_char = char.lower()
        if l_char in uniques:
            uniques[l_char] += 1
        else:
            uniques[l_char] = 1

    return uniques


def sort_on(items):
    return items["count"]


def sort_uniques(uniques):
    unique_items = list()

    for item in uniques:
        unique_items.append({"name": item, "count": uniques[item]})

    unique_items.sort(reverse=True, key=sort_on)

    return unique_items
