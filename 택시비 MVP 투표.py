import random

class BestPlayerVote:
    def __init__(self):
        self.participants = []
        self.taxi_fares = {}
        self.votes = {}
        self.mvp = None

    def round_to_10(self, amount):
        return round(amount / 10) * 10

    def input_participants(self):
        print("참가할 친구들 이름 입력 (최대 10명, 쉼표 구분):")
        self.participants = [name.strip() for name in input().split(",")[:10]]
        if len(self.participants) < 2:
            print("❌ 최소 2명 필요. 종료합니다.")
            exit()

    def input_taxi_fares(self):
        for participant in self.participants:
            while True:
                try:
                    self.taxi_fares[participant] = float(input(f"{participant}의 택시비 입력: "))
                    break
                except ValueError:
                    print("❌ 숫자를 입력하세요.")

    def conduct_voting(self):
        self.votes = {name: 0 for name in self.participants}
        for voter in self.participants:
            print(f"\n{voter}의 투표:")
            choices = [p for p in self.participants if p != voter]
            for i, participant in enumerate(choices, 1):
                print(f"{i}. {participant}")
            while True:
                try:
                    choice = int(input("번호 입력: ")) - 1
                    if 0 <= choice < len(choices):
                        self.votes[choices[choice]] += 1
                        break
                except (ValueError, IndexError):
                    print("❌ 유효한 번호를 입력하세요.")

    def calculate_mvp(self):
        max_votes = max(self.votes.values())
        winners = [name for name, count in self.votes.items() if count == max_votes]
        self.mvp = random.choice(winners) if len(winners) > 1 else winners[0]
        print(f"\n🎉 오늘의 MVP: {self.mvp}! 택시비 면제! 🚕")

    def calculate_fare_distribution(self):
        total_fare = sum(self.taxi_fares.values())
        per_person_fare = self.round_to_10(total_fare / (len(self.participants) - 1))
        print(f"\n💰 택시비 결과: 총 {self.round_to_10(total_fare)}원")
        print(f"{self.mvp}는 면제, 나머지: {per_person_fare}원씩 부담")

    def run(self):
        self.input_participants()
        self.input_taxi_fares()
        self.conduct_voting()
        self.calculate_mvp()
        self.calculate_fare_distribution()

if __name__ == "__main__":
    BestPlayerVote().run()
