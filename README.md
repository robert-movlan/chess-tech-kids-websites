# Tiny Chess and Tech Websites

This is a beginner-friendly Python project for kids ages 6-12. It creates two simple websites:

- `/chess` for a chess puzzle game called Chess IQ Lab
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

That means the chess page is special. It is not just a fact page. It has HTML, CSS, and JavaScript for a playable puzzle board.

## Chess IQ Lab Notes

### Game Goal

The player solves chess thinking puzzles.

- Click a piece.
- Click the best target square.
- Press `Check Move`.
- Learn the pattern: fork, checkmate, pin, skewer, or defender.

### `def chess_game():`

This Python function returns one big HTML page. Inside the page are three web languages:

- HTML makes the buttons, score, and board.
- CSS makes the board colorful.
- JavaScript checks the puzzle answers.

### `const board = document.getElementById("board")`

JavaScript uses this line to find the board on the page. After it finds the board, it can draw the 64 squares and the chess pieces.

### `const puzzles = [...]`

This list stores the chess puzzles.

Each puzzle has:

- a title
- a pattern name
- a short story
- a hint
- the correct answer
- an explanation
- the pieces on the board

### `pieces: { e1: "K", f7: "N" }`

This means, "put a white king on e1 and a white knight on f7."

Uppercase letters are White pieces. Lowercase letters are Black pieces.

### `answer: "f7d6"`

This means the correct move starts on `f7` and ends on `d6`.

### `function squareToPoint(square)`

This turns a chess square like `e4` into grid numbers the computer can use.

### `function drawBoard()`

This redraws the chess board. It uses two loops:

- one loop for rows
- one loop for columns

Together, they make 64 squares.

### `function chooseSquare(squareName)`

This handles clicking.

- The first click chooses the piece.
- The second click chooses where the piece should go.

### `function checkAnswer()`

This compares the student's move to the correct answer.

- Correct moves earn IQ points.
- Correct streaks earn bonus points.
- Wrong moves reset the streak but let the student try again.

### `function showHint()`

This shows a clue without giving away the full answer.

### `function showAnswer()`

This shows the correct move and explains the chess idea.

### `function nextPuzzle()`

This moves the class to the next chess challenge.

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
2. Add a new puzzle to the `puzzles` list.
3. Add one new tech fact.
4. Change how many IQ points a correct answer gives.
