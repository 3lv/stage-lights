import customtkinter as ctk
import lib8relind
import time
import threading

# Set the theme
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

def trigger_relay(relay_number, on_time, off_time):
    for _ in range(3):
        lib8relind.set(0, relay_number, 1)  # Turn on relay
        time.sleep(on_time)  # Wait for on_time
        lib8relind.set(0, relay_number, 0)  # Turn off relay
        time.sleep(off_time)  # Wait for off_time
    #ctk.CTkMessagebox.show_info("Relay Triggered", f"Relay {relay_number} was triggered on/off 3 times.")

def on_relay_button_click(relay_number):
    on_time = on_time_slider.get()
    off_time = off_time_slider.get()
    threading.Thread(target=trigger_relay, args=(relay_number, on_time, off_time)).start()

def update_on_time_label(value):
    on_time_value_label.configure(text=f"{value:.1f} sec")

def update_off_time_label(value):
    off_time_value_label.configure(text=f"{value:.1f} sec")

# Create the main application window
app = ctk.CTk()
app.title("Modern Relay Controller")

# Make the window fullscreen
app.attributes('-fullscreen', True)
app.wm_attributes('-fullscreen', True)
app.state('normal')

# Bind the 'Escape' key to exit fullscreen
app.bind("<Escape>", lambda event: app.attributes('-fullscreen', False))

# Make the grid layout expand with window resizing
app.columnconfigure([0, 1, 2, 3], weight=1, uniform="columns")
app.rowconfigure([0, 1, 2, 3], weight=1, uniform="rows")

# Create buttons for relays 1 to 8 and arrange them in a 4x2 grid
for i in range(1, 9):
    button = ctk.CTkButton(app, text=f"Relay {i}",
                           command=lambda i=i: on_relay_button_click(i))
    button.grid(row=(i-1)//4, column=(i-1)%4, padx=10, pady=10, sticky="nsew")

# Time selectors for on_time and off_time with displayed values
on_time_label = ctk.CTkLabel(app, text="On Time (seconds):")
on_time_label.grid(row=2, column=0, pady=10, sticky="w")

on_time_slider = ctk.CTkSlider(app, from_=0.5, to=5.0, number_of_steps=45, command=update_on_time_label)
on_time_slider.set(1)
on_time_slider.grid(row=2, column=1, pady=10, sticky="ew")

on_time_value_label = ctk.CTkLabel(app, text="1.0 sec")  # Display the on_time value
on_time_value_label.grid(row=2, column=2, pady=10, sticky="w")

off_time_label = ctk.CTkLabel(app, text="Off Time (seconds):")
off_time_label.grid(row=3, column=0, pady=10, sticky="w")

off_time_slider = ctk.CTkSlider(app, from_=0.5, to=5.0, number_of_steps=45, command=update_off_time_label)
off_time_slider.set(1)
off_time_slider.grid(row=3, column=1, pady=10, sticky="ew")

off_time_value_label = ctk.CTkLabel(app, text="1.0 sec")  # Display the off_time value
off_time_value_label.grid(row=3, column=2, pady=10, sticky="w")

# Exit button at the bottom
exit_button = ctk.CTkButton(app, text="Exit", command=app.quit)
exit_button.grid(row=4, column=1, columnspan=2, pady=20, sticky="nsew")

# Run the application
app.mainloop()
