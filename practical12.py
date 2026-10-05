# Experiment No. 12
# Text Preprocessing in Python

import re


text = """
Artificial Intelligence is a field of Computer Science.
AI helps computers learn, reason and solve problems.
"""


print("Original Text:")
print(text)


# Convert text to lowercase
text = text.lower()

print("\nLowercase Text:")
print(text)


# Remove punctuation
text_without_punctuation = re.sub(r'[^\w\s]', '', text)

print("\nAfter Removing Punctuation:")
print(text_without_punctuation)


# Tokenization
tokens = text_without_punctuation.split()

print("\nTokens:")
print(tokens)


# Stop words
stop_words = {
    "is", "a", "of", "and", "the",
    "to", "in", "helps"
}


filtered_tokens = [
    word for word in tokens
    if word not in stop_words
]

print("\nAfter Removing Stop Words:")
print(filtered_tokens)


# Word frequency
frequency = {}

for word in filtered_tokens:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)