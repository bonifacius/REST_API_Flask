from flask import Flask, jsonify, request

app = Flask(__name__)

# Тестовый клиент Flask
client = app.test_client()

tutorials = [
    {
        'title': 'Video #1. Intro',
        'description': 'GET, POST routes'
    },
    {
        'title': 'Video #2. More features',
        'description': 'GET, POST routes'

    }
]

@app.route('/')
def index():
	return "Hello!"

# Создаем роут прописываем метод чтобы возвращать список tutorials
@app.route('/tutorials', methods=['GET'])
def get_list():
    # Чтобы ответ сервера корректо отображался, импортируем jsonify
    # И получаем данные из tutorials в формате json
    return jsonify(tutorials)

# Напишем роут для подзапросов, с помощью которого будет обновляться информация на сервере путем добавления нового элемента
# 1. импортируем request (будем получать json который мы отправили на сервер
# 2. Испоьзуем тестовый client Flask.

@app.route('/tutorials', methods=['POST'])
def update_list():
    # 3. Получаем данные из request
    # 4. Добавляем их в tutorials
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)

# 5. Протестируем роут в консоли питон.
# from app import app, client
# res = client.get('/tutorials')
# res.get_json()
# Должны получить вывод данных

# 6. Теперь попробуем добавить новые данные с помощью подзапроса
# res = client.post('/tutorials', json={'title': 'Video #4. Intro', 'descriprion': 'Unit tests'})
# и проверяем что получили
# res.status_code
# res.get_json()



if __name__ == '__main__':
    app.run(debug=True)

