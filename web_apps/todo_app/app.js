/**
 * TaskFlow – To-Do App
 * Manages tasks with add, complete, delete, and filter functionality.
 * Persists tasks in localStorage so they survive page reloads.
 */

const STORAGE_KEY = "taskflow_tasks";

/** @type {Array<{id: string, text: string, completed: boolean, createdAt: number}>} */
let tasks = [];
let currentFilter = "all";

// ── DOM references ──────────────────────────────────────────────────────────
const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const taskCount = document.getElementById("task-count");
const clearCompletedBtn = document.getElementById("clear-completed");
const filterBtns = document.querySelectorAll(".filter-btn");

// ── Helpers ──────────────────────────────────────────────────────────────────

/**
 * Generate a simple unique ID.
 * @returns {string}
 */
function generateId() {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`;
}

/** Load tasks from localStorage. */
function loadTasks() {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    tasks = stored ? JSON.parse(stored) : [];
  } catch {
    tasks = [];
  }
}

/** Persist tasks to localStorage. */
function saveTasks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

// ── Core actions ─────────────────────────────────────────────────────────────

/**
 * Add a new task.
 * @param {string} text
 */
function addTask(text) {
  const trimmed = text.trim();
  if (!trimmed) return;

  tasks.push({
    id: generateId(),
    text: trimmed,
    completed: false,
    createdAt: Date.now(),
  });

  saveTasks();
  render();
}

/**
 * Toggle the completed state of a task.
 * @param {string} id
 */
function toggleTask(id) {
  const task = tasks.find((t) => t.id === id);
  if (task) {
    task.completed = !task.completed;
    saveTasks();
    render();
  }
}

/**
 * Delete a task by ID.
 * @param {string} id
 */
function deleteTask(id) {
  tasks = tasks.filter((t) => t.id !== id);
  saveTasks();
  render();
}

/** Remove all completed tasks. */
function clearCompleted() {
  tasks = tasks.filter((t) => !t.completed);
  saveTasks();
  render();
}

// ── Rendering ─────────────────────────────────────────────────────────────────

/** Return tasks matching the current filter. */
function getFilteredTasks() {
  switch (currentFilter) {
    case "active":
      return tasks.filter((t) => !t.completed);
    case "completed":
      return tasks.filter((t) => t.completed);
    default:
      return tasks;
  }
}

/**
 * Create a task list item element.
 * @param {{id: string, text: string, completed: boolean}} task
 * @returns {HTMLLIElement}
 */
function createTaskElement(task) {
  const li = document.createElement("li");
  li.className = "task-item";
  li.dataset.id = task.id;

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "task-checkbox";
  checkbox.checked = task.completed;
  checkbox.setAttribute("aria-label", `Mark "${task.text}" as ${task.completed ? "active" : "completed"}`);
  checkbox.addEventListener("change", () => toggleTask(task.id));

  const span = document.createElement("span");
  span.className = `task-text${task.completed ? " completed" : ""}`;
  span.textContent = task.text;

  const deleteBtn = document.createElement("button");
  deleteBtn.className = "task-delete";
  deleteBtn.textContent = "×";
  deleteBtn.setAttribute("aria-label", `Delete task: ${task.text}`);
  deleteBtn.addEventListener("click", () => deleteTask(task.id));

  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(deleteBtn);
  return li;
}

/** Re-render the task list and footer count. */
function render() {
  const filtered = getFilteredTasks();

  // Rebuild list
  taskList.innerHTML = "";
  filtered.forEach((task) => {
    taskList.appendChild(createTaskElement(task));
  });

  // Update count (always based on *all* active tasks, not filtered)
  const activeCount = tasks.filter((t) => !t.completed).length;
  taskCount.textContent = `${activeCount} task${activeCount !== 1 ? "s" : ""} remaining`;
}

// ── Event listeners ──────────────────────────────────────────────────────────

taskForm.addEventListener("submit", (e) => {
  e.preventDefault();
  addTask(taskInput.value);
  taskInput.value = "";
});

clearCompletedBtn.addEventListener("click", clearCompleted);

filterBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    filterBtns.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentFilter = btn.dataset.filter;
    render();
  });
});

// ── Init ─────────────────────────────────────────────────────────────────────
loadTasks();
render();
