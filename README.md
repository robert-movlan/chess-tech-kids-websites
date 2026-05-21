# Tiny Chess and Tech Websites

This is a beginner-friendly Python project for kids ages 6-12. It creates two simple websites:

- `/chess` for a Chess Club page
- `/tech` for a Tech Lab page

The project uses only Python's built-in `http.server` module, so there are no extra packages to install.

## How To Run

```bash
python app.py
```

Then open:

- <http://127.0.0.1:8000/chess>
- <http://127.0.0.1:8000/tech>

Stop the server with `Ctrl + C`.

## Class Teaching Notes

### `from http.server import BaseHTTPRequestHandler, HTTPServer`

This line borrows web server tools that are already inside Python.

- `HTTPServer` listens for browser visits.
- `BaseHTTPRequestHandler` helps us decide what to send back.

### `HOST = "localhost"` and `PORT = 8000`

These variables tell Python where the website lives on our computer.

- `127.0.0.1` means "this computer."
- `8000` is the door number the browser knocks on.

### `def page(...)`

This function builds a whole HTML page. Instead of writing the same page shape twice, we reuse one function.

The function receives:

- `title` for the browser tab
- `heading` for the big page title
- `message` for a short paragraph
- `items` for bullet points
- `color` for the header color

### `for item in items`

This loop reads every fact in a Python list and turns it into an HTML bullet.

### `f""" ... """`

This is an f-string. It lets Python place variable values inside a big piece of text.

Example:

```python
name = "Ada"
print(f"Hello, {name}!")
```

Python prints:

```text
Hello, Ada!
```

### `CHESS_PAGE = page(...)`

This creates the chess website by calling the `page` function.

### `TECH_PAGE = page(...)`

This creates the tech website by calling the same function with different words and a different color.

### `class WebsiteHandler(BaseHTTPRequestHandler)`

This class is the rulebook for the server. It explains what should happen when someone visits a page.

### `def do_GET(self)`

Browsers usually use `GET` when they ask for a page. This method checks the path:

- `/` or `/chess` shows the chess page
- `/tech` shows the tech page
- anything else shows a 404 error

### `send_response(200)`

The number `200` means "OK, the page worked."

### `send_header("Content-type", "text/html")`

This tells the browser, "The thing I am sending is HTML."

### `html.encode("utf-8")`

Computers send bytes over the internet. This turns our text into bytes.

### `if __name__ == "__main__":`

This means "only start the server when this file is run directly."

### `server.serve_forever()`

This keeps the website awake until we stop it.

## Student Challenges

1. Change the chess page color.
2. Add one new chess fact.
3. Add one new tech fact.
4. Make a third page called `/robots`.
