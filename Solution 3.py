'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
''' YOUTUBE LINK FOR THE PROBLEM STATEMENT AND DETAILED SOLUTION:- https://www.youtube.com/watch?v=79yBwtWYGQY '''
class Associate:
    
    def__init__(self,id1,name,technology,experienceInYears):
        
        self.id1 = id1
        self.name = name
        self.technology = technology
        self.experienceInYears = experienceInYears
     
    
class Solution:
    
    @classmethod
    def associatesForGivenTechnology(self, list_obj, searchTechnology):
        result = []
        for i in list_obj:
            if(i.technology.lower() == searchTechnology.lower() and i.experienceInYears%5 == 0):
                result.append(i.id1)
        
        return result        


n = int(input())

list_obj = []

for i in range(n):
    id1 = int(input())
    name = input()
    technology = input()
    experienceInYears = int(input())
    
    list_obj.append(Associate(id1,name,technology,experienceInYears))
    
searchTechnology = input()

ans = Solution.associatesForGivenTechnology(list_obj, searchTechnology)

print(ans)
