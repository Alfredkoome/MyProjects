package com.example.taskmanager

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.taskmanager.databinding.ActivityMainBinding
import com.google.android.material.snackbar.Snackbar

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var viewModel: TaskViewModel
    private lateinit var adapter: TaskAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        viewModel = ViewModelProvider(this)[TaskViewModel::class.java]

        setupRecyclerView()
        setupObservers()
        setupListeners()
    }

    private fun setupRecyclerView() {
        adapter = TaskAdapter(
            onToggle = { task -> viewModel.toggleTask(task) },
            onDelete = { task ->
                viewModel.deleteTask(task)
                Snackbar.make(binding.root, "Task deleted", Snackbar.LENGTH_SHORT)
                    .setAction("Undo") { viewModel.addTask(task) }
                    .show()
            }
        )
        binding.recyclerView.apply {
            layoutManager = LinearLayoutManager(this@MainActivity)
            adapter = this@MainActivity.adapter
        }
    }

    private fun setupObservers() {
        viewModel.tasks.observe(this) { tasks ->
            adapter.submitList(tasks)
            val active = tasks.count { !it.completed }
            binding.taskCountText.text = resources.getQuantityString(
                R.plurals.tasks_remaining, active, active
            )
        }
    }

    private fun setupListeners() {
        binding.addTaskButton.setOnClickListener {
            val text = binding.taskInputEditText.text?.toString()?.trim() ?: ""
            if (text.isNotEmpty()) {
                viewModel.addTask(Task(title = text))
                binding.taskInputEditText.text?.clear()
            } else {
                binding.taskInputLayout.error = getString(R.string.error_empty_task)
            }
        }

        binding.taskInputEditText.setOnEditorActionListener { _, _, _ ->
            binding.addTaskButton.performClick()
            true
        }

        binding.clearCompletedButton.setOnClickListener {
            viewModel.clearCompleted()
        }
    }
}
