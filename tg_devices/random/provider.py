import random
from collections.abc import Sequence

from tg_devices.random.protocols import IRandomProvider, T


class StandardRandomProvider(IRandomProvider):
    def __init__(self, seed: str | int | None = None) -> None:
        self._random = random.Random(seed)

    def choice(
        self,
        population: Sequence[T],
        weights: Sequence[int | float] | None = None,
    ) -> T:
        chosen = self.choices(population=population, weights=weights, k=1)
        return chosen[0]

    def choices(
        self,
        population: Sequence[T],
        weights: Sequence[int | float] | None = None,
        k: int = 1,
    ) -> list[T]:
        if not population:
            raise ValueError("Population is empty")
        return self._random.choices(
            population=population, weights=weights, k=k
        )
