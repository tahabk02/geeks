class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        description = []

        for animal in animal_list:
            count = self.animals[animal]
            if count > 1:
                description.append(animal + 's')
            else:
                description.append(animal)

        if len(description) > 1:
            short_desc = ', '.join(description[:-1]) + ' and ' + description[-1]
        else:
            short_desc = description[0]

        return f"{self.name}'s farm has {short_desc}."
