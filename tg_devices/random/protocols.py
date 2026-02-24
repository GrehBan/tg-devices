from collections.abc import Sequence
from typing import Protocol, TypeVar

T = TypeVar("T")


class IRandomProvider(Protocol):
    def choice(
        self,
        population: Sequence[T],
        weights: Sequence[int | float] | None = None,
    ) -> T: ...

    def choices(
        self,
        population: Sequence[T],
        weights: Sequence[int | float] | None = None,
        k: int = 1,
    ) -> list[T]: ...
