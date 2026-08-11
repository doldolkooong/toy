import random
import tkinter as tk
import random
import tkinter as tk
from tkinter import messagebox


class RockPaperScissorsApp:
    CHOICES = ("가위", "바위", "보")
    WIN = {
        "가위": "보",
        "바위": "가위",
        "보": "바위"
    }

    def __init__(self, root):
        self.root = root
        self.root.title("가위바위보 3선승제")
        self.root.geometry("500x430")
        self.root.resizable(False, False)

        self.user_win = 0
        self.computer_win = 0
        self.count = 0
        self.game_started = False

        tk.Label(
            root,
            text="가위바위보 게임 3선승제",
            font=("맑은 고딕", 20, "bold")
        ).pack(pady=(25, 10))

        self.score_label = tk.Label(
            root,
            text="새 게임 시작 버튼을 눌러주세요.",
            font=("맑은 고딕", 14, "bold")
        )
        self.score_label.pack(pady=5)

        self.result_label = tk.Label(
            root,
            text="",
            font=("맑은 고딕", 13),
            height=4,
            justify="center"
        )
        self.result_label.pack(pady=10)

        # 새 게임 시작 버튼
        self.start_button = tk.Button(
            root,
            text="새 게임 시작",
            font=("맑은 고딕", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            width=18,
            height=2,
            command=self.start_game
        )
        self.start_button.pack(pady=8)

        # 가위바위보 버튼 영역
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.choice_buttons = []

        for choice, icon in zip(self.CHOICES, ("✌", "✊", "✋")):
            button = tk.Button(
                button_frame,
                text=f"{icon}\n{choice}",
                font=("맑은 고딕", 16, "bold"),
                width=8,
                height=3,
                state="disabled",
                command=lambda selected=choice: self.play(selected)
            )
            button.pack(side="left", padx=7)
            self.choice_buttons.append(button)

    def start_game(self):
        """새 게임을 시작하고 점수를 초기화합니다."""
        self.user_win = 0
        self.computer_win = 0
        self.count = 0
        self.game_started = True

        self.score_label.config(
            text="현재 스코어  |  사용자 0 : 0 컴퓨터"
        )
        self.result_label.config(
            text="가위, 바위, 보 중 하나를 선택하세요!"
        )

        for button in self.choice_buttons:
            button.config(state="normal")

        self.start_button.config(text="게임 다시 시작")

    def play(self, user_choice):
        if not self.game_started:
            return

        computer_choice = random.choice(self.CHOICES)
        self.count += 1

        if user_choice == computer_choice:
            outcome = "비겼습니다!"
        elif self.WIN[user_choice] == computer_choice:
            outcome = "이겼습니다!"
            self.user_win += 1
        else:
            outcome = "졌습니다ㅜㅜ"
            self.computer_win += 1

        self.result_label.config(
            text=f"사용자: {user_choice}     컴퓨터: {computer_choice}\n\n{outcome}"
        )

        self.score_label.config(
            text=f"현재 스코어  |  사용자 {self.user_win} : {self.computer_win} 컴퓨터"
        )

        # 3선승제 종료 확인
        if self.user_win == 3 or self.computer_win == 3:
            self.end_game()

    def end_game(self):
        self.game_started = False

        for button in self.choice_buttons:
            button.config(state="disabled")

        if self.user_win == 3:
            message = f"🎉 최종 승리를 축하합니다!\n총 진행 횟수: {self.count}"
        else:
            message = "컴퓨터가 최종 승리했습니다ㅜㅜ"

        self.result_label.config(text=message)
        self.start_button.config(text="새 게임 시작")

        messagebox.showinfo("게임 종료", message)


if __name__ == "__main__":
    window = tk.Tk()
    RockPaperScissorsApp(window)
    window.mainloop()