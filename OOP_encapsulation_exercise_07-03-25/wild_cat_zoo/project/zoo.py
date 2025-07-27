from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker
from project.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"



    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        find_worker = next((w for w in self.workers if worker_name == w.name), None)
        if find_worker:
            self.workers.remove(find_worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_cost_tend_animals = sum(animal.money_for_care for animal in self.animals)
        if self.__budget < total_cost_tend_animals:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_cost_tend_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        result = [f"You have {len(self.animals)} animals",
                  f"----- {len(lions)} Lions:"]
        result += [repr(lion) for lion in lions]
        result += [f"----- {len(tigers)} Tigers:"]
        result += [repr(tiger) for tiger in tigers]
        result += [f"----- {len(cheetahs)} Cheetahs:"]
        result += [repr(cheetah) for cheetah in cheetahs]

        return "\n".join(result)

    def workers_status(self):
        keepers = [a for a in self.workers if isinstance(a, Keeper)]
        caretakers = [a for a in self.workers if isinstance(a, Caretaker)]
        vets = [a for a in self.workers if isinstance(a, Vet)]

        result = [f"You have {len(self.workers)} workers",
                  f"----- {len(keepers)} Keepers:"]
        result += [repr(lion) for lion in keepers]
        result += [f"----- {len(caretakers)} Caretakers:"]
        result += [repr(tiger) for tiger in caretakers]
        result += [f"----- {len(vets)} Vets:"]
        result += [repr(cheetah) for cheetah in vets]

        return "\n".join(result)