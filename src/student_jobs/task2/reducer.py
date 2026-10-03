from src.core.job.reducer import Reducer


class Task2Reducer(Reducer):
    def reduce(self, key, values, emit):
        emit(key, sum(values))
