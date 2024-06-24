import tkinter as tk
from tkinter import ttk, messagebox


class RPGSimulatorApp:
    def __init__(self, title, width, height):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.create_menus()
        self.setup_ui()

        self.status_label = None
        self.weather_label = None
        self.create_status_bar()

        self.root.after(1000, lambda: self.update_status_label("Window initialized"))

    def create_menus(self):
        # Menu Bar setup
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.on_open)
        file_menu.add_command(label="Save", command=self.on_save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_exit)

        # World menu
        world_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="World", menu=world_menu)
        world_menu.add_command(label="Edit World")
        world_menu.add_command(label="Add City")
        world_menu.add_command(label="Add Trade Route")

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def setup_ui(self):
        # Configure grid layout
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # World Map Section
        map_frame = ttk.Frame(self.root, borderwidth=2, relief="sunken")
        map_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        map_label = ttk.Label(map_frame, text="World Map")
        map_label.pack(padx=10, pady=10)

        # Detail Panel
        detail_frame = ttk.Frame(self.root, borderwidth=2, relief="sunken")
        detail_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        detail_label = ttk.Label(detail_frame, text="Details Panel")
        detail_label.pack(padx=10, pady=10)

        # Control Panel
        control_frame = ttk.LabelFrame(detail_frame, text="Control Panel", borderwidth=2, relief="sunken")
        control_frame.pack(fill="both", expand=True, padx=5, pady=5)
        add_button = ttk.Button(control_frame, text="Add City")
        add_button.pack(padx=5, pady=5)

        # Visibility Toggles (inside Detail Panel for this example)
        visibility_frame = ttk.Frame(detail_frame)
        visibility_frame.pack(fill="x", expand=False, padx=5, pady=5)
        toggle_gm_view = ttk.Checkbutton(visibility_frame, text="GM View")
        toggle_gm_view.pack(side="left", padx=10, pady=10)

    def create_status_bar(self):
        # Status Bar
        status_bar = ttk.Frame(self.root, relief="sunken")
        status_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.status_label = ttk.Label(status_bar, text="Status: Loading", anchor="w")
        self.status_label.pack(side="left", padx=5, pady=2)
        self.weather_label = ttk.Label(status_bar, text="Weather: Sunny, 70\u00B0 F")
        self.weather_label.pack(side="right", padx=5, pady=2)

    def update_status_label(self, message):
        self.status_label.config(text=message)

    def on_open(self):
        # TODO: Placeholder for open functionality
        pass

    def on_save(self):
        # TODO: Placeholder for save functionality
        pass

    def on_exit(self):
        shall_we_save = messagebox.askyesnocancel("Save?", "Do you want to save?")

        if shall_we_save is None:
            return  # User replied cancel.

        if shall_we_save:
            self.on_save()

        self.root.destroy()

    @staticmethod
    def show_about():
        messagebox.showinfo("About", "RPG GDP Simulator\nVersion Alpha 0.1\n\nDesigner: Me JW Crouch")
