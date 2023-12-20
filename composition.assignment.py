class Engine:
    def start(self)->None:
        return "Broom broom!!"

    def __str__(self) -> str:
        return f"hello i am engine"
    
    def __repr__(self) -> str:
        return "hi,cmd prompt! i am engine"
    
class car:
    def __init__(self)->None:
        self.engine = Engine()

    def start_car(self)->None:
        return self.engine.start()
    
    def __str__(self) -> str:
        return "hello i am car"

    def __str__(self) -> str:
        return "Hi,cmd prompt i am a car"

if __name__ == '__main__':
    indica = car()
    # honda = Engine()
    result = indica.start_car()
    print(indica.engine)
    del indica
    print(result)





