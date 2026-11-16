# Веб технології — практичні №1–10

**Автор:** Єремейчук Максим, КН-3/1.  
**Предмет:** Веб технології, 2026.

## Практичні роботи

| № | Тема | Файли |
|---|---|---|
| 1 | Python: input, print, умови | `practice1_input_conditions/` |
| 2 | Python: while та list | `practice2_while_list/` |
| 3 | Python: for та dict | `practice3_for_dict/` |
| 4 | Python: функції def (виправлення) | `practice4_def/` |
| 5 | Розробка вебсторінки | `index.html` |
| 6 | HTML та Git | `index.html`, `about.html`, `docs/git-notes.md` |
| 7 | GitHub README | цей `README.md` |
| 8 | HTML | `index.html`, `about.html`, `docs/links.html` |
| 9 | CSS | `css/style.css` |
| 10 | JavaScript | `js/app.js` |

## TaskBoard

Адаптивний навчальний сайт-дошка завдань на HTML, CSS та JavaScript. Є три статуси задач, фільтри, пошук, створення, редагування, видалення і збереження даних у `localStorage`. Для відкриття скористайся `index.html` або Live Server у VS Code.

## Перевірка

```bash
python -m unittest discover -s practice1_input_conditions
python -m unittest discover -s practice2_while_list
python -m unittest discover -s practice3_for_dict
python -m unittest discover -s practice4_def
node --check js/app.js
python scripts/verify_site.py
```

Роботи підготовлено за доступними навчальними матеріалами. Вимоги конкретних завдань у Classroom потрібно звірити; наявність файлів на GitHub сама по собі не означає їх здачу.
