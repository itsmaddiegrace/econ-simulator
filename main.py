# main.py

from econ_simulator import EconSimulator
from crypto_predictor import CryptoPredictor

def main():
    econ_simulator = EconSimulator()
    econ_simulator.run_simulation()

    crypto_predictor = CryptoPredictor()
    crypto_predictor.run_prediction()

if __name__ == "__main__":
    main()
