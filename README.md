# Tiny Chess and Tech Websites

This is a beginner-friendly Python project for kids ages 6-12. It creates two simple websites:

- `/chess` for a fast moving chess-themed game called Knight Dash
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

### `HOST = "127.0.0.1"` and `PORT = 8000`

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

### `CHESS_PAGE = chess_game()`

The project now uses `CHESS_PAGE = chess_game()`.

That means the chess page is special. It is not just a fact page. It has HTML, CSS, and JavaScript for a playable game.

## Knight Dash Game Notes

### Game Goal

The player controls the knight marked `N`.

- Collect `*` stars to gain points.
- Dodge `P` pawns.
- The game gets faster as the score grows.

### `def chess_game():`

This Python function returns one big HTML page. Inside the page are three web languages:

- HTML makes the buttons, score, and board.
- CSS makes the board colorful.
- JavaScript makes the game move.

### `const board = document.getElementById("board")`

JavaScript uses this line to find the board on the page. After it finds the board, it can add squares and pieces to it.

### `let knight`, `let star`, and `let pawns`

These variables remember where the game pieces are.

- `knight` stores the player's square.
- `star` stores the point square.
- `pawns` stores a list of moving enemies.

### `function randomSpot()`

This function picks a random square on the board. It uses `Math.random()` to choose a number.

### `function sameSpot(a, b)`

This checks whether two pieces are standing on the same square.

### `function newGame()`

This resets the score, lives, knight, star, and pawns. It also starts the pawn timer.

### `setInterval(movePawns, 650)`

This tells JavaScript to run `movePawns` again and again. That is what makes the game feel alive.

### `function drawBoard()`

This redraws the chess board. It uses two loops:

- one loop for rows
- one loop for columns

Together, they make 64 squares.

### `function moveKnight(dx, dy)`

This moves the knight.

- `dx` means left or right.
- `dy` means up or down.

The code uses `Math.max` and `Math.min` to keep the knight inside the board.

### `function movePawns()`

This moves each pawn closer to the knight. Sometimes the pawn moves sideways. Sometimes it moves up or down.

### `function checkGame()`

This checks the rules:

- Did the knight collect a star?
- Did a pawn tag the knight?
- Did the player run out of lives?

### `document.addEventListener("keydown", ...)`

This listens for keyboard presses. When the player presses an arrow key, the knight moves.

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

### `try` and `except`

This prints the website address when Python has a normal terminal. If Python is started in the background and cannot print, `except` keeps the website running.

### `server.serve_forever()`

This keeps the website awake until we stop it.

## Student Challenges

1. Change the chess page color.
2. Change how many lives the player starts with.
3. Add one new tech fact.
4. Make the pawns even faster.
