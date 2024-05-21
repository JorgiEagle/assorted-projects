class MyClass:
    def __init__(self, value) -> None:
        self.number = 1

    
    def get(self, item):
        return f"Test String {item}"
    

class MyOtherClass(MyClass):
    def decorator(func):
        def inner_wrapper(*args):
            result = func(*args)
            print(result)
            return result
        return inner_wrapper
    
    @decorator
    def get(self, item):
        return super().get(item)

object1 = MyOtherClass(3)
object2 = MyClass(2)
object1.get(2)
object2.get(20)