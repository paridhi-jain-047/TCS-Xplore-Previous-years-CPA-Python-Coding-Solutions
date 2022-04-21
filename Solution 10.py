            if(i.emp_role == role):
                i.increase_salary(percent)
                res.append(i)
        
        return res
                

if __name__ == '__main__':
    
    n = int(input())
    list_obj = []
    
    for i in range(n):
        emp_id = int(input())
        emp_name = input()
        emp_role = input()
        emp_salary = int(input())
        
        list_obj.append(Employee(emp_id,emp_name,emp_role,emp_salary))
        
    temp = Organisation(list_obj,"XYZ")
    
    input_role = input()
    input_percent = int(input())
    
    ans = temp.calculate_increament(input_role,input_percent)
    
    if(len(ans) != 0):
        for i in ans:
            print(i.emp_name,'\t',i.emp_salary)
            
    else:
        print("Nothing Found")
        
    
