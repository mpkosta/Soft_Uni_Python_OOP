from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(BaseWorker):
    @staticmethod
    def work(): #ne podavame clasa ili self, toi ne pravi nishto ne modificira obecta po nikakuv nachin
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), f"worker {worker} must be of type {BaseWorker.__name__}"

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

class SuperWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
