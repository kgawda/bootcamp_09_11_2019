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

#class PremiumEmployee(Employee):
#    def give_bonus(self, bonus_value):
#        self._salary_to_pay += bonus_value

class PremiumEmployee(Employee):
    def __init__(self, first_name, last_name, rate_per_hour):
        super().__init__(first_name, last_name, rate_per_hour)
        self._bonuses = 0

    def give_bonus(self, bonus_value):
        self._bonuses += bonus_value

    def pay_salary(self):
        result = super().pay_salary()
        result += self._bonuses
        self._bonuses = 0
        return result