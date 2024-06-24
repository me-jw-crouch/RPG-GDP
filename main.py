import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


status_label = None
weather_label = None

def on_open():
    messagebox.showinfo("Open", "Open menu item clicked!")


def on_save():
    messagebox.showinfo("Save", "Save menu item clicked!")


def on_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


def update_status_bar_label(message):
    global status_label
    if status_label:
        status_label.config(text="Status: "+message)


def update_weather_label(weather, temp):
    global weather_label
    if weather_label:
        weather_label.config(text=temp + " - " + weather)


def initialize_window(title, width, height):
    global status_label
    global weather_label

    # Create the main window
    root = tk.Tk()
    root.title(title)
    root.geometry(str(width)+"x"+str(height))

    # Configure grid layout
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    # Create a menu bar
    menu_bar = tk.Menu(root)
    menu_bar.widgetName = "menuBar"
    root.config(menu=menu_bar)

    # Create a File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=on_open)
    file_menu.add_command(label="Save", command=on_save)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=on_exit)

    # Create an Edit menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="World", menu=edit_menu)
    edit_menu.add_command(label="Edit World")
    edit_menu.add_command(label="Add City")
    edit_menu.add_command(label="Add Trade Route")

    # Create a Help menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About",
                          command=lambda: messagebox.showinfo("About", "RPG GDP Simulator\nVersion Alpha.0"))

    # Configure grid layout
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    # World Map Section
    map_frame = ttk.Frame(root, borderwidth=2, relief="sunken")
    map_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    map_label = ttk.Label(map_frame, text="World Map")
    map_label.pack(padx=10, pady=10)

    # Detail Panel
    detail_frame = ttk.Frame(root, borderwidth=2, relief="sunken")
    detail_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    detail_label = ttk.Label(detail_frame, text="Details Panel")
    detail_label.pack(padx=10, pady=10)

    # Control Panel (inside Detail Panel for this example)
    control_frame = ttk.LabelFrame(detail_frame, text="Control Panel", borderwidth=2, relief="sunken")
    control_frame.pack(fill="both", expand=True, padx=5, pady=5)
    add_button = ttk.Button(control_frame, text="Add City")
    add_button.pack(padx=5, pady=5)

    # Visibility Toggles (inside Detail Panel for this example)
    visibility_frame = ttk.Frame(detail_frame)
    visibility_frame.pack(fill="both", expand=True, padx=5, pady=5)
    toggle_gm_view = ttk.Checkbutton(visibility_frame, text="GM View")
    toggle_gm_view.pack(side="left", padx=10, pady=10)

    # Status Bar
    status_bar = ttk.Frame(root, relief="sunken")
    status_bar.grid(row=1, column=0, columnspan=2, sticky="ew")

    status_label = ttk.Label(status_bar, text="Status: Loading", anchor="w")
    status_label.pack(side="left", padx=5, pady=2)

    weather_label = ttk.Label(status_bar, text="")
    weather_label.pack(side="right", padx=5, pady=2)
    update_weather_label("Sunny", "70 F")

    root.after(1000, lambda: update_status_bar_label("Window initialized"))

    return root


def update():

    root.after(100, update)


if __name__ == "__main__":
    root = initialize_window("RPG GDP: TTRPG Shop and Economy Simulator", 1200, 800)

    # Start the Update Loop
    root.after(100, update)

    # Start Tkinter's Draw Loop
    root.mainloop()
