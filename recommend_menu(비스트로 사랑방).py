import random

class BistroMenu:
    def __init__(self):
        # 메뉴 데이터
        self.menu_data = {
            "식사 메뉴": {
                "감자 베이컨 크림 뇨끼": 16000,
                "4가지 고추 정통 까르보나라": 14000,
                "3색 파스타": 16000,
                "부라따 치즈 토마토 파스타": 16000,
                "새우 바질 리조또": 16000,
                "포르치니 버섯 리조또": 14000,
                "치킨 로제 리조또": 14000,
            },
            "음료 메뉴": {
                "콜라": 3000,
                "사이다": 3000,
                "아메리카노": 4000,
            },
            "주류 메뉴": {
                "하이볼": 7000,
                "상그리아": 7000,
                "스텔라 아르투아": 6500,
            }
        }

    def recommend_menu(self, budget, people, drinks, alcohols):
        total_price = 0
        recommendations = []

        # 식사 + 음료 추천
        for _ in range(drinks):
            meal = random.choice(list(self.menu_data["식사 메뉴"].items()))
            drink = random.choice(list(self.menu_data["음료 메뉴"].items()))
            if total_price + meal[1] + drink[1] <= budget:
                recommendations.append((meal, drink, None))
                total_price += meal[1] + drink[1]

        # 식사 + 주류 추천
        for _ in range(alcohols):
            meal = random.choice(list(self.menu_data["식사 메뉴"].items()))
            alcohol = random.choice(list(self.menu_data["주류 메뉴"].items()))
            if total_price + meal[1] + alcohol[1] <= budget:
                recommendations.append((meal, None, alcohol))
                total_price += meal[1] + alcohol[1]

        # 식사만 추천
        for _ in range(people - drinks - alcohols):
            meal = random.choice(list(self.menu_data["식사 메뉴"].items()))
            if total_price + meal[1] <= budget:
                recommendations.append((meal, None, None))
                total_price += meal[1]

        return recommendations, total_price

class BistroProgram:
    def __init__(self):
        self.bistro = BistroMenu()

    def run(self):
        print("\n\U0001F374 비스트로사랑방 메뉴 추천 프로그램 시작! \U0001F37A")
        people = int(input("전체 인원을 입력하세요: "))
        drinks = int(input("음료와 함께할 사람 수: "))
        alcohols = int(input("주류와 함께할 사람 수: "))
        budget = int(input("예산을 입력하세요 (원): "))

        if drinks + alcohols > people:
            print("⚠️ 음료와 주류 인원 합은 전체 인원을 초과할 수 없습니다.")
            return

        # 메뉴 추천
        recommendations, total_price = self.bistro.recommend_menu(budget, people, drinks, alcohols)

        # 결과 출력
        print("\n추천 메뉴:")
        for i, (meal, drink, alcohol) in enumerate(recommendations, 1):
            if drink:
                print(f"{i}. {meal[0]} + {drink[0]} (총 {meal[1] + drink[1]}원)")
            elif alcohol:
                print(f"{i}. {meal[0]} + {alcohol[0]} (총 {meal[1] + alcohol[1]}원)")
            else:
                print(f"{i}. {meal[0]} (총 {meal[1]}원)")

        print(f"\n총 가격: {total_price}원")

if __name__ == "__main__":
    program = BistroProgram()
    program.run()
