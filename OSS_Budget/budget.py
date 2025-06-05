import datetime
from expense import Expense

class Budget:
    def __init__(self, goal = None):
        self.expenses = []
	self.goal = goal

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


