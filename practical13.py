# Experiment No. 13
# Bigram-Based Next Word Prediction System

from collections import Counter, defaultdict
import re


# Training corpus
text = """
Artificial Intelligence is transforming industries.
Artificial Intelligence is changing the world.
Artificial Intelligence is a powerful technology.
Artificial Intelligence is transforming the world.
Machine Learning is a part of Artificial Intelligence.
Machine Learning is changing industries.
"""


# Convert to lowercase
text = text.lower()


# Tokenize text
words = re.findall(r'\b\w+\b', text)


# Generate bigrams
bigrams = list(zip(words, words[1:]))


# Count bigram frequencies
bigram_count = Counter(bigrams)


# Create dictionary of next words
next_words = defaultdict(Counter)

for word1, word2 in bigrams:
    next_words[word1][word2] += 1


print("Bigram Frequencies:")

for bigram, count in bigram_count.items():
    print(bigram, ":", count)


# User input
word = input("\nEnter a word: ").lower()


if word in next_words:
    predicted_word = next_words[word].most_common(1)[0][0]

    print("Predicted next word:", predicted_word)

else:
    print("Word not found in training corpus.")