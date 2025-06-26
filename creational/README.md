# 🏗️ [Creational Design Patterns](https://refactoring.guru/design-patterns/creational-patterns)

**Creational Design Patterns** are a category of design patterns that deal with object creation mechanisms. They abstract the instantiation process, making it more flexible and dynamic.

Instead of creating objects directly using constructors, creational patterns provide ways to create objects in a controlled and reusable manner.

## ✅ Purpose
- Hide the complexity of object creation.
- Enhance code flexibility, scalability, and reusability.
- Support different object creation scenarios (e.g., based on environment, configuration, or type).

## 🧩 Common Creational Patterns

| Pattern           | Description |
|------------------|-------------|
| **[Singleton](https://github.com/Swayam595/Design-Patterns/tree/main/creational/singleton)**     | Ensures a class has only one instance and provides a global point of access to it. |
| **Factory Method**| Defines an interface for creating objects, but lets subclasses alter the type of objects that will be created. |
| **Abstract Factory** | Provides an interface to create families of related or dependent objects without specifying their concrete classes. |
| **[Builder](https://github.com/Swayam595/Design-Patterns/tree/main/creational/builder)**      | Separates the construction of a complex object from its representation so the same construction process can create different representations. |
| **Prototype**     | Creates new objects by copying an existing object (clone). |

## 🛠️ When to Use
- When the system should be independent of how its objects are created.
- When you need to manage or control object creation logic.
- When dealing with complex object creation with many parameters or configurations.

