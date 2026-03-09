package com.example.taskmanager

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

/**
 * ViewModel that holds the task list and exposes actions to the UI.
 * In a production app this would delegate to a repository/database.
 */
class TaskViewModel : ViewModel() {

    private val _tasks = MutableLiveData<List<Task>>(emptyList())
    val tasks: LiveData<List<Task>> = _tasks

    /** Add a new task (or re-add a previously deleted one for undo support). */
    fun addTask(task: Task) {
        _tasks.value = (_tasks.value ?: emptyList()) + task
    }

    /** Toggle the completed state of an existing task. */
    fun toggleTask(task: Task) {
        _tasks.value = (_tasks.value ?: emptyList()).map { existing ->
            if (existing.id == task.id) existing.copy(completed = !existing.completed)
            else existing
        }
    }

    /** Remove a single task from the list. */
    fun deleteTask(task: Task) {
        _tasks.value = (_tasks.value ?: emptyList()).filter { it.id != task.id }
    }

    /** Remove all completed tasks at once. */
    fun clearCompleted() {
        _tasks.value = (_tasks.value ?: emptyList()).filter { !it.completed }
    }
}
