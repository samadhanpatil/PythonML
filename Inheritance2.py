class Base:
    def __init__(self):
      print(f"inside base constructor")

class Derived(Base):
    def __init__(self):
        
        print(f"Inside derived constructor")


bobj=Base()