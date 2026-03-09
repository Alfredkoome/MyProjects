package com.example.taskmanager

import java.util.UUID

/**
 * Represents a single task in the task manager.
 *
 * @property id Unique identifier generated automatically.
 * @property title Human-readable task description.
 * @property completed Whether the task has been marked done.
 * @property createdAt Timestamp (epoch ms) when the task was created.
 */
data class Task(
    val id: String = UUID.randomUUID().toString(),
    val title: String,
    val completed: Boolean = false,
    val createdAt: Long = System.currentTimeMillis()
)
