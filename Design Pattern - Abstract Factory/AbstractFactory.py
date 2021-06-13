from abc import ABC, abstractmethod


class AbstractAlgorithm(ABC):
    @abstractmethod
    def function(self) -> str:
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def _createAlgorithmA(self) -> AbstractAlgorithm:
        pass

    @abstractmethod
    def _createAlgorithmB(self) -> AbstractAlgorithm:
        pass

    @abstractmethod
    def _createAlgorithmC(self) -> AbstractAlgorithm:
        pass
