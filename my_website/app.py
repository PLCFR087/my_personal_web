from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "这是小刘的web站点，可用于存放个人文件及软件代码。"

# 仅仅本地电脑运行才会执行，Vercel线上完全忽略这一段
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
