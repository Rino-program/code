import json
import requests

class LessonManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.lessons = self.load_data()

    def add_lesson(self, time, subject, materials, homework=None):
        """授業を追加"""
        self.lessons[time] = {
            "subject": subject,
            "materials": materials,
            "homework": homework
        }
        print(f"{time}の授業を追加しました: {subject}")

    def delete_lesson(self, time):
        """授業を削除"""
        if time in self.lessons:
            del self.lessons[time]
            print(f"{time}の授業を削除しました。")
        else:
            print(f"{time}の授業は存在しません。")

    def display_schedule(self):
        """スケジュールを表示"""
        if not self.lessons:
            print("スケジュールは空です。")
        for time, info in self.lessons.items():
            print(f"{time}: {info['subject']}")
            print(f"  持ち物: {', '.join(info['materials'])}")
            if info["homework"]:
                print(f"  提出物: {info['homework']}")
            print("-" * 20)

    def save_data(self):
        """データをJSONファイルに保存"""
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(self.lessons, file, indent=4, ensure_ascii=False)
        print(f"データを{self.data_file}に保存しました。")

    def load_data(self):
        """JSONファイルからデータを読み込む"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

class GitHubUploader:
    def __init__(self, token, repo, branch="main"):
        self.token = token
        self.repo = repo
        self.branch = branch
        self.api_url = f"https://api.github.com/repos/{repo}/contents/"

    def upload_file(self, file_path, github_path):
        """ファイルをGitHubにアップロード"""
        with open(file_path, 'rb') as file:
            content = file.read()
        base64_content = content.encode('base64').decode('utf-8')

        # リポジトリへのAPIリクエスト
        response = requests.put(
            self.api_url + github_path,
            headers={
                "Authorization": f"token {self.token}",
                "Content-Type": "application/json"
            },
            json={
                "message": f"Add {github_path}",
                "content": base64_content,
                "branch": self.branch
            }
        )

        if response.status_code == 201:
            print(f"{github_path} をGitHubにアップロードしました。")
        else:
            print(f"アップロードに失敗しました: {response.json()}")

# 使用例
if __name__ == "__main__":
    # 授業管理
    manager = LessonManager("lessons.json")
    manager.add_lesson("1時間目", "数学", ["教科書", "ノート", "筆記用具"], "宿題プリント")
    manager.display_schedule()
    manager.save_data()

    # GitHubアップロード
    token = "your_github_token_here"  # GitHubアクセストークン
    repo = "your_username/your_repository"  # リポジトリ名
    uploader = GitHubUploader(token, repo)
    uploader.upload_file("lesson_manager.py", "folder_name/lesson_manager.py")
    uploader.upload_file("lessons.json", "folder_name/lessons.json")