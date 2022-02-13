'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''YOUTUBE LINK FOR THE PROBLEM STATEMENT AND DETAILED SOLUTION:- https://www.youtube.com/watch?v=4i0FDCk3Qkk'''

class CricketPlayer:
    def__init__(self,cplayerName, cplayedCountry,cplayerAge,cpCountryFrom):
        self.cplayerName = cplayerName
        self.cplayedCountry = cplayedCountry
        self.cplayerAge = cplayerAge
        self.cpCountryFrom = cpCountryFrom
        
    
class Solution:
    
    @classmethod
    def countPlayers(cls,country_name,list_obj):
        count = 0
        for i in list_obj:
            if(i.cpCountryFrom == country_name):
                count += 1
        return count
        
    @classmethod
    def getPlayerPlayedForMaxCountry(cls,list_obj):
        res=0
        player_name = ''
        for i in list_obj:
            max_countries = i.cplayedCountry
            if(len(max_countries) > res):
                res = len(max_countries)
                player_name = i.cplayerName
                
        return player_name

n = int(input())

list_obj = []

for i in range(n):
    player_name = input()
    no_of_countries = int(input())
    countries_list = []
    for j in range(no_of_countries):
        country = input()
        countries_list.append(country)
    player_age = int(input())
    players_home_country = input()
    list_obj.append(CricketPlayer(player_name,countries_list,player_age,players_home_country))
    
country_name = input()
ans1 = Solution.countPLayers(country_name,list_obj)
print(ans1)

ans2 = Solution.getPlayerPlayedForMaxCountry(list_obj)
print(ans2)
