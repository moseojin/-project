import customtkinter as ctk
import random

class TaxiFareCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("택시비 정산: 럭키 보이")
        self.root.geometry("600x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.people = []
        self.total_fare = 0
        self.lucky_person = None
        self.per_person_share = 0

        self.create_widgets()

    def create_widgets(self):
        # 제목
        self.title_label = ctk.CTkLabel(self.root, text="택시비 정산 프로그램: 럭키 보이", font=("Arial", 20, "bold"), text_color="#32CD32")
        self.title_label.pack(pady=20)

        # 이름과 택시비 입력 프레임
        self.input_frame = ctk.CTkFrame(self.root)
        self.input_frame.pack(pady=10)

        self.name_label = ctk.CTkLabel(self.input_frame, text="이름:", font=("Arial", 14))
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ctk.CTkEntry(self.input_frame, width=200)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.fare_label = ctk.CTkLabel(self.input_frame, text="택시비:", font=("Arial", 14))
        self.fare_label.grid(row=1, column=0, padx=5, pady=5)
        self.fare_entry = ctk.CTkEntry(self.input_frame, width=200)
        self.fare_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = ctk.CTkButton(self.input_frame, text="추가", command=self.add_person)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # 리스트와 결과 출력 프레임
        self.result_frame = ctk.CTkFrame(self.root)
        self.result_frame.pack(pady=10)

        self.result_text = ctk.CTkTextbox(self.result_frame, height=150, width=400, font=("Arial", 12))
        self.result_text.pack(pady=10)

        # 버튼
        self.calculate_button = ctk.CTkButton(self.root, text="정산 시작", command=self.run_calculation, fg_color="#2E8B57")
        self.calculate_button.pack(pady=10)

        self.clear_button = ctk.CTkButton(self.root, text="초기화", command=self.clear_all)
        self.clear_button.pack(pady=5)

    def add_person(self):
        name = self.name_entry.get().strip()
        fare = self.fare_entry.get().strip()

        if not name or not fare:
            ctk.CTkMessagebox.show_error(title="입력 오류", message="이름과 택시비를 모두 입력해주세요.")
            return

        try:
            fare = float(fare)
            self.people.append((name, fare))
            self.result_text.insert("end", f"{name}: {fare:.0f}원\n")
            self.name_entry.delete(0, "end")
            self.fare_entry.delete(0, "end")
        except ValueError:
            ctk.CTkMessagebox.show_error(title="입력 오류", message="택시비는 숫자로 입력해주세요.")

    def run_calculation(self):
        if not self.people:
            ctk.CTkMessagebox.show_error(title="오류", message="입력된 사람이 없습니다.")
            return

        self.total_fare = sum(fare for _, fare in self.people)
        self.lucky_person = random.choice(self.people)
        remaining_people = [person for person in self.people if person != self.lucky_person]

        if remaining_people:
            self.per_person_share = round(self.total_fare / len(remaining_people), -1)
        else:
            self.per_person_share = 0

        result_message = (
            f"총 택시비: {int(round(self.total_fare, -1)):,}원\n"
            f"오늘의 럭키 보이: {self.lucky_person[0]} (택시비 면제!)\n"
            f"나머지 인원: {int(self.per_person_share):,}원씩 부담\n"
        )
        self.result_text.insert("end", f"\n{result_message}")

    def clear_all(self):
        self.people.clear()
        self.result_text.delete("1.0", "end")
        self.name_entry.delete(0, "end")
        self.fare_entry.delete(0, "end")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    app = TaxiFareCalculatorApp(root)
    root.mainloop()
