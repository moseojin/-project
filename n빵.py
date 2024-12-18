class Splitter:
    def __init__(self):
        self.places = {}

    def get_places(self):
        print("장소와 총 금액을 입력하세요 (종료: '끝')")
        while True:
            place = input("장소: ").strip()
            if place == "끝":
                break
            try:
                cost = float(input(f"{place} 금액: "))
                self.places[place] = self.places.get(place, 0) + cost
            except ValueError:
                print("숫자를 입력하세요.")

    def calculate_split(self):
        total = sum(self.places.values())
        print("\n장소별 총 금액:")
        for place, cost in self.places.items():
            print(f"- {place}: {cost:.0f}원")
        print(f"총 금액: {total:.0f}원")

        while True:
            try:
                num_people = int(input("\n참여 인원 수: "))
                if num_people > 0:
                    per_person = round(total / num_people, 2)
                    print(f"1인당 부담 금액: {per_person:.0f}원")
                    break
                else:
                    print("참여 인원은 1명 이상이어야 합니다.")
            except ValueError:
                print("숫자를 입력하세요.")

    def run(self):
        self.get_places()
        if not self.places:
            print("입력된 금액이 없습니다.")
            return
        self.calculate_split()

if __name__ == "__main__":
    Splitter().run()
