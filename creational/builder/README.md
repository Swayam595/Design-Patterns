# 🧱 [Builder Design Pattern](https://refactoring.guru/design-patterns/builder)

The **Builder Design Pattern** is a creational pattern used to construct complex objects step by step. It separates the construction logic from the representation, allowing the same construction process to create different representations.

## ✅ Key Features
- Useful when an object has many optional or configurable parameters.
- Promotes immutability and code readability via method chaining.
- Helps avoid telescoping constructors.

## 🧩 Structure
- **Builder**: Provides methods to set individual parts.
- **Product**: The complex object being built.
- **Director (optional)**: Controls the build order.

## 📌 Benefits
- Improves clarity when creating objects.
- Makes code flexible and easier to maintain.
- Enables controlled object construction and validation.
