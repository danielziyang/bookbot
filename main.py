def word_counter(file):
    words = file.split()
    print(len(words))

def letter_counter(file):
    words = file.lower().split()
    dict = {}
    for word in words: 
        for c in word:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
    return(dict)

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_counter(file_contents)
        letters = letter_counter(file_contents)
        
    for k, v in letters.items():
        if k.isalpha():
            print(f'the letter {k} appears {str(v)} times')


main()