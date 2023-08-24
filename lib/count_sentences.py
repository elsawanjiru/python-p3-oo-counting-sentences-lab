#!/usr/bin/env python3

class MyString:
  pass
import re

class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("MyString value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Use regular expressions to split the string into sentences
        # The pattern "\s*[.!?]" matches periods, question marks, and exclamation marks
        # followed by optional whitespace.
        sentences = re.split(r'\s*[.!?]', self.value)
        
        # Filter out empty sentences (resulting from consecutive punctuation marks)
        sentences = [sentence for sentence in sentences if sentence]

        return len(sentences)

# Example usage:
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())  # True
print(string.is_question())  # False
print(string.is_exclamation())  # True
print(string.count_sentences())  # 3
