
class Dog:
    species = "dog"  

    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def __str__(self) -> str:
        return f"{self.name} is a {self.breed} ({self.species})"


tommy = Dog("Tommy", "Labrador")
mithu = Dog("Mithu", "Beagle")

print(tommy)
print(mithu)