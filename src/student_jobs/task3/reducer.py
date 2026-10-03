from src.core.job.reducer import Reducer


class Task3Reducer(Reducer):
    def reduce(self, key, values, emit):
        total_v = 0
        total_c = 0
        count = 0

        for v, c in values:
            total_v += v
            total_c += c
            count += 1

        total = total_v + total_c
        if total == 0:
            return

        v_pct = round(total_v / total * 100, 1)
        c_pct = round(total_c / total * 100, 1)

        if total_v > 0:
            ratio = round(total_c / total_v, 2)
        else:
            ratio = "inf"

        result = f"words={count}, vowels={v_pct}%({total_v}), consonants={c_pct}%({total_c}), ratio={ratio}"
        emit(key, result)
