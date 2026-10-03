import string
from src.core.job.mapper import Mapper


class Task1Mapper(Mapper):
    def map(self, record, emit):
        line = str(record)
        for token in line.split():
            word = token.strip(string.punctuation ).lower()
            if word:
                emit(word, 1)
