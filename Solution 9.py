class Pan:
    def __init__(self,Id,Material,Brand,Price,Capacity):
        
        self.Id = Id
        self.Material = Material
        self.Brand = Brand
        self.Price = Price
        self.Capacity = Capacity
        
class Solution:
    
    def __init__(self,list_obj):
        self.list_obj = list_obj
    
    def Costliest_Pan(self,material):
        a = max(self.list_obj.Price)
        for i in self.list_obj:
            if(i.Price == a and i.Material == material):
                return i.Id
        
    
    def Discounted_Price(self,brand):
        for i in self.list_obj:
            if(i.Capacity > 500 and i.Brand == brand):
                i.Price -= 20 * (i.Price/100)
                temp = i.Price
                
            elif(i.Capacity > 1000 and i.Brand == brand):
                i.Price -= 26 * (i.Price/100)
                temp = i.Price
                
        return temp
    

#main function
n = int(input())
list_obj = []

for i in range(n):
    Id = int(input())
    Material = input()
    Brand = input()
    Price = int(input())
    Capacity = int(input())
    
    list_obj.append(Pan(Id,Material,Brand,Price,Capacity))
    
material = input()
brand = input()

temp = Solution(list_obj)
ans1 = temp.Costliest_Pan(material)
ans2 = temp.Discounted_Price(brand)

print(ans1)
print(ans2)
    

