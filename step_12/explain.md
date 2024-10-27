# 1. **UUID**

- `user_id`: It uses a universally unique identifier. In the request, it's given as a string, and Pydantic ensures it's valid.

## 2. **datetime.datetime**

- `created_at`: Represents both date and time in ISO 8601 format (e.g., `2024-10-27T14:23:00+05:00`).  

## 3. **datetime.date**

- `birth_date`: A simple date without the time component (e.g., `1990-05-15`).

## 4. **datetime.time**

- `login_time`: Only the time portion, useful for logging events or schedules (e.g., `08:45:00`).

## 5. **datetime.timedelta**

- `session_duration`: Represents a time difference (in seconds). It’s given as `3600.5` seconds (1 hour + 0.5 sec).

## 6. **Set and FrozenSet**

- `tags`: A set ensures all elements are unique (`["python", "fastapi", "backend"]` after removing duplicates).
- `permissions`: A `FrozenSet` behaves similarly to a set but is immutable (same as `tags`).

## 7. **Bytes**

- `data`: It uses a `bytes` type. In the request, it is given as a Base64 encoded string, which the system interprets correctly.

## 8. **Decimal**

- `balance`: Using `Decimal` ensures high precision when dealing with floating-point values (like monetary data).

## 9. **Optional[bool]**

- `is_active`: This field is optional, meaning it can be either `True`, `False`, or `None`.  
