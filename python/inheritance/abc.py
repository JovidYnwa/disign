from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime


class Viechle(ABC):
    @abstractmethod
    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        raise NotImplementedError("Subcalls hould implement this method")

    @abstractmethod
    def renew_licence(self, start_date: datetime, end_date: datetime) -> str:
        raise NotImplementedError("Subcalls hould implement this method")


@dataclass
class Car(Viechle):
    model: str
    reversed: bool = False

    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        return f"Car model {self.model} is reserved at {start_date} till {end_date}"

    def renew_licence(self, start_date: datetime, end_date: datetime) -> str:
        return f"Car model {self.model} renewed till {end_date}"

@dataclass
class Truk(Viechle):
    model: str
    reversed: bool = False

    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        return f"Truk model {self.model} is reserved at {start_date} till {end_date}"

    def renew_licence(self, start_date: datetime, end_date: datetime) -> str:
        return f"Truk model {self.model} renewed till {end_date}"


def reserve_now(viechle: Viechle, start_date: datetime, end_date: datetime) -> str:
    print(viechle.reserve(start_date, end_date))


def main():
    carObj = Car("tesla", 2002)
    trukObj = Truk("Man", 2022)

    reserve_now(carObj, datetime.datetime.now(), datetime.datetime.now())
    reserve_now(trukObj, datetime.datetime.now(), datetime.datetime.now())


main()
