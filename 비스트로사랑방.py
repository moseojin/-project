import random

# 비스트로사랑방 메뉴 데이터
menu_data = {
    "식사 메뉴": {
        "감자 베이컨 크림 뇨끼": 16000,
        "4가지 고추 정통 까르보나라": 14000,
        "3색 파스타": 16000,
        "부라따 치즈 토마토 파스타": 16000,
        "앤초비 주키니 오일 파스타": 14000,
        "수비드 문어 레몬버터 파스타": 15000,
        "라자냐": 17000,
        "오늘의 파스타 & 리조또": 16000,
        "새우 바질 리조또": 16000,
        "포르치니 버섯 리조또": 14000,
        "라구소스 사프란 리조또": 15000,
        "치킨 로제 리조또": 14000,
    },
    "음료 메뉴": {
        "콜라": 3000,
        "사이다": 3000,
        "제로콜라": 3000,
        "오렌지 주스": 4000,
        "복숭아 아이스티": 4000,
        "아메리카노": 4000,
        "자몽 에이드": 4000,
        "레몬 에이드": 4000,
        "와인 에이드": 4000,
        "체리 에이드": 4000,
    },
    "주류 메뉴": {
        "하이볼": 7000,
        "상그리아": 7000,
        "블루 와인 칵테일": 7000,
        "하우스 와인": 7000,
        "스텔라 아르투아": 6500,
        "서머스비 애플사이다": 6500,
        "레페 브라운 흑맥주": 6500,
    }
}

# 추천 함수
def recommend_menu(budget, people, with_drink, with_alcohol):
    recommendations = []
    total_price = 0

    for _ in range(with_drink):
        while True:
            # 1인 식사 메뉴와 음료 선택
            meal = random.choice(list(menu_data["식사 메뉴"].items()))
            drink = random.choice(list(menu_data["음료 메뉴"].items()))
            total = meal[1] + drink[1]
            if total_price + total <= budget:
                recommendations.append((meal, drink, None))
                total_price += total
                break

    for _ in range(with_alcohol):
        while True:
            # 1인 식사 메뉴와 주류 선택
            meal = random.choice(list(menu_data["식사 메뉴"].items()))
            alcohol = random.choice(list(menu_data["주류 메뉴"].items()))
            total = meal[1] + alcohol[1]
            if total_price + total <= budget:
                recommendations.append((meal, None, alcohol))
                total_price += total
                break

    for _ in range(people - with_drink - with_alcohol):
        while True:
            # 1인 식사 메뉴만 선택
            meal = random.choice(list(menu_data["식사 메뉴"].items()))
            if total_price + meal[1] <= budget:
                recommendations.append((meal, None, None))
                total_price += meal[1]
                break

    return recommendations, total_price

# 예산 검증 함수
def is_budget_sufficient(budget, people, with_drink, with_alcohol):
    # 최소 가격 계산 (가장 저렴한 식사 메뉴 + 음료/주류 조합)
    min_meal_price = min(menu_data["식사 메뉴"].values())
    min_drink_price = min(menu_data["음료 메뉴"].values())
    min_alcohol_price = min(menu_data["주류 메뉴"].values())
    required_budget = (with_drink * (min_meal_price + min_drink_price)) + (with_alcohol * (min_meal_price + min_alcohol_price)) + ((people - with_drink - with_alcohol) * min_meal_price)
    return budget >= required_budget

# 사용자 입력 받기
def main():
    print("\n\U0001F374 비스트로사랑방 메뉴 추천 프로그램 \U0001F37A")
    while True:
        try:
            # 전체 인원 입력
            people = int(input("전체 식사 인원을 입력하세요 (명): "))
            with_drink = int(input("음료와 함께 먹을 사람의 수를 입력하세요 (명): "))
            with_alcohol = int(input("주류와 함께 먹을 사람의 수를 입력하세요 (명): "))

            if with_drink + with_alcohol > people:
                print("\u26A0\ufe0f 음료와 주류 인원의 합은 전체 식사 인원 수를 초과할 수 없습니다.")
                continue

            while True:
                # 예산 입력
                budget = int(input("예산을 입력하세요 (원): "))

                # 예산 검증
                if not is_budget_sufficient(budget, people, with_drink, with_alcohol):
                    print("\n\u26A0\ufe0f 현재 예산으로는 모든 사람의 식사를 추천할 수 없습니다. 예산을 늘려주세요. \u26A0\ufe0f")
                    continue

                # 추천 메뉴 계산
                recommendations, total_price = recommend_menu(budget, people, with_drink, with_alcohol)

                # 결과 출력
                print("\n추천 메뉴 조합:")
                for i, (meal, drink, alcohol) in enumerate(recommendations, 1):
                    if drink:
                        print(f"{i}. {meal[0]} ({meal[1]}원) + {drink[0]} ({drink[1]}원)")
                    elif alcohol:
                        print(f"{i}. {meal[0]} ({meal[1]}원) + {alcohol[0]} ({alcohol[1]}원)")
                    else:
                        print(f"{i}. {meal[0]} ({meal[1]}원)")

                print(f"\n\U0001F4B0 총 가격: {total_price}원 (예산: {budget}원)")
                return
        except ValueError:
            print("\u26A0\ufe0f 잘못된 입력입니다. 숫자를 입력해주세요.")

# 실행
if __name__ == "__main__":
    main()
