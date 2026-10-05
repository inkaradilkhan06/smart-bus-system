
from datetime import datetime

# Автобус жолақысы
FARE = 120

# Жолаушылар
passengers = {
    1: {
        "name": "Adilkhan Inkar",
        "face_id": "FACE_VECTOR_001"
    },
    2: {
        "name": "Samatqyzy Rayana",
        "face_id": "FACE_VECTOR_002"
    }
}


def recognize_face(face_id):
    """AI камера арқылы жолаушыны анықтау"""

    for passenger_id, passenger in passengers.items():
        if passenger["face_id"] == face_id:
            return passenger_id, passenger

    return None, None


def make_payment(passenger_id, passenger):
    """Жол ақысын автоматты төлеу"""

    payment = {
        "passenger_id": passenger_id,
        "name": passenger["name"],
        "fare": FARE,
        "status": "PAID",
        "time": datetime.now()
    }

    return payment


print("================================")
print("      AI FACEPAY BUS")
print("================================")

face = input("Face ID енгізіңіз: ")

passenger_id, passenger = recognize_face(face)

if passenger:

    print("\n✅ Жолаушы танылды")
    print("Жолаушы:", passenger["name"])

    payment = make_payment(passenger_id, passenger)

    print("\n💳 Автоматты төлем")
    print("Сома:", payment["fare"], "₸")
    print("Статус:", payment["status"])
    print("Уақыт:", payment["time"])

    print("\n🚌 Сапар жалғасады")

else:

    print("\n❌ Жолаушы танылмады")
    print("Төлем орындалмады")
