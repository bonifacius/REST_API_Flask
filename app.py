from flask import Flask, jsonify, request

app = Flask(__name__)

# Тестовый клиент Flask
client = app.test_client()

tutorials = [
    {
        'id': 1,
        'title': 'Video #1. Intro',
        'description': 'GET, POST routes'
    },
    {
        'id': 2,
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

# Создаем новый роут для метода PUT
@app.route('/tutorials/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    # Что бы получиться элемент по его id воспользуемся конструкцией генератором
    # Он вернет элемент с соответствующим id или None
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    # Нужно получиться параметры которые переданы в запросе для изменения
    params = request.json
    # Проверяем был ди найден соответствующий элемент в списке прежде чем изменять его
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    item.update(params)
    # А в ответе мы вернем тот элемент списка который был изменен
    return item

# Протестируем роут в консоли питон.
# from app import client
# res = client.put('/tutorials/2', json={'description': 'PUT routes for editing'})
# res.status_code
# res.get_json()

# Создаем новый роут для метода DELETE
@app.route('/tutorials/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    # Получаем индекс элемента. Функция enumerate пронумеровывает словариб кортежи
    idx, _ = next((x for x in enumerate(tutorials) if x[1]['id'] == tutorial_id), (None, None))
    tutorials.pop(idx)
    return '', 204

# Протестируем роут в консоли питон.
# from app import client
# res = client.delete('/tutorials/1')
# res.status_code должен быть код - 204
# res = client.get('/tutorials')
# res.get_json()


if __name__ == '__main__':
    app.run(debug=True)

