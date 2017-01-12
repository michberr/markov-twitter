from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open file and read into memory
    text = open(file_path).read().rstrip()

    # Replace newlines with space
    #text = text.replace('\n', ' ')

    return text


def update_chains(text_string, chains, ngrams):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    # split text in to list of words
    words = text_string.split()

    # get n-grams starting at each word
    for x in range(len(words[:-ngrams])):
        key = tuple(words[x:x + ngrams])

        # add n-grams to dictionary
        if key in chains:
            chains[key].append(words[x + ngrams])
        else:
            chains[key] = [words[x + ngrams]]

    return chains


def get_uppercase(word_dict):
    """Return all keys in dictionary whose first word starts with a capital"""

    all_keys = word_dict.keys()
    upper_keys = [key for key in all_keys if key[0][0].isupper()]

    return upper_keys


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = []
    nchars = 0

    # Starting ngram (as tuple), first word in tuple must be uppercase
    start = choice(get_uppercase(chains))

    # Add starting ngram to text list
    text.extend(start)

    # Add length of words in first bigram and two spaces to nchars
    nchars += len(start[0]) + len(start[1]) + 2

    while nchars < 119:
        # Choose next word randomly from list
        new_word = choice(chains[start])

        # add length of new word to nchars
        # add one for space between words
        nchars += len(new_word) + 1

        if nchars > 120:
            break
        else:
            # Add new word to text list
            text.append(new_word)

            # Generate tuple for next ngram
            new_key = start[1:] + (new_word,)

        # Break out of loop if bigram doesn't exist
        if new_key in chains:
            start = new_key
        else:
            break

    text.append("#hackbrightgracejan17")

    # Find last sentence punctuation in text
    text_string = ' '.join(text)

    # period = text_string.rfind('.')
    # exclamation = text_string.rfind('!')
    # question = text_string.rfind('?')

    # largest = max(period, exclamation, question)

    # # Remove everything after the last punctuation, if there is anything
    # if len(text_string) == largest+1:
    #     return text_string
    # else:
    #     return text_string[:largest+1]

    return text_string
