def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(str):
    return len(str.split())

def count_characters(str):
    dict = {}

    for item in str:
        if not item.isalpha():
            continue
        item = item.lower()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    return dict



file_path = "books/frankenstein.txt"
contents = read_file(file_path)
char_dict = count_characters(contents)

print(f"--- Begin report of {file_path} ---")
print(f"{count_words(contents)} words found in the document")
for item in char_dict:
    print(f"The '{item}' character was found {char_dict[item]} times")
print("--- End report ---")
