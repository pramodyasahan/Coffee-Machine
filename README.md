# Coffee Machine Application

A simple coffee machine application that takes user input for selecting coffee options, processes coins inserted as payment, and prepares the selected coffee if there are sufficient resources and payment. This application is created using Object-Oriented Programming (OOP) concepts in Python.

## Features

- User can select between three types of coffee: Espresso, Latte, and Cappuccino.
- User can insert coins as payment.
- Coffee is served if there are sufficient resources and payment.
- Provides a report on the current status of resources.

## Classes and Methods

### 1. `CoffeeMachine`

The main class representing the coffee machine. The coffee machine maintains its state (resources and menu) and provides methods to interact with it.

#### Methods:

- `__init__`: Initializes a new instance of `CoffeeMachine` with default resources and menu.
- `report`: Prints the current status of the coffee machine's resources.
- `check_resources`: Checks if there are sufficient resources to make the requested coffee.
- `manage_resources`: Deducts the resources used to make the coffee from the available resources.
- `process_coins`: Processes coin input from the user and returns the total amount.
- `serve_coffee`: Serves the requested coffee and manages the transaction.
- `run`: Runs the coffee machine, accepting and processing user input.

## Usage

Create an instance of the `CoffeeMachine` class and call the `run` method:

```python
machine = CoffeeMachine()
machine.run()
```
## Requirements

- Python 3.6+
