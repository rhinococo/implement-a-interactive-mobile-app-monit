import tkinter as tk
from tkinter import ttk
import psutil

class AppMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Mobile App Monitor")
        self.root.geometry("400x400")

        # Create tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=1)

        # Create frames for each tab
        self.frame_cpu = ttk.Frame(self.tabs)
        self.frame_memory = ttk.Frame(self.tabs)
        self.frame_battery = ttk.Frame(self.tabs)

        # Add frames to tabs
        self.tabs.add(self.frame_cpu, text="CPU")
        self.tabs.add(self.frame_memory, text="Memory")
        self.tabs.add(self.frame_battery, text="Battery")

        # Create labels and updates for CPU usage
        self.label_cpu = ttk.Label(self.frame_cpu, text="CPU Usage:")
        self.label_cpu.pack()
        self.cpu_usage = ttk.Label(self.frame_cpu, text="")
        self.cpu_usage.pack()

        # Create labels and updates for Memory usage
        self.label_memory = ttk.Label(self.frame_memory, text="Memory Usage:")
        self.label_memory.pack()
        self.memory_usage = ttk.Label(self.frame_memory, text="")
        self.memory_usage.pack()

        # Create labels and updates for Battery percentage
        self.label_battery = ttk.Label(self.frame_battery, text="Battery Percentage:")
        self.label_battery.pack()
        self.battery_percentage = ttk.Label(self.frame_battery, text="")
        self.battery_percentage.pack()

        # Update function for CPU usage
        def update_cpu():
            cpu = psutil.cpu_percent(interval=1)
            self.cpu_usage.config(text=f"{cpu}%")
            self.root.after(1000, update_cpu)

        # Update function for Memory usage
        def update_memory():
            memory = psutil.virtual_memory().percent
            self.memory_usage.config(text=f"{memory}%")
            self.root.after(1000, update_memory)

        # Update function for Battery percentage
        def update_battery():
            battery = psutil.sensors_battery().percent
            self.battery_percentage.config(text=f"{battery}%")
            self.root.after(1000, update_battery)

        # Start updates
        update_cpu()
        update_memory()
        update_battery()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMonitor(root)
    root.mainloop()