

class Car:
    def __init__(self,engine_size,speed,model,color,brand,price,start_engine):
        self.engine_size = engine_size
        self.speed = speed
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price
        self.start_engine = start_engine
        
        
    def car_info(self):
        print(f"Car Brand : {self.brand}")
        print(f"Car Color : {self.color}")
        print(f"Car Speed : {self.speed}")
        print(f"Car Model : {self.model}")
        print(f"Car Engine size : {self.engine_size}")
        print(f"Car Price : {self.price}")
        
    
    def start_engine(self):
        self.start_engine = True
        
    def stop_engine(self):
        self.start_engine = False
        
    def __str__(self):
        return "Class Car *****"    
    


car1 = Car(1500,200,"2024","Black","BMW",50000,False)
car2 = Car(1800,220,"2023","White","Hunda",34000,False)
car1.color = "Orange"
car1.car_info()   
car2.car_info()        
          
        
        