from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    
    # データをCSVファイルに保存
    file_exists = os.path.isfile('survey_results.csv')
    with open('survey_results.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['名前', 'メールアドレス', 'フィードバック'])
        writer.writerow([name, email, feedback])
    
    return jsonify({"message": "データが送信されました"}), 200

if __name__ == '__main__':
    app.run(debug=True)