class Employee:
    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self._salary_to_pay = 0
        #self.time = 0

    def register_time(self, time):
        if time > 8:
             self._salary_to_pay += 8 * self.rate_per_hour + \
                                  (time - 8) * 2 * self.rate_per_hour
             # self.time = ... #to samo tylko bez "* self.rate_per_hour"
        else:
             self._salary_to_pay += time * self.rate_per_hour
             # self.time = time

    def pay_salary(self):
        result = self._salary_to_pay
        # result = self.time * self.rate_per_hour
        self._salary_to_pay = 0
        # self.time = 0
        return result

if __name__ == "__main__":
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    #print("Hacking!", employee._salary_to_pay)
    print(employee.pay_salary())
    print(employee.pay_salary())
    employee.register_time(10)
    print(employee.pay_salary())
    employee.register_time(5)
    employee.register_time(5)
    print(employee.pay_salary())  # spodziewam się 1000
