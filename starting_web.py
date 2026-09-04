from flask import Flask, render_template

# Создаём приложение
app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Страница "Резюме"
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Страница "Услуги"
@app.route('/services')
def services():
    return render_template('services.html')

# Страница "Контакты"
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Страница "Коучинг"
@app.route('/coaching')
def coaching():
    return render_template('coaching.html')

# Страница "Психология"
@app.route('/psych')
def psych():
    return render_template('psych.html')

# Страница "Проекты"
@app.route('/project')
def project():
    return render_template('project.html')

# Страница "Образование"
@app.route('/education')
def education():
    return render_template('education.html')

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True, port=5000)