'''YOUTUBE LINK FOR PROBLEM STATEMENT AND DETAILED SOLUTION:- https://www.youtube.com/watch?v=nPnhEDWbz00&list=PLceg7N8gv62C4zp56Gr6K8tplOItxHe5h&index=11'''

class DairyProduct:
    def__init__(self, dairyid,dairyBrand,producttype,price,grade):
        self.dairyid = dairyid
        self.dairyBrand = dairyBrand
        self.producttype = producttype
        self.price = price
        self.grade = grade
        
class ProductGrade:
    def__init__(self,dairyList,weightagedict):
        self.dairyList = dairyList
        self.weightagedict = weightagedict
        
    def priceBasedOnBrandAndType(self,dairy_brand,product_type):
        flag = 0
        for i in self.dairyList:
            if(i.dairyBrand.lower() == dairy_brand.lower() and i.producttype.lower() == product_type.lower()):
                i.price = i.price+(i.price * self.weightagedict[i.grade.lower()]/100)
                flag = 1
                return i
                
        if(flag == 0):
            return None

    

n = int(input())
list_obj = []
weightage_dict = {}
for i in range(n):
    dairyid = int(input())
    dairyBrand = input()
    producttype = input()
    price = int(input())
    grade = input()
    
    list_obj.append(DairyProduct(dairyid,dairyBrand,producttype,price,grade))
    
for i in range(n):
    x = input()
    y = int(input())
    weightage_dict[x] = y

temp = ProductGrade(list_obj,weightage_dict)
dairy_brand = input()
product_type = input()
ans = temp.priceBasedOnBrandAndType(dairy_brand,product_type)
if(ans  == None):
    print("No dairy product found")
    
else:
    print("Dairy:Brand Price")
    print(ans.dairyBrand, ans.price)


    
    
