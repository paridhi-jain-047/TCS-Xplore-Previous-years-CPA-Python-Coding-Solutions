'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

''' Youtube Link for the problem statement:-https://www.youtube.com/watch?v=49oDxmYgDxY&t=62s'''


class Traveler:
    
    def__init(self,travelerName,traveledCountry,travelerAge,countryFrom):
        self.travelerName = travelerName;
        self.traveledCountry = traveledCountry;
        self.travelerAge = travelerAge;
        self.countryFrom = countryFrom;
        
        
class TravelAgency:
    @classmethod
    def countTravelersTraveledCountry(self,list_obj,find_country):
        count = 0
        for i in list_obj:
            if(find_country in i.traveledCountry):
                count += 1
        
        return count
        
    @classmethod
    def getTravelerTraveledMaxCountry(self,list_obj):
        res = 0
        traveler_name = ''
        for i  in list_obj:
            list1 = i.traveledCountry
            if(res < len(list1)):
                res = len(list1)
                traveler_name = i.traveler_name
        
        return traveler_name
    
n = int(input())
list_obj = []  '''these two lines needed to be written in every code'''

for i in range(n):
    traveler = input()
    c = int(input())
    traveledCountry = []
    for j in range(c):
        traveledCountry.append(input())
    
    travelerAge = int(input())
    
    countryFrom = input()
    
    list_obj.append(Traveler(travelerName,traveledCountry,travelerAge,countryFrom))
    
find_country = input()

ans1 = TravelAgency.countTravelersTraveledCountry(list_obj,find_country)
ans2 = TravelAgency.getTravelerTraveledMaxCountry(list_obj)

print(ans1)
print(ans2)
