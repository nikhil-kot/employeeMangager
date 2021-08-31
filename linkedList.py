#these classes implement a LinkedList to store all the different employees (with their attributes)
from employee import Employee

#the following Node class code was taken from CS172 LinkedList lecture demo
class Node():
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
    def getData(self):
        return self.__data
    def getNext(self):
        return self.__next
    def setData(self, d):
        self.__data = d
    def setNext(self, n):
        self.__next = n

class LinkedList:
    def __init__(self):
        self.__head = None

#the following isEmpty method code was referenced from CS172 LinkedList lecture demo
    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False

#the following search method code was taken from CS172 LinkedList lecture demo
    def search(self, data):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        return found

#the following len method code was taken from CS172 LinkedList lecture demo
    def __len__(self):
        if self.__head == None:  # if list is empty return 0
            return 0
        
        current = self.__head   #list is not empty and has at least 1 Node
        counter = 1
        
        while current.getNext() != None: # check if theres's another item after the current node
            counter += 1
            current = current.getNext()
        return counter
 
 #the following getitem method code was taken from CS172 LinkedList lecture demo
    def __getitem__(self, index):
        if index < 0 or index > len(self) - 1:
            raise IndexError
        
        current = self.__head
        for i in range(index):
            current = current.getNext()
        return current.getData()

#the following str method code was referenced from CS172 LinkedList lecture demo
    def __str__(self):
        
        current = self.__head
        mystr = ""
        mystr += "\n*** Payroll ***\n"
        while current != None:
            mystr += str(current.getData()) + "\n"
            current = current.getNext()
        return mystr
        
        '''
        myStr = ''
        current = self.__head
        myStr += "\n*** Payroll ***\n"
        while current != None:
            employee = current.getData()
            
            x = "Employee Name: {}\n".format(employee.getName())
            myStr += x
            y = "Employee ID: {}\n".format(employee.getEID())
            myStr += y
            z = "Hourly Rate: {:.2f}\n".format(employee.getRate())
            myStr += z
            a = "Hours Worked: {:.2f}\n".format(float(employee.getHours()))
            myStr += a
            b = "Gross Pay: {:.2f}\n".format(float(employee.getGrossPay()))
            myStr += b
            myStr += '\n'
        
            
            current = current.getNext()
        return myStr
        #mystr = ''
        #current = self.__head
            
        #while current != None:
        #    mystr += str(current.getData()) + ' --> '
        #    current = current.getNext()
        
        #return mystr
        
        '''
            
#the following append method code was taken from CS172 LinkedList lecture demo  
    def append(self, data):
        newNode = Node(data)
        
        if self.isEmpty():       # if list is empty, head will point to newNode
            self.__head = newNode
            
        else:                     # list is not empty, go to end of list and add newNode there
            current = self.__head
            while current.getNext() != None: # check if theres's another item after the current node
                current = current.getNext()
            current.setNext(newNode)
 
#the following remove method code was taken from CS172 LinkedList lecture demo
    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        
        # first find item in the list
        while not found and current != None :
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if current == None:  #list was empty or item was not in the list
            return False
        elif previous == None:  # item was in the fist node
            self.__head = current.getNext()
            return True
        else:  # item was somewhere after the first node
            previous.setNext(current.getNext())
            return True
