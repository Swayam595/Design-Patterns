# Singleton Pattern and Double-Checked Locking

## 🧩 Singleton Pattern

The **Singleton Pattern** ensures that a class has **only one instance** and provides a **global point of access** to that instance.

It is commonly used in situations where:
- A single object is needed to coordinate actions (e.g., configuration manager, logging service, database connection pool).
- Ensuring controlled access to shared resources.

### Key Characteristics:
- A private constructor (to prevent external instantiation)
- A static instance of the class
- A public method to get the instance

### 🔒 Double-Checked Locking

**Double-Checked Locking** is an optimization technique used to reduce the overhead of acquiring a lock by first testing the locking criterion without synchronization.

#### ✅ Key Points:
- Used in **multi-threaded** environments to ensure a class is **lazily initialized** in a **thread-safe** manner.
- It involves checking if the instance is `None` (or null) **before** acquiring the lock.
- The instance is checked **again inside the lock** to ensure that it hasn’t already been initialized by another thread.
- Helps avoid the cost of locking every time the instance is accessed after initialization.
- Especially useful when creating expensive-to-initialize singleton objects.

#### ⚠️ Caution:
- Must be implemented carefully to avoid race conditions.
- In some languages like Java, the instance should be marked as `volatile` to prevent instruction reordering.

