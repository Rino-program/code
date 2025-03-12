import requests
from bs4 import BeautifulSoup

# 指定されたURL
url = 'https://netroom.oz96.com/?r=221971'

# HTTPリクエストを送信してHTMLを取得
response = requests.get(url)
html_content = response.content

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')

# チャットの内容を取得するためのセレクタを指定
# 以下のセレクタは例です。実際のHTMLを確認して適切なものに置き換えてください。
chat_selector = '.chat-message'  # チャットメッセージのクラスやタグを指定
timestamp_selector = '.chat-timestamp'  # タイムスタンプのクラスやタグを指定
user_selector = '.chat-user'  # ユーザー名のクラスやタグを指定

# チャット内容を格納するリスト
chat_data = []

# チャットメッセージをループして取得
for chat in soup.select(chat_selector):
    timestamp = chat.select_one(timestamp_selector).get_text(strip=True)
    user = chat.select_one(user_selector).get_text(strip=True)
    message = chat.get_text(strip=True)
    
    # チャットデータを辞書形式で格納
    chat_data.append({
        'timestamp': timestamp,
        'user': user,
        'message': message
    })

# 取得したチャット内容を出力
for chat in chat_data:
    print(f"{chat['timestamp']} - {chat['user']}: {chat['message']}")
