# YOUTUBE LINK FOR PROBLEM STATEMENT AND DETAILED SOLUTION :- https://www.youtube.com/watch?v=kOBXntqoh4o

class Painting:
    
    def __init__(self,paintingID,painterName,paintingprice,paintingtype):
        self.paintingID = paintingID
        self.painterName = paintingName
        self.paintingprice = paintingprice
        self.paintingtype = paintingtype
        

class ShowRoom:
    
    def __init__(self,paintingList):
        self.paintingList = paintingList
    
    def getTotalPaintingPrice(self,ptype):
        flag=0
        for i in self.paintingList:
            if i.paintingtype.lower() == ptype.lower():
                s+= i.paintingprice
                flag = 1
            if(flag==0):
                return "No painting found"
            else:
                return s
        
    def getPainterWithMaxCountPaintings(self):
        
        d = {}
        s=0
        for i in self.paintingList:
            if(i.painterName in d.keys()):
                d[i.painterName] += 1
                
            else:
                d[i.painterName] = 1
                
        for i in sorted(d.keys()):
            if(s<d[i]):
                s = d[i]
                name = i
        return name
        
if __name__ == '__main__':
    
    n = int(input())
    
    list_obj = []
    
    for i in range(n):
        paintingID = int(input())
        painterName = input()
        paintingprice = int(input())
        paintingtype = input()
        list_obj.append(Painting(paintingID,painterName,paintingprice,paintingtype))
    
    ptype = input()
    temp = showRoom(list_obj)
    ans1 = temp.getTotalPaintingPrice(ptype)
    ans2 = temp.getPainterWithMaxCountPaintings()
    
    print(ans1)
    print(ans2)
    
    
        
        

  
  
