class Employee:
    def __init__(self, code, fname, lname, salary):
        self.code = code
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __del__(self):
        print("Object is deleted")

    def calTax(self):
        if self.salary < 1300000:
            return 0
        else:
            return (self.salary - 1300000) * 10 / 100

    def callInsurance(self):
        return self.salary * 7 / 100

    def pay(self):
        return self.salary - (self.calTax() + self.callInsurance())

    def write_to_file(self, filename):
        with open(filename+"txt", "a") as f:
            f.write(str(self))

    def __str__(self):
        s = "Code: {}\n".format(self.code)
        s += "Firstname: {}\n".format(self.fname)
        s += "Lastname: {}\n".format(self.lname)
        s += "Salary: {}\n".format(self.salary)
        s += "Tax: {}\n".format(self.calTax())
        s += "Insurance: {}\n".format(self.callInsurance())
        s += "Payment: {}\n".format(self.pay())
        return s

while True:
        
    code = input("Enter the personal code: ")
    fname = input("Enter the firstname: ")
    lname = input("Enter the lastname: ")
    salary = float(input("Enter the salary: "))

    obj = Employee(code, fname, lname, salary)
    print(obj)

    filename = input("Enter the filename to save the employee information: ")
    obj.write_to_file(filename)
    
    ans = input("Do you want to continue?")
    if ans == 'n' or 'N':
        break

del obj