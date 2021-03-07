from app import client

# Тест для GET rout
def test_get():
    res = client.get('/tutorials')
    # Проверим статус при запросе
    assert res.status_code == 200
    # Проверим, что в полученном json есть список
    assert len(res.get_json()) == 2
    # Проверим, что id первой записи == 1
    assert res.get_json()[0]['id'] == 1

# Тест для POST rout
def test_post():
    # Передаем данные
    data = {
        'id': 3,
        'title': 'Unit tests',
        'description': 'Pytest tutorials'
    }

    res = client.post('/tutorials', json=data)
    # Проверим статус при запросе
    assert res.status_code == 200
    # Проверим, что в полученном json есть список
    assert len(res.get_json()) == 3
    # Проверим, что последний элемент в списке это наш добавленный словарь data
    assert res.get_json()[-1]['title'] == data['title']
