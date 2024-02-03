import tkinter as tk

class UserInterface:
    def __init__(self, econ_simulator):
        self.econ_simulator = econ_simulator
        self.root = tk.Tk()

        self.label_balance = tk.Label(self.root, text=f"Current Balance: {self.econ_simulator.balance}")
        self.label_balance.pack()

        self.button_simulate = tk.Button(self.root, text="Simulate Event", command=self.simulate_event)
        self.button_simulate.pack()

        self.label_info = tk.Label(self.root, text="")
        self.label_info.pack()

        self.entry_parameter = tk.Entry(self.root)
        self.entry_parameter.pack()

    def run_simulation(self):
        self.root.mainloop()

    def simulate_event(self):
        user_input = self.entry_parameter.get()
        self.econ_simulator.simulate_event(user_input)
        self.update_interface()

    def update_interface(self):
        self.label_balance.config(text=f"Current Balance: {self.econ_simulator.balance}")
        self.label_info.config(text="Event simulated. Balance updated.")
