from abc import ABC, abstractmethod


class Specification(ABC):
    @abstractmethod
    def apply(self, query):
        raise NotImplementedError("Specification must specify apply()")

    def __call__(self, query):
        return self.apply(query)


def specification(func: callable):
    def create_specification(*args, **kwargs):
        def created_specification(query):
            return func(query=query, *args, **kwargs)

        return created_specification

    return create_specification
