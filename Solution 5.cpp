'''YOUTUBE LINK FOR DETAILED SOLUTION AND PROBLEM STATEMENT:- https://www.youtube.com/watch?v=03SjHpJq_cQ'''

class Player:
    def__init__(self,playerName, playerCountry, playerAge, noOfMatches, noOfRuns, noOfWickets):
        self.playerName = playerName
        self.playerCountry = playerCountry
        self.playerAge = playerAge
        self.noOfMatches = noOfMatches
        self.noOfRuns = noOfRuns
        self.noOfWickets = noOfWickets

class Team:
    
    @classmethod
    def getMinRuns(self,list_obj):
        res=[]
        players_details = []
        for i in list_obj:
            res.append(i.noOfRuns)
        
        min1 = min(res)
        
        for i in list_obj:
            if(min1 == i.noOfRuns):
                players_details.append(i.playerName)
                players_details.append(i.min1)
                players_details.append(i.playerCountry)
        
        return players_details
                
        
    @classmethod
    def getMaxWickets(self,list_obj):
        res=[]
        players_details = []
        for i in list_obj:
            res.append(i.noOfWickets)
        
        max1 = max(res)
        
        for i in list_obj:
            if(max1 == i.noOfWickets):
                players_details.append(i.playerName)
                players_details.append(i.max1)
                players_details.append(i.playerCountry)
        
        return players_details
    
n = int(input())
list_obj = []

for i in range(n):
    player_name = input()
    player_country = input()
    player_age = input()
    no_of_matches = int(input())
    no_of_runs = int(input())
    no_of_wickets = input(input())
    
    list_obj.append(Player(player_name,player_country,player_age,no_of_matches,no_of_runs,no_of_wickets))
    
ans1 = Team.getMinRuns(list_obj)
ans2 = Team.getMaxWickets(list_obj)

print(ans1)
print(ans2)
    
