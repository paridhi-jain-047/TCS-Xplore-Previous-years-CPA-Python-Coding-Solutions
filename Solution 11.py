class Employee:
    
    def __init__(self,empno,empname,leaves):
        
        self.empno = empno
        self.empname = empname
        self.leaves = leaves
        
class Company:
    
    def __init__(self,cname,emps):
        
        self.cname = cname
        self.emps = emps
        
    def display_leaves(self,emp_no,leave_type):
        
        for i in self.emps:
            if(i.empno == emp_no):
                return i.leaves[leave_type]
                
    def leave_application(self,emp_no,leave_type,no_leaves):
        flag = False
        for i in self.emps:
            if(i.empno == empno):
                for key,data in i.leaves.items():
                    if(key == leave_type and data >= no_leaves):
                        flag = True
        
        if(flag):
            return "Granted"
            
        else:
            return "Rejected"
            

if __name__ == '__main__':
    
    n = int(input())
    list_obj = []
    
    for i in range(n):
        leaves = {}
        empno = int(input())
        empname = input()
        leaves["EL"] = int(input())
        leaves["SL"] = int(input())
        leaves["CL"] = int(input())
        list_obj.append(Employee(leaves,empno,empname))
        
    cname = input()
    
    temp = Company(cname,list_obj)
    
    emp_no = int(input())
    leave_type = input()
    no_leaves = int(input())
    
    ans1 = temp.display_leaves(emp_no,leave_type)
    print(ans1)
    ans2 = temp.leave_application(emp_no,leave_type,no_leaves)
    print(ans2)
