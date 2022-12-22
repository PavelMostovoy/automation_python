from abc import abstractmethod, ABC


class C(ABC):
    @abstractmethod
    def my_abstract_method(self, arg1):
        ...
    #
    # @classmethod
    # @abstractmethod
    # def my_abstract_classmethod(cls, arg2):
    #     ...
    #
    # @staticmethod
    # @abstractmethod
    # def my_abstract_staticmethod(arg3):
    #     ...
    #
    # @property
    # @abstractmethod
    # def my_abstract_property(self):
    #     ...
    #
    # @my_abstract_property.setter
    # @abstractmethod
    # def my_abstract_property(self, val):
    #     ...
    #
    # @abstractmethod
    # def _get_x(self):
    #     ...
    #
    # @abstractmethod
    # def _set_x(self, val):
    #     ...


class ClObj(C):
    var = "12"

    def my_abstract_method(self, arg1):
        print(arg1)


exemplar = ClObj()
#
# a.my_abstract_method(1)