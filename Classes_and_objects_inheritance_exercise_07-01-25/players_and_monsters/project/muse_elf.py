from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, name: str, level: int):
        super().__init__(name, level)