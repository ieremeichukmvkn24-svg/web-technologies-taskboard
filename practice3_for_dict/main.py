"""Практична №3: цикл for та словники dict."""

tasks: dict[int, dict[str, object]] = {
    1: {"name": "HTML", "status": "done", "hours": 2},
    2: {"name": "CSS", "status": "doing", "hours": 3},
    3: {"name": "JavaScript", "status": "todo", "hours": 4},
    4: {"name": "Git", "status": "done", "hours": 1},
}


def count_by_status(items: dict[int, dict[str, object]]) -> dict[str, int]:
    result: dict[str, int] = {}
    for task in items.values():
        status = str(task["status"])
        result[status] = result.get(status, 0) + 1
    return result


def total_hours(items: dict[int, dict[str, object]]) -> int:
    result = 0
    for task in items.values():
        result += int(task["hours"])
    return result


def task_names(items: dict[int, dict[str, object]], status: str) -> list[str]:
    found: list[str] = []
    for task in items.values():
        if task["status"] == status:
            found.append(str(task["name"]))
    return found


def main() -> None:
    print("=== Практична 3: for і dict ===")
    for key, task in tasks.items():
        print(f'{key}: {task["name"]} | {task["status"]} | {task["hours"]} год')
    print("\nКількість за статусом:")
    for status, amount in count_by_status(tasks).items():
        print(f"{status}: {amount}")
    print("Годин загалом:", total_hours(tasks))
    print("Виконані:", ", ".join(task_names(tasks, "done")))


if __name__ == '__main__':
    main()
