"""Практична 4 (def): вправи з функціями Python.

Увага: точне індивідуальне завдання недоступне; це навчальна реалізація
за загальною темою «Практична 4. def».
"""

from collections.abc import Iterable


def check_name(name: str) -> bool:
    """Перевіряє, чи назва завдання не порожня й не надто коротка."""
    return isinstance(name, str) and len(name.strip()) >= 2


def get_priority_name(priority: int) -> str:
    """Перекладає числовий пріоритет у текст."""
    priorities = {1: "низький", 2: "середній", 3: "високий"}
    if priority not in priorities:
        raise ValueError("Пріоритет має бути від 1 до 3")
    return priorities[priority]


def total_hours(hours: Iterable[float]) -> float:
    """Підраховує суму витрачених годин."""
    values = list(hours)
    if any(value < 0 for value in values):
        raise ValueError("Години не можуть бути від’ємними")
    return sum(values)


def completion_percent(completed: int, total: int) -> float:
    """Розраховує частку виконаних задач у відсотках."""
    if total < 0 or completed < 0 or completed > total:
        raise ValueError("Некоректна кількість задач")
    return round(completed / total * 100, 1) if total else 0.0


def task_summary(title: str, priority: int, completed: bool = False) -> str:
    """Формує текстовий опис задачі з параметром за замовчуванням."""
    if not check_name(title):
        raise ValueError("Назва має містити мінімум 2 символи")
    state = "виконано" if completed else "в роботі"
    return f"{title.strip()} | пріоритет: {get_priority_name(priority)} | {state}"


def main() -> None:
    tasks = ["HTML", "CSS", "JavaScript", "Git"]
    print("Практична №4 — Python, функції def")
    print("Кількість задач:", len(tasks))
    print("Перевірка назви:", check_name("TaskBoard"))
    print("Пріоритет 3:", get_priority_name(3))
    print("Витрачено годин:", total_hours([1.5, 2, 0.5]))
    print("Прогрес:", completion_percent(3, 4), "%")
    print("Опис:", task_summary("Оформити сайт", 2, True))


if __name__ == "__main__":
    main()
