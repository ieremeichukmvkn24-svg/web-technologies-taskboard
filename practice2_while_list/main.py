"""Практична №2: список та цикл while на прикладі TaskBoard."""

def add_task(tasks: list[str], name: str) -> bool:
    name = name.strip()
    if not name or name in tasks:
        return False
    tasks.append(name)
    return True


def remove_task(tasks: list[str], name: str) -> bool:
    if name not in tasks:
        return False
    tasks.remove(name)
    return True


def get_tasks(tasks: list[str]) -> str:
    if not tasks:
        return "Список завдань порожній"
    return "\n".join(f"{i}. {task}" for i, task in enumerate(tasks, 1))


def main() -> None:
    tasks: list[str] = ["HTML", "CSS", "JavaScript"]
    print("=== Практична 2: список завдань ===")
    while True:
        print("\n1 — додати; 2 — переглянути; 3 — видалити; 0 — вихід")
        cmd = input("Команда: ").strip()
        if cmd == "1":
            name = input("Введи назву: ")
            print("Додано" if add_task(tasks, name) else "Назва порожня або вже існує")
        elif cmd == "2":
            print(get_tasks(tasks))
        elif cmd == "3":
            name = input("Введи назву для видалення: ")
            print("Видалено" if remove_task(tasks, name) else "Такого завдання немає")
        elif cmd == "0":
            print("Завершення програми")
            break
        else:
            print("Невідома команда")


if __name__ == '__main__':
    main()
