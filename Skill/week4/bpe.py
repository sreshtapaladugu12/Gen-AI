# Byte Pair Encoding (BPE)
# Demonstrating frequency counting and pair merging

from collections import Counter

# Training words with their frequencies
words = {
    "low": 5,
    "lower": 2,
    "lowest": 1
}

# Initially split words into characters
vocab = {
    word: list(word) + ["</w>"]
    for word in words
}

def get_pair_frequencies(vocab):
    pairs = Counter()

    for word, symbols in vocab.items():
        frequency = words[word]

        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pairs[pair] += frequency

    return pairs


def merge_pair(pair, vocab):
    new_vocab = {}

    for word, symbols in vocab.items():
        new_symbols = []
        i = 0

        while i < len(symbols):

            if (
                i < len(symbols) - 1
                and symbols[i] == pair[0]
                and symbols[i + 1] == pair[1]
            ):
                new_symbols.append(pair[0] + pair[1])
                i += 2

            else:
                new_symbols.append(symbols[i])
                i += 1

        new_vocab[word] = new_symbols

    return new_vocab


# Perform BPE merges
for iteration in range(5):

    frequencies = get_pair_frequencies(vocab)

    if not frequencies:
        break

    most_frequent_pair = frequencies.most_common(1)[0]

    pair = most_frequent_pair[0]
    frequency = most_frequent_pair[1]

    print("\nIteration:", iteration + 1)
    print("Pair frequencies:", frequencies)
    print("Most frequent pair:", pair)
    print("Frequency:", frequency)

    vocab = merge_pair(pair, vocab)

    print("Vocabulary after merging:")

    for word, symbols in vocab.items():
        print(word, ":", symbols)