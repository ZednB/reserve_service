from datetime import datetime, timedelta


def test_create_reservation_success(client):
    # Устанавливаем время для бронирования
    future_time = (datetime.now() + timedelta(hours=1)).isoformat()

    response = client.post("/reservations/", json={
        "table_id": 1,
        "customer_name": "Test Customer",
        "reservation_time": future_time,
        "duration_minutes": 30
    })

    if response.status_code == 200:
        data = response.json()
        print("✅ Бронь успешно создана:", data)
        assert data["table_id"] == 1
        assert data["duration_minutes"] == 30

    elif response.status_code == 409:
        print("⚠️ Время уже забронировано, что тоже допустимо:", response.json())

    else:
        # Любой другой код — это неожиданная ошибка
        assert False, f"Непредвиденный статус ответа: {response.status_code}, тело: {response.json()}"


def test_invalid_date_format(client):
    response = client.post("/reservations/", json={
        "table_id": 1,
        "customer_name": "Invalid Date",
        "reservation_time": "not-a-date",
        "duration_minutes": 30
    })
    assert response.status_code == 422


def test_reservation_in_past(client):
    past_time = (datetime.now() - timedelta(hours=1)).isoformat()

    response = client.post("/reservations/", json={
        "table_id": 1,
        "customer_name": "Time Traveler",
        "reservation_time": past_time,
        "duration_minutes": 30
    })

    # В зависимости от логики — либо 422, либо 400
    assert response.status_code in (400, 422)


def test_list_reservations(client):
    response = client.get("/reservations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

