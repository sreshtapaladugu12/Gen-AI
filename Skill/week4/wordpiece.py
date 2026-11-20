# WordPiece Tokenizer
# Demonstrating subword tokenization

vocabulary = {
    "un",
    "happi",
    "ness",
    "##happi",
    "##ness",
    "##able",
    "play",
    "##ing"
}


def wordpiece_tokenize(word):

    word = word.lower()

    tokens = []
    start = 0

    while start < len(word):

        end = len(word)
        found = False

        while end > start:

            substring = word[start:end]

            if start > 0:
                substring = "##" + substring

            if substring in vocabulary:

                tokens.append(substring.replace("##", ""))
                start = end
                found = True
                break

            end -= 1

        if not found:
            return ["[UNK]"]

    return tokens


words = ["unhappiness", "playing"]

for word in words:

    tokens = wordpiece_tokenize(word)

    print("Word:", word)
    print("Tokens:", tokens)
    print("Number of tokens:", len(tokens))
    print()