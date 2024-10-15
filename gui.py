import tkinter as tk
from tkinter import messagebox
import lib8relind
import time
import threading

def trigger_relay(relay_number, on_time, off_time):
    # Relay on/off loop 3 times
    for _ in range(3):
        lib8relind.set(0, relay_number, 1)  # Turn on relay
        time.sleep(on_time)  # Wait for the specified on time
        lib8relind.set(0, relay_number, 0)  # Turn off relay
        time.sleep(off_time)  # Wait for the specified off time
    #messagebox.showinfo("Relay Triggered", f"Relay {relay_number} was triggered on/off 3 times.")

def on_relay_button_click(relay_number):
    on_time = on_time_slider.get()
    off_time = off_time_slider.get()
    # Use threading to avoid freezing the GUI during relay operation
    threading.Thread(target=trigger_relay, args=(relay_number, on_time, off_time)).start()

# Create the main application window
app = tk.Tk()
app.title("Relay Controller")

# Create buttons for relays 1 to 8 and arrange them in a 4x2 grid
for i in range(1, 9):
    button = tk.Button(app, text=f"Relay {i}", width=10, height=2,
                       command=lambda i=i: on_relay_button_click(i))
    button.grid(row=(i-1)//4, column=(i-1)%4, padx=10, pady=10)  # 4 columns, 2 rows

# Time selectors for on_time and off_time
on_time_label = tk.Label(app, text="On Time (seconds):")
on_time_label.grid(row=2, column=0, pady=10)
on_time_slider = tk.Scale(app, from_=0.5, to=5.0, resolution=0.1, orient=tk.HORIZONTAL)
on_time_slider.set(1)  # Default value is 1 second
on_time_slider.grid(row=2, column=1, pady=10)

off_time_label = tk.Label(app, text="Off Time (seconds):")
off_time_label.grid(row=2, column=2, pady=10)
off_time_slider = tk.Scale(app, from_=0.5, to=5.0, resolution=0.1, orient=tk.HORIZONTAL)
off_time_slider.set(1)  # Default value is 1 second
off_time_slider.grid(row=2, column=3, pady=10)

# Exit button below the grid
exit_button = tk.Button(app, text="Exit", width=10, height=2, command=app.quit)
exit_button.grid(row=3, column=1, columnspan=2, pady=20)

# Run the application
app.mainloop()
