import string
from src.core.job.mapper import Mapper


class Task2Mapper(Mapper):
    def map(self, record, emit):
        line = str(record)
        for token in line.split():
            word = token.strip(string.punctuation).lower()
            if len(word) > 5:
                emit(word, 1)
