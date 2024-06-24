from rpg_simulator_app import RPGSimulatorApp


if __name__ == "__main__":
    app = RPGSimulatorApp("TTRPG Shop and Economy Simulator", 800, 600)
    app.update_logic()
    app.root.mainloop()
