import json
import os
from datetime import datetime
from google.colab import drive

# === 1. Google Driveをマウント ===
drive.mount('/content/drive')

# === 2. 保存先フォルダ・ファイル名 ===
folder_path = '/content/drive/My Drive/SchoolManager'
lessons_file = os.path.join(folder_path, 'lessons.json')  # 授業データ
schedule_file = os.path.join(folder_path, 'schedule.json')  # 授業日程データ

# フォルダが存在しない場合は作成
os.makedirs(folder_path, exist_ok=True)

class LessonManager:
    def __init__(self, lessons_file, schedule_file):
        self.lessons_file = lessons_file
        self.schedule_file = schedule_file
        self.lessons = self.load_data(lessons_file)
        self.schedule = self.load_data(schedule_file)

    def load_data(self, file_path):
        """JSONファイルからデータを読み込む"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, file_path, data):
        """データをJSONファイルに保存する"""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"データが{file_path}に保存されました。")

    def add_schedule_based_lessons(self):
        """授業日程に基づいてスケジュールを作成"""
        date = input("日付を入力してください（例: 2025-05-08）: ")
        try:
            day_of_week = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"][
                datetime.strptime(date, "%Y-%m-%d").weekday()
            ]
        except ValueError:
            print("日付の形式が正しくありません。")
            return

        if day_of_week in self.schedule:
            if date not in self.lessons:
                self.lessons[date] = {}
            for i, subject in enumerate(self.schedule[day_of_week], start=1):
                time = f"{i}時間目"
                if time not in self.lessons[date]:
                    self.lessons[date][time] = {
                        "subject": subject,
                        "materials": [],
                        "homework": []
                    }
            print(f"{date}のスケジュールを授業日程から作成しました。")
        else:
            print(f"{day_of_week}の授業日程が存在しません。")

    def display_schedule(self):
        """スケジュールを表示する"""
        if not self.lessons:
            print("スケジュールは空です。")
        else:
            for date, day_schedule in self.lessons.items():
                print(f"=== {date} ===")
                for time, details in day_schedule.items():
                    print(f"{time}: {details['subject']}")
                    print(f"  持ち物: {', '.join(details['materials'])}")
                    print(f"  提出物: {', '.join(details['homework'])}")
                    print("-" * 20)

    def display_timetable(self):
        """授業日程を表示する"""
        if not self.schedule:
            print("授業日程がまだ設定されていません。")
        else:
            for day, subjects in self.schedule.items():
                print(f"=== {day} ===")
                for i, subject in enumerate(subjects, start=1):
                    print(f"{i}時間目: {subject}")
                print("-" * 20)

def main():
    manager = LessonManager(lessons_file, schedule_file)

    # 初回実行時に授業日程がない場合、サンプルデータを作成
    if not manager.schedule:
        manager.schedule = {
            "月曜日": ["現代の国語", "数学I", "論評I", "情報I", "化学基礎", "公共"],
            "火曜日": ["英コミュI", "情報I", "生物基礎", "探究", "数学I", "言語文化"],
            "水曜日": ["数学A", "現代の国語", "生物基礎", "英コミュI", "実用英語(会話)", "LT"],
            "木曜日": ["保険", "言語文化", "実用英語(文法)", "音楽", "論表I", "化学基礎"],
            "金曜日": ["公共", "英コミュI", "体育", "体育", "数学I", "数学A"]
        }
        manager.save_data(schedule_file, manager.schedule)

    while True:
        print("\n=== メニュー ===")
        print("1. 授業日程に基づいてスケジュールを作成")
        print("2. スケジュールを表示")
        print("3. 授業日程を表示")
        print("4. 保存して終了")
        choice = input("操作を選んでください (1-4): ")

        if choice == "1":
            manager.add_schedule_based_lessons()
        elif choice == "2":
            manager.display_schedule()
        elif choice == "3":
            manager.display_timetable()
        elif choice == "4":
            manager.save_data(lessons_file, manager.lessons)
            print("プログラムを終了します。")
            break
        else:
            print("無効な選択です。もう一度入力してください。")

if __name__ == "__main__":
    main()