from budget import Budget


def main():
    goal = int(input("가계부 목표 지출 횟수를 입력: "))
    income = int(input("월 수익을 입력하세요: "))
    limit_per = int(input("수익의 몇 %를 넘기면 경고할까요?: "))
    budget = Budget(goal)

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            if amount > budget.income:
                print("지출 금액이 월 수익보다 클 수 없습니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
