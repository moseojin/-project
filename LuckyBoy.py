import random

class TaxiFareCalculator:
    def __init__(self):
        self.people = []
        self.total_fare = 0
        self.lucky_person = None
        self.per_person_share = 0

    def input_people(self):
        print("택시비 정산 프로그램: 럭키 보이")
        print("사람 이름과 택시비를 입력하세요. (입력을 종료하려면 빈 줄을 입력)")

        while True:
            name = input("이름: ")
            if not name:
                break
            try:
                fare = float(input(f"{name}의 택시비: "))
                self.people.append((name, fare))
            except ValueError:
                print("잘못된 입력입니다. 숫자로 입력해주세요.")

        if not self.people:
            print("입력된 사람이 없습니다. 프로그램을 종료합니다.")
            return False

        return True

    def calculate_fare(self):
        self.total_fare = sum(fare for _, fare in self.people)

    def select_lucky_person(self):
        self.lucky_person = random.choice(self.people)

    def calculate_share(self):
        remaining_people = [person for person in self.people if person != self.lucky_person]
        self.per_person_share = round(self.total_fare / len(remaining_people), -1)  # 1/n 금액 반올림

    def display_result(self):
        print("\n결과:")
        print(f"총 택시비: {format(int(round(self.total_fare, -1)), ',')}원")
        print(f"오늘의 럭키 보이! : {self.lucky_person[0]}! 택시비 면제!")
        print(f"나머지 인원의 금액: {format(int(self.per_person_share), ',')}원")

    def run(self):
        if not self.input_people():
            return
        self.calculate_fare()
        self.select_lucky_person()
        self.calculate_share()
        self.display_result()

if __name__ == "__main__":
    calculator = TaxiFareCalculator()
    calculator.run()
