from flask import Flask, render_template
app = Flask(__name__)
# 路由： 首页
@app.route('/')
def home():
    return render_template('index.html')
# 路由： 关于我（可以加其他东西）
@app.route('/about')
def about():
    return "这是小刘的web站点，可用存放个人文件及软件代码。"
# 启动服务
if __name__ == '__main__':
    app.run(debug=Flask, host='0.0.0.0', port=5000)