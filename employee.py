#this class creates an Employee object with various attributes

class Employee:
    counter = 0
    def __init__(self, name , rate=0.0):
        self.__name = name
        Employee.counter += 1
        self.__hours = 0
        self.__rate = rate
        self.__grossPay = 0.0
        self.EID = Employee.counter

#getters
    def getRate(self):
        return float(self.__rate)
    def getEID(self):
        return int(self.EID)
    def getName(self):
        return str(self.__name)
    def getHours(self):
        return float(self.__hours)

#computes gross pay
    def getGrossPay(self):
        self.__grossPay = float(self.__hours) * float(self.__rate)
        return float(self.__grossPay)

#overlaods the str operator to return the proper string result of an employee
    def __str__(self):
        myStr = "Employee Name: " + self.__name + "\nEmployee ID: " + str(self.EID)
        myStr = myStr + "\nHourly Rate: "+ '{:.2f}'.format(float(self.__rate))
        myStr = myStr + "\nHours Worked: " + '{:.2f}'.format(float(self.__hours))
        myStr = myStr + "\nGross Pay: "+ '{:.2f}'.format(float(self.getGrossPay()))
        return myStr
        
        #return 'Employee Name: {}\nEmployee ID: {}\nHourly Rate: {:.2f}\nHours Worked: {:.2f}\nGross Pay: {:.2f}'.format(str(self.__name), str(self.EID), str(self.__rate), str(self.__hours), str(self.__grossPay))
 
#overlaods the equals operator to determine if ID's are the same
    def __eq__(self, ID):
        if self.EID == ID.EID:
            return True
        else:
            return False
#setters   
    def setRate(self, rate):
        self.__rate = rate
    def setHours(self, hours):
        self.__hours = hours
