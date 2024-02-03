from econ_module import EconomicSimulator
from interface import UserInterface

def main():
    econ_sim = EconomicSimulator()
    ui = UserInterface(econ_sim)
    ui.run_simulation()

if __name__ == "__main__":
    main()
