'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
''' WRITE A PROGRAM TO PRINT DISEASE BASED ON THE GIVEN DATA'''
''' VIDEO LINK:https://www.youtube.com/watch?v=Xkn0DLbfGIs'''

class Medicine:
    def __init__(self,MedicineName,batch,price):
        self.MedicineName = MedicineName
        self.batch = batch
        self.disease = disease
        self.price = price
        
class Solution:
    @classmethod
    def getPriceByDisease(cls, list_Med, dis):
        result = []
        for i in list_Med:
            if(i.disease.lower() == dis.lower()):
                result.apped(i.price)
        
        return result
        
n = int(input())
list_Med = []
for i in range(n):
    MedicineName = input()
    batch = input()
    disease = input()
    price = int(input())
    list_Med = append(Medicine(MedicineName,batch,disease,price)
    
dis = input()
answer = Solution.getPriceByDisease(list_Med,dis)

for i in answer:
    print(i)