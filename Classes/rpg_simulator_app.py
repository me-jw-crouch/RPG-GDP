import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from world import World
import pickle
from mytime import *
from datetime import datetime, timedelta


class RPGSimulatorApp:
    def __init__(self, title, width, height):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.world: World = World("New World")
        self.gm_view = False
        self.last_status_update_time = datetime.now() - timedelta(seconds=4)

        self.menu_bar = None
        self.file_menu = None
        self.world_menu = None
        self.help_menu = None
        self.create_menus()

        self.status_label = None
        self.weather_label = None
        self.create_status_bar()

        self.map_frame = None
        self.map_label = None
        self.detail_frame = None
        self.control_frame = None
        self.visibility_frame = None
        self.gm_view_checkbox = None
        self.setup_ui()

        self.root.after(1000, lambda: self.update_status_label("Window initialized"))

    def create_menus(self):
        # Menu Bar setup
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New World", command=self.on_new_world)
        self.file_menu.add_command(label="Load World", command=self.on_load_world)
        self.file_menu.add_command(label="Save World", command=self.on_save_world)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.on_exit)

        # World menu
        self.world_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="World", menu=self.world_menu)
        self.world_menu.add_command(label="Edit World")
        self.world_menu.add_command(label="Add City")
        self.world_menu.add_command(label="Add Trade Route")

        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

    def setup_ui(self):
        # Configure grid layout
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # World Map Section
        self.map_frame = ttk.Frame(self.root, borderwidth=2, relief="sunken")
        self.map_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.map_label = ttk.Label(self.map_frame, text="World Map")
        self.map_label.pack(padx=10, pady=10)

        # Detail Panel
        self.detail_frame = ttk.Frame(self.root, borderwidth=2, relief="sunken")
        self.detail_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        detail_label = ttk.Label(self.detail_frame, text="Details Panel")
        detail_label.pack(padx=10, pady=10)

        # Control Panel
        self.control_frame = ttk.LabelFrame(self.detail_frame, text="Control Panel", borderwidth=2, relief="sunken")
        self.control_frame.pack(fill="both", expand=True, padx=5, pady=5)
        add_button = ttk.Button(self.control_frame, text="Add City", command=self.world.add_city)
        add_button.pack(padx=5, pady=5)

        # Visibility Toggles (inside Detail Panel for this example)
        self.visibility_frame = ttk.Frame(self.detail_frame)
        self.visibility_frame.pack(fill="x", expand=False, padx=5, pady=5)
        self.gm_view_checkbox = tk.Checkbutton(self.visibility_frame, text="GM View", command=self.toggle_gm_view)
        self.gm_view_checkbox.pack(side="left", padx=10, pady=10)
        self.toggle_gm_view()

    def toggle_gm_view(self):
        self.gm_view = not self.gm_view

        if self.gm_view:
            self.gm_view_checkbox.select()
            self.update_status_label("GM view ON")
        else:
            self.gm_view_checkbox.deselect()
            self.update_status_label("GM view OFF")

        self.root.after(2000, lambda: self.update_status_label("Running"))

    def create_status_bar(self):
        # Status Bar
        status_bar = ttk.Frame(self.root, relief="sunken")
        status_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.status_label = ttk.Label(status_bar, text="Status: Loading", anchor="w")
        self.status_label.pack(side="left", padx=5, pady=2)
        self.weather_label = ttk.Label(status_bar, text="Weather: Sunny, 70\u00B0 F")
        self.weather_label.pack(side="right", padx=5, pady=2)

    def update_status_label(self, message):
        self.status_label.config(text=get_formatted_time() + "   Status: " + message)
        self.last_status_update_time = datetime.now()

    def on_new_world(self, settings=None):
        name = 'This New World'
        self.world = World(name)
        self.world.generate_world(settings)

    def on_load_world(self):
        file_path = filedialog.askopenfilename(filetypes=[("RPG GDP world files", "*.rworld"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'rb') as file:
                self.world = pickle.load(file)

    def on_save_world(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".rworld",
                                                 filetypes=[("RPG GDP world files", "*.rworld"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'wb') as file:
                pickle.dump(self.world, file)

    def on_exit(self):
        shall_we_save = messagebox.askyesnocancel("Save?", "Do you want to save?")

        if shall_we_save is None:
            return  # User replied cancel.

        if shall_we_save:
            self.on_save_world()

        self.root.destroy()

    def update_logic(self):
        msg = "Running"
        if has_a_second_passed(self.last_status_update_time):
            self.update_status_label(msg)

        self.root.after(100, self.update_logic)

    @staticmethod
    def show_about():
        messagebox.showinfo("About", "RPG GDP Simulator\nVersion Alpha 0.1\n\nDesigner: Me JW Crouch")
