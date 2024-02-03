# Python Economic Simulator

## Overview

The Python Economic Simulator is a simple command-line program that simulates economic events and updates the state of an economy based on user input. This project consists of three main files: `main.py`, `econ_module.py`, and `interface.py`.

## Files

1. **main.py:**
    - The entry point of the program.
    - Initializes an instance of the `EconomicSimulator` class and the `UserInterface` class.
    - Calls the `run_simulation` method of the `UserInterface` to start the simulation.

2. **econ_module.py:**
    - Defines the `EconomicSimulator` class.
    - Handles the simulation of economic events and updates the state of the economy.
    - Contains methods such as `simulate_event` and `update_economy`.

3. **interface.py:**
    - Implements the user interface using the `tkinter` library.
    - Provides a simple GUI with elements such as labels, buttons, and entry widgets.
    - Allows users to simulate economic events by providing input.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/itsmaddiegrace/econ-simulator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd econ-simulator
    ```

3. Run the simulation:

    ```bash
    python main.py
    ```

4. Follow the instructions on the interface to simulate economic events and observe the updated balance.

## Dependencies

- Python 3.x
- tkinter (usually included with Python installations)

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Suggestions and improvements are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community and the tkinter library for providing tools to create simple user interfaces.
