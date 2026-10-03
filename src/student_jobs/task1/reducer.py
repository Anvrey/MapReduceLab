from src.core.job.reducer import Reducer


class Task1Reducer(Reducer):
    def reduce(self, key, values, emit):
        emit(key, sum(values))
