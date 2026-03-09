package com.example.taskmanager

import android.graphics.Paint
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.example.taskmanager.databinding.ItemTaskBinding

/**
 * RecyclerView adapter for displaying [Task] items.
 *
 * @param onToggle Called when the user checks/unchecks a task.
 * @param onDelete Called when the user taps the delete button.
 */
class TaskAdapter(
    private val onToggle: (Task) -> Unit,
    private val onDelete: (Task) -> Unit,
) : ListAdapter<Task, TaskAdapter.TaskViewHolder>(DiffCallback) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TaskViewHolder {
        val binding = ItemTaskBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return TaskViewHolder(binding)
    }

    override fun onBindViewHolder(holder: TaskViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class TaskViewHolder(private val binding: ItemTaskBinding) :
        RecyclerView.ViewHolder(binding.root) {

        fun bind(task: Task) {
            binding.taskTitleText.text = task.title
            binding.taskCheckbox.isChecked = task.completed

            // Strike-through text for completed tasks
            val flags = if (task.completed) {
                binding.taskTitleText.paintFlags or Paint.STRIKE_THRU_TEXT_FLAG
            } else {
                binding.taskTitleText.paintFlags and Paint.STRIKE_THRU_TEXT_FLAG.inv()
            }
            binding.taskTitleText.paintFlags = flags

            binding.taskCheckbox.setOnClickListener { onToggle(task) }
            binding.deleteButton.setOnClickListener { onDelete(task) }
        }
    }

    private companion object DiffCallback : DiffUtil.ItemCallback<Task>() {
        override fun areItemsTheSame(oldItem: Task, newItem: Task) = oldItem.id == newItem.id
        override fun areContentsTheSame(oldItem: Task, newItem: Task) = oldItem == newItem
    }
}
