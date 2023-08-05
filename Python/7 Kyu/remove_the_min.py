

def remove_smallest(numbers):
    if len(numbers) ==0:
        return numbers
    
    
    car = [x for x in numbers]
    car.remove(min(car))
    return car
    
    
    
  

