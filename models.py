import math

class Input:
    def __init__(self, ticksNum, intersectionsNum, streetsNum, carsNum, bonusNum, intersections, cars):
        self.ticksNum = ticksNum
        self.intersectionsNum = intersectionsNum
        self.streetsNum = streetsNum
        self.carsNum = carsNum
        self.bonusNum = bonusNum
        self.intersections = intersections
        self.cars = cars

    def filterCars (self):
        carsF = []
        for car in self.cars:
            if car.ticks < self.ticksNum:
                carsF.append(car)
                
        carsF.sort()
        return carsF
    
    def simulate (self):
        target_cars = self.filterCars()
        for tick in range(1, self.ticksNum+1):
            # for car in target_cars:
            #     car.tick(tick)
            target_cars[0].tick(tick)
    
    
    def printResult(self):
        self.simulate()
        answer = str(self.intersectionsNum) + '\n'
        for id, streets in self.intersections.items():
            answer += str(id) + "\n"
            answer += str(len(streets)) + "\n"
            for street in streets:
                answer += street.name + " " + str(math.floor(max(street.light_car_times)/len(streets)) + len(streets)) + '\n'
        return answer


    def __str__(self):
        res = f'There is {self.ticksNum} ticks, \ncross {self.intersectionsNum} intersections, with {self.streetsNum} streets, and {self.carsNum} cars, each car gives {self.bonusNum} points!\n'
        res += 'GRAPH: \n'
        for origin, streets in self.intersections.items():
            res += f'\t{origin}:\n'
            for street in streets:
                res += '\t\t' + str(street)
        res += 'CARS:\n'
        for car in self.cars:
            res += '\t' + str(car.ticks) + ' ' + str(car)

        res += 'FILTER CARS:\n'
        for car in self.filterCars():
            res += '\t' + str(car.ticks) + ' ' + str(car)
        return res + '\n'
    
class Street:
    def __init__(self, origin, to, name, length):
        self.name = name
        self.length = length
        self.to = to
        self.origin = origin 
        self.light_car_times = [1]
        
    def __str__(self):
        res = f'{self.origin} -----{self.length}-----> {self.to} ({self.name})\n'
        return res
    
class Car:
    def __init__(self, streets):
        self.streets = streets
        ticks = 0
        self.streetsNumb = 0
        for street in self.streets:
            self.streetsNumb+=1
            ticks += street.length
        self.ticks = ticks
        self.street_id = 0
        self.streetPosition = self.streets[self.street_id].length
        
    def tick(self, global_time):
        if self.streetPosition < self.streets[self.street_id].length:
            self.streetPosition += 1
        elif self.street_id < len(self.streets)-1:
            self.streets[self.street_id].light_car_times.append(global_time)
            self.street_id += 1
            self.streetPosition = 0
        
    def __lt__(self, other):
        return self.ticks < other.ticks
         
            
        
    def __str__(self):
        res = f'{list(map(str, self.streets))}\n'
        return res
    
    
class Output:
    def __init__(self, ticksNum, intersectionsNum, streetsNum, carsNum, bonusNum, Streets, Cars):
        self.ticksNum = ticksNum
        self.intersectionsNum = intersectionsNum
        self.streetsNum = streetsNum
        self.carsNum = carsNum
        self.bonusNum = bonusNum
        self.intersections = intersections
        self.Cars = Cars