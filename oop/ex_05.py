class CashMachine:
    def __init__(self):
        self._money = []  # lista posiadanych banknotów (int)

    def is_available(self):
        return bool(self._money)
        # return len(self._money) > 0

    def put_money(self, bills):
        # for bill in bills:
        #     if bill in (50, 100, 200):
        #         self._money.append(bill)
        self._money.extend(bills)

    def withdraw_money(self, amount):
        collected_sum = 0
        collected_bills = []
        self._money.sort(reverse=True)
        for bill in self._money:
            if bill + collected_sum <= amount:
                collected_sum += bill
                collected_bills.append(bill)
        if collected_sum == amount:
            for bill in collected_bills:
                self._money.remove(bill)
            return collected_bills
        # TODO else:

def test_cash_machine_init():
    machine = CashMachine()
    assert machine.is_available() == False

def test_cash_machine_put_money():
    machine = CashMachine()
    machine.put_money([50, 100])
    assert machine.is_available()

def test_cash_machine_withdraw():
    machine = CashMachine()
    machine.put_money([200, 100, 100, 50])
    assert machine.withdraw_money(150) == [100, 50]

def test_cash_machine_withdraw_different_order():
    machine = CashMachine()
    machine.put_money([200, 50, 50, 100])
    assert machine.withdraw_money(150) == [100, 50]