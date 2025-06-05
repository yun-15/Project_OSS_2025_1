import datetime
from expense import Expense

class Budget:
    def __init__(self, goal = None, income = None, limit_per = None):
        self.expenses = []
	self.goal = goal
        self.income = income
        self.limit_per = limit_per

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
	if len(self.expenses) == self.goal:
		print(f"{self.goal}번째 지출을 기록하였습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
		line = f"{idx}. {e}"
            	if idx % 5 == 0:
                	line += "\n!Warning! {}번째 지출입니다".format(idx)
            	print(line)
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
        limit_amount = self.income * self.limit_per/100
        if total > limit_amount:
            print(f"경고: 수익의 {self.limit_per}%를 초과했습니다.")
        else:
            print(f"수익의 {self.limit_per}%를 초과하지 않았습니다.")

