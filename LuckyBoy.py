import random

def lucky_boy():
    print("택시비 정산 프로그램: 럭키 보이")
    print("사람 이름과 택시비를 입력하세요. (입력을 종료하려면 빈 줄을 입력)")

    # 사람 이름과 택시비 입력 받기
    people = []
    while True:
        name = input("이름: ")
        if not name:
            break
        try:
            fare = float(input(f"{name}의 택시비: "))
            people.append((name, fare))
        except ValueError:
            print("잘못된 입력입니다. 숫자로 입력해주세요.")

    # 입력된 정보가 없으면 종료
    if not people:
        print("입력된 사람이 없습니다. 프로그램을 종료합니다.")
        return

    # 총 택시비 계산
    total_fare = sum(fare for _, fare in people)

    # 랜덤으로 1명 선택
    lucky_person = random.choice(people)

    # 나눌 금액 계산 (럭키 보이는 총합의 1/n 금액 면제)
    remaining_people = [person for person in people if person != lucky_person]
    per_person_share = round(total_fare / len(remaining_people), -1)  # 1/n 금액 반올림

    # 결과 출력
    print("\n결과:")
    print(f"총 택시비: {format(int(round(total_fare, -1)), ',')}원")
    print(f"오늘의 럭키 보이! : {lucky_person[0]}! 택시비 면제! ")
    print(f"나머지 인원의 금액: {format(int(per_person_share), ',')}원")

if __name__ == "__main__":
    lucky_boy()
