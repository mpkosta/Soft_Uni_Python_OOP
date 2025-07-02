from project.wizard import Wizard


class SoulMaster(Wizard):
    def __init__(self, name: str, level: int):
        super().__init__(name, level)