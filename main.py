#this program acts as a payroll application simulation
#By: Deeksha Reddy (dgr39)

from linkedList import LinkedList
from linkedList import Node
from employee import Employee 

#creating an empty list
empList = LinkedList()

#function for displaying menu
def menu():
    print('a. Add New Employee')
    print('b. Enter Employee Hours')
    print('c. Update Employee Hourly Rate')
    print('d. Display Payroll')
    print('e. Remove Employee from Payroll')
    print('f. Exit the program\n')
    return input('Enter your choice: ')

print("*** CS 172 Payroll Simulator ***")
choice = menu()

#loop for taking user input/calling on necessary linked methods and displaying menu again
while choice != 'f':
    
    if choice == 'a':
        name = input('Enter the new employee name: ')
        rate = float(input('Enter their hourly rate: '))
        print(end='')
        Emp = Employee(name, rate)
        empList.append(Emp)
        #print(Emp.getEID())
        print("Employee {} added to payroll\n".format(Emp.getEID()))
     
    
    if choice == 'b':
        for item in empList:
            print('Enter hours worked for employee' , item.getEID(),':', end=' ')
            hours = input()
            item.setHours(hours)
            #print(item.getHours())
    
    if choice == 'c':
        id = input('Enter employee ID: ')
        id = int(id)
        #index = id-1
        
        for item in empList:
            if item.getEID() == id:
                #print(item)
                print('Enter new wage for employee', id, ':', end=' ')
                newRate = input()
                item.setRate(newRate)
                
            else:
                print("Employee doesn't exist.")
                
    if choice == 'd':
        print(empList)
    
    if choice == 'e':
        id = input('Enter employee ID: ')
        id = int(id)
        #index = id-1
        if empList.isEmpty() == False:
            for item in empList:
                if item.getEID() == id:
                    empList.remove(item) 
                else:
                    print("Employee doesn't exist.")
        else:
            print("Employee doesn't exist.")

#exception handling
    if choice != "a" and choice !="b" and choice !="c" and choice !="d" and choice !="e" :
        print("Invalid entry.")
    choice = menu()  

else:
    if choice == "f":
        print('Goodbye.')
        
    
    