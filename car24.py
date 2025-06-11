class CarInfo:
    def __init__(self, carId, carName, carType, city):
        self.__carId = carId
        self.__carName = carName
        self.__carType = carType
        self.__city = city

    def getCarId(self):
        return self.__carId

    def getCarName(self):
        return self.__carName

    def getCarType(self):
        return self.__carType

    def getCity(self):
        return self.__city

    def checkAvailability(self):
        name = self.__carName.lower()
        type_ = self.__carType.lower()
        city = self.__city.lower().replace(" ", "")  # Normalize city for input like "Newyork"

        valid_names = ["nissan", "ford"]
        valid_types = ["sedan", "suv", "muv"]
        valid_cities = {
            "newyork": "New york",
            "denver": "Denver",
            "losangels": "LosAngels"
        }

        if name not in valid_names or type_ not in valid_types or city not in valid_cities:
            return "Not Available"

        car_database = {
            "nissan": {
                "sedan": ("Kicks", 8400.0),
                "suv": ("Magnite", 10800.0),
                "muv": ("Terrano", 14400.0)
            },
            "ford": {
                "sedan": ("Figo", 4802.0),
                "suv": ("Eco Sport", 9605.0),
                "muv": ("Endeavour", 21600.0)
            }
        }

        self.__city = valid_cities[city]  # Set the correctly formatted city
        available_car, price = car_database[name][type_]
        return f"Availablecarandpriceis:{available_car}and${price}"


class UserInterface:
    @staticmethod
    def extractDetails(carDetails):
        parts = carDetails.strip().split(":")
        if len(parts) != 4:
            return None
        return CarInfo(parts[0], parts[1], parts[2], parts[3])


# Main program
if __name__ == "__main__":
    print("Enter the Car Details")
    user_input = input()
    car = UserInterface.extractDetails(user_input)

    if car is None:
        print("Invalid Details")
    else:
        result = car.checkAvailability()
        if result == "Not Available":
            print("Invalid Details")
        else:
            print("Car Id :", car.getCarId())
            print("\nMarshMCLennan Internals")
            print("CarName:" + car.getCarName())
            print("Car Type :", car.getCarType().lower())
            print("City :", car.getCity())
            print(result)
