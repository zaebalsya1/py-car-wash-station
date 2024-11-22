class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center == 0:
            raise ValueError("Distance from city center cannot be zero.")
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = max(car.clean_mark, self.clean_power)

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = round(
            total_rating / self.count_of_ratings, 1
        )
