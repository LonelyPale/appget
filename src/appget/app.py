from abc import ABC, abstractmethod


class App(ABC):
    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def uninstall(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def upgrade(self):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def search(self):
        pass
