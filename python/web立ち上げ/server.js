const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.post('/submit', (req, res) => {
    const { name, message } = req.body;
    const data = `名前: ${name}\n文章: ${message}\n\n`;

    fs.appendFile(path.join(__dirname, 'data.txt'), data, (err) => {
        if (err) {
            console.error('データの保存中にエラーが発生しました:', err);
            res.status(500).json({ error: 'データの保存中にエラーが発生しました' });
        } else {
            res.status(200).json({ message: 'データが保存されました' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`サーバーがポート${PORT}で起動しました`);
});