class SomeSharedService:
    """ an example of a shared Service to be made available to regular Domains """
    def __init__(self) -> None:
        self.greeting = 'Hi,'
    
    def greet(self, name:str) -> None:
        print(f'[{self.__class__.__name__}] {self.greeting} {name}')