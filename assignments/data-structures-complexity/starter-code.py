"""Starter code: Estruturas de Dados e Complexidade em Python.

Objetivo: comparar abordagens com diferentes estruturas de dados.
"""

from collections import deque
from time import perf_counter
from typing import Iterable


class Stack:
    def __init__(self) -> None:
        self._items: list[str] = []

    def push(self, item: str) -> None:
        # TODO: adicionar item ao topo da pilha
        pass

    def pop(self) -> str | None:
        # TODO: remover item do topo; retornar None se vazia
        pass


class Queue:
    def __init__(self) -> None:
        self._items: deque[str] = deque()

    def enqueue(self, item: str) -> None:
        # TODO: adicionar item ao fim da fila
        pass

    def dequeue(self) -> str | None:
        # TODO: remover item do inicio; retornar None se vazia
        pass


def frequency_count(values: Iterable[int]) -> dict[int, int]:
    """TODO: contar frequencia de cada valor usando dict."""
    return {}


def has_duplicates_naive(values: list[int]) -> bool:
    """TODO: implementar abordagem O(n^2)."""
    return False


def has_duplicates_optimized(values: list[int]) -> bool:
    """TODO: implementar abordagem O(n) com set ou dict."""
    return False


def benchmark_duplicate_checks(sizes: list[int]) -> None:
    print("size | naive_seconds | optimized_seconds")
    print("-" * 42)

    for size in sizes:
        # Dica: gere dados com duplicata perto do final para estressar a versao ingenua.
        sample = list(range(size)) + [size - 1]

        start = perf_counter()
        has_duplicates_naive(sample)
        naive_elapsed = perf_counter() - start

        start = perf_counter()
        has_duplicates_optimized(sample)
        optimized_elapsed = perf_counter() - start

        print(f"{size:>4} | {naive_elapsed:>13.6f} | {optimized_elapsed:>17.6f}")


def main() -> None:
    # TODO: completar exemplos de uso de Stack/Queue e frequency_count
    benchmark_duplicate_checks([1_000, 5_000, 10_000])


if __name__ == "__main__":
    main()
