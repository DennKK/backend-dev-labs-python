"""Набор функций для демонстрации работы со структурами данных Python: списки, кортежи и словари."""

import random
from typing import Any, List, Tuple, Dict, Optional


def reverse_list(inp: List[Any]) -> List[Any]:
    """Возвращает список в обратном порядке."""
    return inp[::-1]


def modify_list_values(inp: List[int], modifier: Any, mode: str = "add") -> List[int]:
    """Модифицирует элементы списка по указанному режиму."""
    if mode == "apply":
        return [modifier(v) for v in inp]
    if mode == "set":
        return [modifier for _ in inp]
    if mode == "mul":
        return [v * modifier for v in inp]
    return [v + modifier for v in inp]


def all_lists_equal(*lists: List[Any]) -> bool:
    """Проверяет, равны ли все списки."""
    if len(lists) < 2:
        return True
    first = lists[0]
    return all(lst == first for lst in lists[1:])


def slice_with_params(inp: List[Any], start=None, stop=None, step=None) -> List[Any]:
    """Возвращает срез списка с параметрами."""
    if step == 0:
        raise ValueError("step cannot be zero")
    return inp[slice(start, stop, step)]


def build_number_sequence(start=0, stop=None, step=1, length=None) -> List[int]:
    """Создаёт числовую последовательность."""
    if stop is not None:
        return list(range(start, stop, step))
    if length is not None:
        return [start + i * step for i in range(length)]
    return []


def insert_into_list(inp: List[Any], index: int, element: Any) -> List[Any]:
    """Вставляет элемент в список по индексу."""
    out = inp.copy()
    out.insert(index, element)
    return out


def merge_and_sort(*lists: List[Any], sort_key=None, reverse=False) -> List[Any]:
    """Объединяет и сортирует списки."""
    merged = [x for lst in lists for x in lst]
    return sorted(merged, key=sort_key, reverse=reverse)


def generate_until_odd_length_and_analyze() -> Dict[str, Any]:
    """Генерирует список случайной длины, пока она не станет нечётной."""
    attempt = 0
    while True:
        attempt += 1
        length = random.randint(1, 10)
        lst = [random.randint(0, 5) for _ in range(length)]
        if length % 2 == 1:
            mid = length // 2
            mid_val = lst[mid]
            count_same = lst.count(mid_val)
            return {"attempts": attempt, "list": lst, "mid_val": mid_val, "count_same": count_same}


def add_and_limit(
    first: List[Any],
    *others: List[Any],
    limit=None,
    trim_strategy="pop_end"
) -> List[Any]:
    """Объединяет списки и ограничивает их длину."""
    res = first.copy()
    for o in others:
        res.extend(o)
    if limit is None:
        return res
    while len(res) > limit:
        if trim_strategy == "pop_start":
            res.pop(0)
        elif trim_strategy == "random":
            res.pop(random.randrange(len(res)))
        else:
            res.pop()
    return res



def sort_ascending(lst: List[float]) -> List[float]:
    """Возвращает отсортированный по возрастанию список."""
    return sorted(lst)


def sort_descending_via_map(lst: List[float]) -> List[float]:
    """Сортирует список по убыванию с использованием map."""
    pairs = list(map(lambda x: (x, x), lst))
    pairs.sort(key=lambda t: t[0], reverse=True)
    return [t[1] for t in pairs]


def sort_strings_by_length(lst: List[str]) -> List[str]:
    """Сортирует строки по длине."""
    zipped = list(zip(map(len, lst), lst))
    zipped.sort(key=lambda t: t[0])
    return [t[1] for t in zipped]


def sort_strings_case_insensitive(lst: List[str]) -> List[str]:
    """Сортирует строки без учёта регистра."""
    return sorted(lst, key=str.lower)


def sort_by_custom_key_map(lst: List[Any], key_func) -> List[Any]:
    """Сортирует элементы по пользовательской функции ключа."""
    pairs = list(map(lambda item: (key_func(item), item), lst))
    pairs.sort(key=lambda t: t[0])
    return [t[1] for t in pairs]


def sort_by_second_element(lst: List[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
    """Сортирует список кортежей по второму элементу."""
    return sorted(lst, key=lambda t: t[1])


def pop_min_element(lst: List[Any]) -> Any:
    """Удаляет и возвращает минимальный элемент из списка."""
    if not lst:
        return None
    min_val = min(lst)
    lst.remove(min_val)
    return min_val


def tuple_concat(*tuples: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Объединяет кортежи."""
    res = tuple()
    for t in tuples:
        res += t
    return res


def tuple_element_counts(tpl: Tuple[Any, ...], element: Any) -> int:
    """Подсчитывает количество элементов в кортеже."""
    return tpl.count(element)


def tuple_types(tpl: Tuple[Any, ...]) -> Tuple[type, ...]:
    """Возвращает типы элементов в кортеже."""
    return tuple(type(x) for x in tpl)


def tuple_contains(tpl: Tuple[Any, ...], element: Any) -> bool:
    """Проверяет наличие элемента в кортеже."""
    return element in tpl


def make_2d_from_lists(*lists: List[Any], fill_value=None) -> List[List[Any]]:
    """Создаёт двумерный список, заполняя недостающие элементы."""
    max_len = max((len(l) for l in lists), default=0)
    return [list(l) + [fill_value] * (max_len - len(l)) for l in lists]


def dict_keys_sorted(d: Dict[Any, Any]) -> List[Any]:
    """Возвращает отсортированные ключи словаря."""
    return sorted(d.keys(), key=str)


def dict_values_sum_if_numeric(d: Dict[Any, Any]) -> float:
    """Возвращает сумму всех числовых значений словаря."""
    return sum(v for v in d.values() if isinstance(v, (int, float)))


def dict_invert(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """Инвертирует словарь: значения становятся ключами."""
    res: Dict[Any, List[Any]] = {}
    for k_item, v_item in d.items():
        res.setdefault(v_item, []).append(k_item)
    return res


def count_key_presence(target_key: Any, *dicts: Dict[Any, Any]) -> int:
    """Подсчитывает количество словарей, содержащих указанный ключ."""
    return sum(1 for d in dicts if target_key in d)


def find_deepest_values(nested: Dict[Any, Any], target_key: Any) -> Optional[List[Any]]:
    """Находит значения ключа на самом глубоком уровне словаря."""
    results: List[Any] = []

    def is_leaf(node_dict: Dict[Any, Any]) -> bool:
        return not any(isinstance(val, dict) for val in node_dict.values())

    def rec(node: Any):
        if isinstance(node, dict):
            if is_leaf(node) and target_key in node:
                results.append(node[target_key])
            else:
                for val in node.values():
                    rec(val)
        elif isinstance(node, list):
            for sub in node:
                rec(sub)

    rec(nested)
    return results or None


def step_19_runner():
    """Выполняет демонстрацию всех шагов."""
    results = {
        "step1": reverse_list([1, 2, 3, 4]),
        "step2": modify_list_values([10, 20, 30], 5),
        "step3": all_lists_equal([1, 2], [1, 2], [1, 2]),
        "step4": slice_with_params([0, 1, 2, 3, 4, 5], 1, 5, 2),
        "step5": build_number_sequence(start=5, length=5, step=2),
        "step6": insert_into_list(["a", "b", "c"], 1, "x"),
        "step7": merge_and_sort([3, 1], [2]),
        "step8": generate_until_odd_length_and_analyze(),
        "step9": add_and_limit([1, 2], [3, 4, 5], limit=4),
        "step10a": sort_ascending([4, 1, 3]),
        "step10b": sort_descending_via_map([4, 1, 3]),
        "step10c": sort_strings_by_length(["k", "word", "ab"]),
        "step10d": sort_strings_case_insensitive(["b", "A", "c"]),
        "step10e": sort_by_custom_key_map(["aa", "b", "ccc"], len),
        "step10f": sort_by_second_element([(1, 3), (2, 1), (3, 2)]),
    }

    temp = [5, 2, 7, 2]
    results["step11_pop"] = pop_min_element(temp)
    results["step11_remaining"] = temp
    results["step12_concat"] = tuple_concat((1, 2), ("a",))
    results["step12_count"] = tuple_element_counts((1, 2, 1, 3), 1)
    results["step13_types"] = tuple_types((1, "a", 2.5, None))
    results["step14_contains"] = tuple_contains((1, 2, 3), 2)
    results["step15_matrix"] = make_2d_from_lists([1, 2], [3], [4, 5, 6], fill_value=0)
    sample_dict = {"a": 1, "b": 2, "c": 2}
    results["step16_keys_sorted"] = dict_keys_sorted(sample_dict)
    results["step16_values_sum"] = dict_values_sum_if_numeric(sample_dict)
    results["step16_invert"] = dict_invert(sample_dict)
    results["step17_count_key"] = count_key_presence("a", {"a": 1}, {"b": 2}, {"a": 3, "c": 4})
    complex_dict = {
        "lvl1": {
            "lvl2a": {"leaf": {"target": 1}, "inner": {"notleaf": {"target": 2}}},
            "lvl2b": {"leaf2": {"target": 3}},
        }
    }
    results["step18_find"] = find_deepest_values(complex_dict, "target")
    return results


if __name__ == "__main__":
    for name, value in step_19_runner().items():
        print(f"{name}: {value}")
