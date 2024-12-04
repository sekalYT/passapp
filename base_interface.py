from abc import ABC, abstractmethod

class BaseInterface(ABC):
    @abstractmethod
    def run(self):
        pass