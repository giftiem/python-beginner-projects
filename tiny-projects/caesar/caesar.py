import string
def shift(n, text):
    """
    Encrypt (or decrypt) the given text by shifting each character
    by n positions in the alphabet.

    For simplicity, we're only dealing with lowercase text.
    """
    alphabet = list(string.ascii_lowercase)
    text = list(text)

    for i in range(len(text)):
        char_at_i = text[i]

        if char_at_i in [' ', ',','!']:
            continue

        alph_index_i = alphabet.index(text[i])
        if (alph_index_i + n) > 26:
            diff = 26 - alph_index_i
            n = n - diff
            alph_index_i = 0
        print(alph_index_i)
        print(n)
        print(char_at_i)
        text[i] = alphabet[alph_index_i+n]
    
    print(text)

    return ''.join(text)

pangram = "the quick brown fox jumps over the lazy dog"
shifted = "gur dhvpx oebja sbk whzcf bire gur ynml qbt"
shift(13, pangram)