# Device Energy Consumption

## Overview
This project demonstrates abstraction in Python by modeling different devices (e.g., Phone, Laptop) and their energy consumption behavior.

## Concepts Covered
- Abstract Classes (ABC)
- Inheritance
- Method Overriding (Polymorphism)
- Encapsulation

## Features
- Common interface for all devices using an abstract base class
- Each device defines its own energy consumption logic
- Demonstrates polymorphism by calling the same method on different device types

## Code Structure
- `Device` → Abstract base class defining required methods
- `Phone` → Implements device-specific energy usage
- `Laptop` → Implements device-specific energy usage

## Example Usage
```python
phone = Phone(battery=100)
laptop = Laptop(battery=100)

phone.use(2)
laptop.use(2)
