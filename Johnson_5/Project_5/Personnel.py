class Personnel:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Personnel):
    def __init__(self, specialty, name, age):
        super().__init__(name, age)
        self.speciality = specialty

    def display_doctor(self):
        print(f"Name: {self.name} \nAge: {self.age} \nSpecialty: {self.speciality} \n")


class Surgeon(Personnel):
    def __init__(self, board_certified, name, age):
        super().__init__(name, age)
        self.boardCertified = board_certified

    def display_surgeon(self):
        print(f"Name: {self.name} \nAge: {self.age} \nBoard Certified: {self.boardCertified} \n")


class Nurse(Personnel):
    def __init__(self, rank, name, age):
        super().__init__(name, age)
        self.rank = rank

    def display_nurse(self):
        print(f"Name: {self.name} \nAge: {self.age} \nRank: {self.rank} \n")