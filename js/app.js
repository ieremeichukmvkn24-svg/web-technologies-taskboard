"use strict";

// Практична 10: робота з DOM, подіями, формами, фільтрацією та localStorage.
(() => {
  const STORAGE_KEY = "taskboard-kn31-tasks-v1";
  const ALLOWED_STATUSES = ["todo", "doing", "done"];
  const ALLOWED_PRIORITIES = ["low", "medium", "high"];
  const labels = { high: "Високий", medium: "Середній", low: "Низький" };
  const initialTasks = [
    { id: "seed-1", title: "Повторити основи HTML", description: "Семантичні теги та навігація між сторінками", priority: "medium", status: "done", date: "" },
    { id: "seed-2", title: "Оформити головну сторінку", description: "Картки, відступи, адаптивна сітка", priority: "high", status: "doing", date: "" },
    { id: "seed-3", title: "Додати JavaScript", description: "Робота з подіями та збереження завдань", priority: "high", status: "todo", date: "" },
    { id: "seed-4", title: "Написати README", description: "Інструкція запуску та опис технологій", priority: "low", status: "todo", date: "" }
  ];

  const $ = selector => document.querySelector(selector);
  const dialog = $("#task-dialog");
  const form = $("#task-form");
  const message = $("#board-message");

  function validTask(raw) {
    return raw && typeof raw.id === "string" &&
      typeof raw.title === "string" && raw.title.trim().length >= 2 &&
      ALLOWED_STATUSES.includes(raw.status) &&
      ALLOWED_PRIORITIES.includes(raw.priority) &&
      typeof raw.description === "string" &&
      typeof raw.date === "string";
  }

  function loadTasks() {
    try {
      const saved = window.localStorage.getItem(STORAGE_KEY);
      if (saved === null) return initialTasks.map(task => ({ ...task }));
      const parsed = JSON.parse(saved);
      return Array.isArray(parsed) ? parsed.filter(validTask) : initialTasks.map(task => ({ ...task }));
    } catch (error) {
      console.warn("Не вдалося прочитати збережені завдання", error);
      return initialTasks.map(task => ({ ...task }));
    }
  }

  let tasks = loadTasks();

  function persist() {
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
    } catch (error) {
      message.textContent = "Не вдалося зберегти зміни. Перевір налаштування браузера.";
      console.warn("localStorage unavailable", error);
    }
  }

  function announce(text) { message.textContent = text; }

  function textElement(tag, className, content) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = content;
    return element;
  }

  function safeDate(value) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return "Без терміну";
    const parsed = new Date(`${value}T12:00:00`);
    if (Number.isNaN(parsed.valueOf())) return "Без терміну";
    return new Intl.DateTimeFormat("uk-UA", { day: "numeric", month: "short", year: "numeric" }).format(parsed);
  }

  function overdue(task) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(task.date) || task.status === "done") return false;
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, "0");
    const day = String(today.getDate()).padStart(2, "0");
    return task.date < `${year}-${month}-${day}`;
  }

  function taskCard(task) {
    const article = document.createElement("article");
    article.className = "task-card";
    article.draggable = true;
    article.dataset.id = task.id;
    article.tabIndex = 0;
    article.setAttribute("aria-label", `${task.title}, пріоритет ${labels[task.priority]}`);

    const top = textElement("div", "task-top", "");
    top.appendChild(textElement("span", `priority priority-${task.priority}`, labels[task.priority]));
    const editTop = textElement("button", "task-menu", "⋯ Змінити");
    editTop.type = "button";
    editTop.dataset.action = "edit";
    editTop.setAttribute("aria-label", `Редагувати ${task.title}`);
    top.appendChild(editTop);
    article.appendChild(top);
    article.appendChild(textElement("h4", "", task.title));
    article.appendChild(textElement("p", "task-description", task.description || "Без опису"));

    const bottom = textElement("div", "task-bottom", "");
    const date = textElement("span", overdue(task) ? "date-label date-overdue" : "date-label", safeDate(task.date));
    bottom.appendChild(date);
    const actions = textElement("div", "card-actions", "");
    const change = textElement("button", "small-action", "Змінити");
    change.type = "button";
    change.dataset.action = "edit";
    const remove = textElement("button", "small-action", "✕");
    remove.type = "button";
    remove.dataset.action = "delete";
    remove.setAttribute("aria-label", `Видалити ${task.title}`);
    actions.append(change, remove);
    bottom.appendChild(actions);
    article.appendChild(bottom);
    return article;
  }

  function render() {
    const search = $("#task-search").value.trim().toLocaleLowerCase("uk-UA");
    const priority = $("#priority-filter").value;
    const filtered = tasks.filter(task =>
      (priority === "all" || task.priority === priority) &&
      (task.title + " " + task.description).toLocaleLowerCase("uk-UA").includes(search));

    for (const status of ALLOWED_STATUSES) {
      const list = $(`#${status}-list`);
      list.replaceChildren();
      const data = filtered.filter(task => task.status === status);
      for (const task of data) list.appendChild(taskCard(task));
      if (!data.length) list.appendChild(textElement("p", "task-empty", "Тут поки немає завдань"));
    }

    const todo = tasks.filter(task => task.status === "todo").length;
    const doing = tasks.filter(task => task.status === "doing").length;
    const done = tasks.filter(task => task.status === "done").length;
    const percent = tasks.length ? Math.round(100 * done / tasks.length) : 0;
    $("#total-count").textContent = tasks.length;
    $("#progress-count").textContent = doing;
    $("#done-count").textContent = done;
    $("#percent-count").textContent = `${percent}%`;
    $("#todo-count").textContent = todo;
    $("#doing-count").textContent = doing;
    $("#done-column-count").textContent = done;
    $("#progress-fill").style.width = `${percent}%`;
    $("#progress-bar").setAttribute("aria-valuenow", String(percent));
    $("#clear-done").disabled = done === 0;
  }

  function openEditor(task = null) {
    form.reset();
    $("#task-id").value = task?.id ?? "";
    $("#task-title").value = task?.title ?? "";
    $("#task-desc").value = task?.description ?? "";
    $("#task-priority").value = task?.priority ?? "medium";
    $("#task-status").value = task?.status ?? "todo";
    $("#task-date").value = task?.date ?? "";
    $("#dialog-heading").textContent = task ? "Редагувати завдання" : "Нове завдання";
    dialog.showModal();
    $("#task-title").focus();
  }

  $("#add-task").addEventListener("click", () => openEditor());
  $("#close-dialog").addEventListener("click", () => dialog.close());
  $("#cancel-dialog").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", event => {
    if (event.target === dialog) dialog.close();
  });

  form.addEventListener("submit", event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const id = $("#task-id").value;
    const title = $("#task-title").value.trim();
    if (title.length < 2) {
      $("#task-title").setCustomValidity("Назва має бути не коротшою за 2 символи");
      form.reportValidity();
      return;
    }
    const task = {
      id: id || (window.crypto?.randomUUID?.() || `${Date.now()}-${Math.random()}`),
      title, description: $("#task-desc").value.trim(),
      priority: $("#task-priority").value, status: $("#task-status").value,
      date: $("#task-date").value
    };
    if (!validTask(task)) return;
    if (id) tasks = tasks.map(existing => existing.id === id ? task : existing);
    else tasks.unshift(task);
    persist();
    render();
    announce(id ? "Завдання оновлено." : "Нове завдання додано.");
    dialog.close();
  });
  $("#task-title").addEventListener("input", event => event.currentTarget.setCustomValidity(""));

  $("#board").addEventListener("click", event => {
    const button = event.target.closest("button[data-action]");
    const card = event.target.closest(".task-card");
    if (!button || !card) return;
    const task = tasks.find(item => item.id === card.dataset.id);
    if (!task) return;
    if (button.dataset.action === "edit") openEditor(task);
    if (button.dataset.action === "delete" && window.confirm(`Видалити «${task.title}»?`)) {
      tasks = tasks.filter(item => item.id !== task.id);
      persist(); render(); announce("Завдання видалено.");
    }
  });

  $("#board").addEventListener("dragstart", event => {
    const card = event.target.closest(".task-card");
    if (!card || !event.dataTransfer) return;
    event.dataTransfer.setData("text/plain", card.dataset.id);
    event.dataTransfer.effectAllowed = "move";
    card.classList.add("dragging");
  });
  $("#board").addEventListener("dragend", () => {
    document.querySelectorAll(".board-column").forEach(column => column.classList.remove("drag-over"));
    document.querySelectorAll(".task-card.dragging").forEach(card => card.classList.remove("dragging"));
  });
  document.querySelectorAll(".board-column").forEach(column => {
    column.addEventListener("dragover", event => { event.preventDefault(); column.classList.add("drag-over"); });
    column.addEventListener("dragleave", event => {
      if (!column.contains(event.relatedTarget)) column.classList.remove("drag-over");
    });
    column.addEventListener("drop", event => {
      event.preventDefault();
      column.classList.remove("drag-over");
      const id = event.dataTransfer?.getData("text/plain");
      const task = tasks.find(item => item.id === id);
      if (task) {
        task.status = column.dataset.status;
        persist(); render(); announce(`Статус завдання «${task.title}» змінено.`);
      }
    });
  });
  $("#task-search").addEventListener("input", render);
  $("#priority-filter").addEventListener("change", render);
  $("#clear-done").addEventListener("click", () => {
    if (!window.confirm("Видалити всі виконані завдання?")) return;
    tasks = tasks.filter(task => task.status !== "done");
    persist(); render(); announce("Виконані завдання видалено.");
  });
  render();
})();
