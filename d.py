from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoggingLibraryLogger(Logger):
    def log(self, message):
        print(message)

class LoguruLogger(Logger):
    def log(self, message):
        print(message)

class MyClass:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        print("Doing something")

def main():

    logger = LoggingLibraryLogger()
    obj = MyClass(logger)
    obj.do_something()

if __name__ == "__main__":
    main()