from abc import ABCMeta, abstractmethod
from .context import Context


class Node(metaclass=ABCMeta):
    @abstractmethod
    def assemble(self, context):
        pass
