"""Практична №1: input/print, логічні та умовні оператори."""

def validate_task(title: str, minutes: int, priority: int) -> tuple[bool, str]:
    if not title.strip():
        return False, "Назва не може бути порожньою"
    if minutes <= 0 or minutes > 1440:
        return False, "Час має бути від 1 до 1440 хвилин"
    if priority < 1 or priority > 3:
        return False, "Пріоритет має бути від 1 до 3"
    return True, "Коректні дані"


def get_recommendation(minutes: int, priority: int, urgent: bool) -> str:
    if urgent and priority == 3:
        return "Виконати зараз — термінове завдання з високим пріоритетом"
    elif priority == 3 or minutes >= 180:
        return "Почати сьогодні"
    elif priority == 2 and minutes > 30:
        return "Запланувати на найближчий час"
    return "Можна виконати пізніше"


def main() -> None:
    print("=== Практична 1: Параметри завдання TaskBoard ===")
    title = input("Назва завдання: ")
    try:
        minutes = int(input("Час у хвилинах: "))
        priority = int(input("Пріоритет 1-3: "))
        urgent_answer = input("Термінове завдання? так/ні: ").strip().lower()
        urgent = urgent_answer in ("так", "т", "yes", "y")
    except ValueError:
        print("Помилка: потрібно вводити цілі числа")
        return
    valid, message = validate_task(title, minutes, priority)
    if not valid:
        print("Помилка:", message)
    else:
        print("Назва:", title)
        print("Терміновість:", "так" if urgent else "ні")
        print("Рекомендація:", get_recommendation(minutes, priority, urgent))


if __name__ == "__main__":
    main()
