class Service:
    def __init__(self,ServiceID,Model_Name,Manf_Name,Dist_Travelled,Insured):
        self.ServiceID = ServiceID
        self.Model_Name = Model_Name
        self.Manf_Name = Manf_Name
        self.Dist_Travelled = Dist_Travelled
        self.Insured = Insured
        if Insured.lower() == "yes":
            self.Min_Payment = 1000
        else:
            self.Min_Payment = 1750
    
    
class ServiceCenter:
    
    def __init__(self,list_obj,sdict):
        self.list_obj = list_obj
        self.sdict = sdict
        
    def DistanceAndService(self,input_state_code):
        r = []
        for i in self.list_obj:
            if (self.sdict[i.ServiceID] == input_state_code and i.Dist_Travelled > 5000):
                r.append(i)
                
        if(len(r) == 0):
            print("No car found with given criteria")
            
        else:
            for i in r:
                print(i.ServiceID,i.Model_Name,i.Manf_Name,i.Min_Payment)
        

n = int(input())
list_obj = []
sdict = {}

for i in range(n):
    ServiceID = int(input())
    Model_Name = input()
    Manf_Name = input()
    Dist_Travelled = int(input())
    Insured = input()
    state_code = input()
    sdict[ServiceID] = state_code
    list_obj.append(Service(ServiceID,Model_Name,Manf_Name,Dist_Travelled,Insured))
    
input_state_code = input()
temp = ServiceCenter(list_obj,sdict)
temp.DistanceAndService(input_state_code)
    
        
        
