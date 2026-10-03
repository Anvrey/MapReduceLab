import string
from src.core.job.mapper import Mapper

VOWELS = set("aeiouаеєиіїоуюя")


class Task3Mapper(Mapper):
    def map(self, record, emit):
        line = str(record)
        for token in line.split():
            word = token.strip(string.punctuation).lower()

            letters = []
            for ch in word:
                if ch.isalpha():
                    letters.append(ch)

            if not letters:
                continue

            v = 0
            for ch in letters:
                if ch in VOWELS:
                    v += 1

            c = len(letters) - v
            emit(len(letters), (v, c))
