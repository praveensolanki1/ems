import json



class Employee:
    
#initializing constructor
    def __init__(self,name,id,title,dep_ment):
        self.id =id
        self.name = name 
        self.title = title 
        self.dep_ment = dep_ment

# employee details method
    def employee_details(self):
        print("ID:",self.id)
        print("NAME:",self.name)
        print("Title:",self.title)
        print("Department:",self.dep_ment)

    def __repr__(self) -> str:
        return f'{self.id} name is {self.name}'



class Department:
    def __init__(self,name):
        self.name = name
        self.employees = []

company = {}
employee={}


def add_department(name):
        company[name] = Department(name)

def remove_department(name):
    del company[name]

def display_all_departments():
    for department in company.values():
        print(department.name)
    

def add_employee()->str:
    ''' it takes id , name, title, and department of the '''
 


    id = int(input("enter employee id"))
    if check_id(id)==True:
        print("employee already exist,please select other option from menu")
        menu()
    else:
        name = input("enter the name of the employee to add")
        title = input("enter the title of the employee to add")
        dep_ment = input("enter the department of the employee to add")

        data_object = Employee(id,name,title,dep_ment)
    
        with open('employee.json', 'w') as file:
            json.dump(data_object,file)
            





def check_id(id)->bool:
    with open("emp_data.json","w+") as file:
        json_obj = json.load(file)
        for data in json_obj:
            if data['id']==int(id):
                return True 
            else:
                return False


def view_employee_list():
    for emp in employee.values():
        print(emp)

def remove_employee():
    
    id = int(input("enter employee id that to be remove"))
    if check_id(id)==False:
        print("employee does not exist,please select other option from menu")
        menu()
    else:
         
         with open('employee.json', 'r') as file:
            json_object = json.loads(file)
            for object in json_object:
                if object["id"]==id:
                    json_object.remove(object)

    

def display_employee():
     
     id = int(input("enter employee id that to be display"))
     if check_id(id)==False:
        print("employee does not exist,please select other option from menu")
        menu()


   

def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("A to Add Employee")
    print("R to Remove Employee ")
    print("D to Display Employees")
    print("E to Exit")
     
  
    value = str(input("Enter your Choice "))
    if value == "A" or "a":
        add_employee()
         
    elif value == "R" or "r":
        remove_employee()
                  
    elif value == "D" or "d":
        display_employee()
         
    elif value == "E" or "e":
        exit()
         
    else:
        print("Invalid Input value")
       


if __name__=="__main__":
    menu()        