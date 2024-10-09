import datetime


class Viechle:

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        raise NotImplementedError("Subcalls hould implement this method")

    def renew_licence(self, start_date: datetime, end_date: datetime) -> str:
        raise NotImplementedError("Subcalls hould implement this method")


class Car(Viechle):

    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        return f"Car model {self.model} is reserved at {start_date} till {end_date}"

    def renew_licence(self, start_date: datetime, end_date: datetime) -> str:
        return f"Car model {self.model} renewed till {end_date}"


class Truk(Viechle):

    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        return f"Truk model {self.model} is reserved at {start_date} till {end_date}"

    def renew_licence(self, start_date: datetime, end_date: datetime) -> str:
        return f"Truk model {self.model} renewed till {end_date}"


def reserve_now(viechle: Viechle, start_date: datetime, end_date: datetime) -> str:
    print(viechle.reserve(start_date, end_date))


def main():
    carObj = Car("yo", "tesla", 2002)
    trukObj = Truk("yo", "Man", 2022)

    reserve_now(carObj, datetime.datetime.now(), datetime.datetime.now())
    reserve_now(trukObj, datetime.datetime.now(), datetime.datetime.now())


main()
