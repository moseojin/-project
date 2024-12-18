import customtkinter as ctk
import tkinter as tk
import random
import math

# 장소 목록
places = [
    "PC방", "볼링장", "노래방", "보드게임 카페", "공방", "찜질방/사우나", "스크린 골프", "고양이 카페", "강아지 카페페"
    "스크린 야구", "탁구장", "VR 게임방", "방탈출 카페", "팝업 스토어", "메이드 카페", "공원에서 산책", "클럽"
    "포켓볼/당구장", "롤러스케이트장", "도서관", "오락실", "영화관", "실내 낚시터", "만화 카페", "그림 카페"
]

# GUI 애플리케이션 클래스
class RouletteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("시각적 룰렛")
        self.geometry("500x600")

        # Canvas 설정 (룰렛 화면)
        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack(pady=20)

        # 돌리기 버튼
        self.spin_button = ctk.CTkButton(self, text="룰렛 돌리기", command=self.spin_roulette)
        self.spin_button.pack(pady=10)

        # 결과 출력 라벨
        self.result_label = ctk.CTkLabel(self, text="룰렛을 돌려보세요!", font=("Arial", 18))
        self.result_label.pack(pady=10)

        # 회전 상태 변수
        self.current_angle = 0
        self.is_spinning = False
        self.selected_place = None

    def draw_roulette(self, current_angle):
        """룰렛 그리기 (모션만 표시)"""
        self.canvas.delete("all")
        for i in range(len(places)):
            start_angle = 360 / len(places) * i + current_angle
            color = self.random_color(i)
            self.canvas.create_arc(
                20, 20, 380, 380, start=start_angle, extent=360 / len(places), fill=color, outline="black"
            )
        self.canvas.create_oval(190, 190, 210, 210, fill="red")

    def random_color(self, index):
        """각 섹터에 무작위 색상 지정"""
        colors = ["#FF9999", "#FFCC99", "#FFFF99", "#99FF99", "#99FFFF", "#9999FF", "#FF99FF"]
        return colors[index % len(colors)]

    def spin_roulette(self):
        """룰렛을 회전시키는 함수"""
        if not self.is_spinning:
            self.is_spinning = True
            spin_time = random.randint(25, 45)  # 회전 시간 설정
            self.animate_spin(spin_time)

    def animate_spin(self, remaining):
        """룰렛 회전 애니메이션"""
        if remaining > 0:
            self.current_angle += 10  # 회전 각도 증가
            self.draw_roulette(self.current_angle)
            self.after(50, self.animate_spin, remaining - 1)
        else:
            self.is_spinning = False
            self.display_result()

    def display_result(self):
        """결과 표시"""
        segment_size = 360 / len(places)
        final_angle = (360 - (self.current_angle % 360)) % 360
        selected_index = int(final_angle // segment_size) % len(places)
        self.selected_place = places[selected_index]
        self.result_label.configure(text=f"오늘의 추천 장소 : {self.selected_place} !!")

# 애플리케이션 실행
if __name__ == "__main__":
    app = RouletteApp()
    app.mainloop()
