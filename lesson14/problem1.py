class Employee: #we are using a class to create objects; this case the class employee will create employee name,salary and years of service

    def __init__(self,name,salary,years_of_service):
        self.__name = name
        self.__salary = salary
        self.__years_of_service = years_of_service


    def set_name(self,name):
        self.__name = name
    def set_salary(self,salary):
        self.__salary = salary
    def set_years_of_service(self,years_of_service):
        self.__years_of_service=years_of_service


    def get_name(self):  # the getter methods
        return self.__name
    def get_salary(self):
        return self.__salary
    def get_years_of_service(self):
        return self.__years_of_service

    def pension(self):
        monthly_pension_payout=self.__salary * self.__years_of_service *0.0015 #calculate the pension
        return monthly_pension_payout


def main():
    name = 'Joe Chen'
    salary = 80000
    years_of_service = 30

    employee= Employee(name,salary,years_of_service) # the object or instance of the class
    print('Employee name:', employee.get_name() )
    print('Employee salary:', employee.get_salary())
    print('Employee years of service', employee.get_years_of_service())

    print('Employee monthly pension: ', employee.pension())

main()
