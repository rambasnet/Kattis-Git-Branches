"""
Main manager class that manages HelloWorld
Uses Single Pattern - https://refactoring.guru/design-patterns/singleton
"""
from __future__ import annotations


from hello import HelloWorld


class Main():
    """
    Singleton class Main
    """
    _instance = None

    def __init__(self) -> None:
        """
        Constructor - uses single pattern

        Returns:
                None
        """
        if Main._instance:
            raise RuntimeError(
                "Cannot create multiple instances of a singleton class Main")
        self._solution: 'HelloWorld' = HelloWorld()
        Main._instance = self

    def solve(self) -> None:
        """
        Solves the problem

        :return: None
        """
        self._solution.print_message()

    @classmethod
    def get_instance(cls) -> 'Main':
        """Create or return exsiting instance

        Returns:
                        Main: class instance
        """
        if not cls._instance:
            cls._instance = Main()
        return cls._instance

    @staticmethod
    def main() -> None:
        """main static method
        """
        singleton_main: 'Main' = Main.get_instance()
        singleton_main.solve()


if __name__ == '__main__':
    Main.main()
