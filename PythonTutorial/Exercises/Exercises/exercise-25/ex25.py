# Exercise 25: Even More Practice

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Use break_words method
a = break_words("Hello, I'm Tung")
print(a)

# Use sort_words method
b = sort_words("abd, dsd")
print(b)

# Use another sort_words method example
c = sort_words("dcba, tung vu123")
print(c)

# Use two print-word methods
print_first_word(a)
print_last_word(c)

# Use sort_sentence method
d = sort_sentence("Hello world!, I'm Vu Tung")
print(d)

# Use two print-word methods
print_first_and_last("Hello world!, I'm Vu Tung")

print_first_and_last_sorted("Hello world!, I'm Vu Tung")