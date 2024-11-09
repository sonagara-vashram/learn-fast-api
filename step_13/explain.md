# 1. **Setting a Cookie**

- `response.set_cookie`: In FastAPI, the `set_cookie` method of the `Response` object allows you to set a cookie in the client’s browser. It requires a `key` and `value` parameter, where `key` is the name of the cookie and `value` is the data stored in it.
  
## 2. **Getting a Cookie**

- `session_id: str = Cookie(None)`: This syntax defines a parameter `session_id` with the `Cookie` dependency. The `Cookie` function checks if the specified cookie (in this case, `session_id`) exists in the request. If it does, the value is assigned to `session_id`; otherwise, `None` is used as the default.
