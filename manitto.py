import random

def select_manitto(participants, my_name):
    # 본인을 제외한 리스트 생성
    others = [name for name in participants if name != my_name]
    if not others:
        return None
    # 랜덤으로 마니또 선정
    return random.choice(others)

def select_mission():
    # 미션 리스트
    missions = [
        "하루 동안 칭찬 3개를 적어서 편지로 전달하기",
        "좋아하는 간식을 몰래 주머니에 두기",
        "웃긴 동영상 보내기로 하루 한 번 웃음 선물하기",
        "놀고있을 때, 친구 대신 간식을 사다 주기",
        "상대방을 위해 깜짝 이벤트 준비하기",
        "특정 색깔 옷 입고 사진 찍어 보내기",
        "오늘 친구가 먹고 싶어 하는 음식을 말하게 만들기",
        "웃음을 터트리게 하는 행동을 하기",
        "친구를 3번 이상 웃기기",
        "이름 대신 별명으로 부르기",
    ]
    # 랜덤으로 미션 선택
    return random.choice(missions)

def main():
    print("🎉 마니또 미션 프로그램 🎉")

    # 참가자 입력
    participants = input("참가자 이름을 쉼표로 구분해 입력하세요 (예: 철수, 영희, 민수): ").split(",")
    participants = [name.strip() for name in participants]

    # 본인 이름 입력
    my_name = input("본인의 이름을 입력하세요: ").strip()

    if my_name not in participants:
        print("⚠️ 본인의 이름이 참가자 명단에 없습니다. 다시 확인해주세요.")
        return

    # 마니또 선정
    manitto = select_manitto(participants, my_name)
    if not manitto:
        print("⚠️ 참가자가 본인 한 명뿐입니다. 마니또를 설정할 수 없습니다.")
        return

    # 미션 선정
    mission = select_mission()

    # 결과 출력
    print(f"\n✨ 당신의 마니또는 {manitto}입니다! ✨")
    print(f"🎯 오늘의 미션: {mission}")

if __name__ == "__main__":
    main()
