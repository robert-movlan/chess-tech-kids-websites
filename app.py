"""
Tiny Two-Website Python Project

Audience: kids ages 6-12 learning how a Python web server works.

Run this file, then open:
  http://127.0.0.1:8000/chess
  http://127.0.0.1:8000/tech

This project uses only Python's built-in tools. No Flask, no Django, no
extra installs. That keeps the code small enough to explain in class.
"""

# SECTION 1: Import tools Python already has.
# http.server gives us small building blocks for making a web server.
from http.server import BaseHTTPRequestHandler, HTTPServer


# SECTION 2: Save the server address in variables.
# A variable is a name that remembers a value.
HOST = "127.0.0.1"
PORT = 8000


# SECTION 3: Make one helper function that wraps every page in the same style.
# A function is a reusable mini-machine: give it information, get a result back.
def page(title, heading, message, items, color):
    """
    Build a full HTML page.

    title: text shown on the browser tab
    heading: big text at the top of the page
    message: short paragraph for the page
    items: a Python list of facts to show as bullet points
    color: the main page color
    """

    # This loop turns each list item into an HTML <li> bullet.
    bullets = ""
    for item in items:
        bullets = bullets + f"<li>{item}</li>"

    # f"""...""" is an f-string. It lets us place variables inside text.
    return f"""
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>{title}</title>
        <style>
          body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f7f4ec;
            color: #202020;
          }}
          header {{
            background: {color};
            color: white;
            padding: 28px;
            text-align: center;
          }}
          main {{
            max-width: 720px;
            margin: 24px auto;
            padding: 0 18px;
          }}
          nav a {{
            display: inline-block;
            margin: 8px;
            color: white;
            font-weight: bold;
          }}
          .box {{
            background: white;
            border: 2px solid #202020;
            border-radius: 8px;
            padding: 20px;
          }}
          li {{
            margin: 10px 0;
          }}
          .button {{
            display: inline-block;
            margin-top: 12px;
            padding: 10px 14px;
            background: {color};
            color: white;
            border-radius: 6px;
            text-decoration: none;
          }}
        </style>
      </head>
      <body>
        <header>
          <h1>{heading}</h1>
          <nav>
            <a href="/chess">Chess Site</a>
            <a href="/tech">Tech Site</a>
          </nav>
        </header>
        <main>
          <div class="box">
            <p>{message}</p>
            <ul>{bullets}</ul>
            <a class="button" href="/chess">Play the chess game</a>
          </div>
        </main>
      </body>
    </html>
    """


# SECTION 4: Create the chess IQ puzzle page.
# This function returns one full HTML page with CSS and JavaScript inside it.
def chess_game():
    """
    Build a smart puzzle game called Chess IQ Lab.

    Kids click a piece, then click where it should move. The app checks the
    answer, gives hints, and explains the chess idea behind the best move.
    """

    return """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Chess IQ Lab</title>
        <style>
          body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f0e6;
            color: #1f2523;
          }
          header {
            background: #26483f;
            color: white;
            padding: 18px 14px;
            text-align: center;
          }
          nav a {
            color: white;
            font-weight: bold;
            margin: 0 8px;
          }
          main {
            max-width: 980px;
            margin: 18px auto;
            padding: 0 16px;
          }
          .layout {
            display: grid;
            grid-template-columns: minmax(280px, 560px) minmax(250px, 1fr);
            gap: 18px;
            align-items: start;
          }
          .scoreboard {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px;
            font-weight: bold;
          }
          .scoreboard div {
            background: white;
            border: 2px solid #202020;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
          }
          .panel {
            background: white;
            border: 2px solid #202020;
            border-radius: 8px;
            padding: 14px;
          }
          .panel h2 {
            margin: 0 0 8px;
            font-size: 22px;
          }
          .tag {
            display: inline-block;
            background: #e7f0ec;
            border: 1px solid #26483f;
            border-radius: 6px;
            padding: 5px 8px;
            font-weight: bold;
            margin-bottom: 8px;
          }
          #board {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            width: min(92vw, 560px);
            aspect-ratio: 1;
            margin: 0;
            border: 4px solid #202020;
          }
          .square {
            display: grid;
            place-items: center;
            font-size: clamp(20px, 7vw, 44px);
            font-weight: bold;
            user-select: none;
            position: relative;
            cursor: pointer;
          }
          .light {
            background: #f1d9b5;
          }
          .dark {
            background: #9f704d;
          }
          .selected {
            outline: 4px solid #1b61d1;
            outline-offset: -4px;
          }
          .target {
            box-shadow: inset 0 0 0 5px #e0a400;
          }
          .last {
            box-shadow: inset 0 0 0 5px #2b8a3e;
          }
          .white-piece {
            color: #fdfdfd;
            text-shadow: 0 2px 2px #111;
          }
          .black-piece {
            color: #121212;
            text-shadow: 0 1px 1px white;
          }
          .coords {
            bottom: 3px;
            font-size: 10px;
            left: 4px;
            opacity: 0.65;
            position: absolute;
          }
          .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 14px 0;
          }
          button {
            min-height: 42px;
            border: 2px solid #202020;
            border-radius: 8px;
            background: white;
            padding: 8px 12px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
          }
          button.primary {
            background: #26483f;
            color: white;
          }
          #moveText {
            font-family: Consolas, monospace;
            font-size: 20px;
            font-weight: bold;
          }
          #message {
            background: #fff8d7;
            border: 2px solid #9f704d;
            border-radius: 8px;
            font-weight: bold;
            min-height: 24px;
            padding: 10px;
          }
          #explain {
            line-height: 1.45;
          }
          .meter {
            background: #ddd2bd;
            border: 2px solid #202020;
            border-radius: 8px;
            height: 18px;
            overflow: hidden;
          }
          #meterFill {
            background: #2b8a3e;
            height: 100%;
            width: 0%;
          }
          @media (max-width: 820px) {
            .layout {
              grid-template-columns: 1fr;
            }
            #board {
              margin: 0 auto;
            }
          }
        </style>
      </head>
      <body>
        <header>
          <h1>Chess IQ Lab</h1>
          <nav>
            <a href="/chess">Chess IQ Lab</a>
            <a href="/tech">Tech Site</a>
          </nav>
        </header>

        <main>
          <div class="scoreboard">
            <div>IQ Points: <span id="score">0</span></div>
            <div>Streak: <span id="streak">0</span></div>
            <div>Puzzle: <span id="level">1</span>/5</div>
          </div>

          <div class="layout">
            <div id="board"></div>

            <section class="panel">
              <span class="tag" id="pattern">Pattern</span>
              <h2 id="title">Find the best move</h2>
              <p id="story"></p>
              <p>Selected move: <span id="moveText">none</span></p>
              <div class="meter"><div id="meterFill"></div></div>
              <div class="controls">
                <button class="primary" onclick="checkAnswer()">Check Move</button>
                <button onclick="showHint()">Hint</button>
                <button onclick="showAnswer()">Show Answer</button>
                <button onclick="nextPuzzle()">Next Puzzle</button>
                <button onclick="resetLab()">Restart Lab</button>
              </div>
              <p id="message">Click a piece, then click its best square.</p>
              <p id="explain"></p>
            </section>
          </div>
        </main>

        <script>
          // SECTION A: These variables connect JavaScript to HTML boxes.
          const board = document.getElementById("board");
          const scoreText = document.getElementById("score");
          const streakText = document.getElementById("streak");
          const levelText = document.getElementById("level");
          const titleText = document.getElementById("title");
          const storyText = document.getElementById("story");
          const patternText = document.getElementById("pattern");
          const moveText = document.getElementById("moveText");
          const message = document.getElementById("message");
          const explain = document.getElementById("explain");
          const meterFill = document.getElementById("meterFill");

          // SECTION B: These puzzles are the brain of the game.
          // Uppercase pieces are White. Lowercase pieces are Black.
          const puzzles = [
            {
              title: "White to move: win the queen",
              pattern: "Fork",
              story: "A knight can attack two important pieces at once. Which knight jump attacks the black king and queen?",
              hint: "Knights move in an L shape. Look for a square that attacks e8 and d7.",
              answer: "f7d6",
              explain: "Nf7-d6+ is a fork. The knight checks the king on e8 and attacks the queen on d7, so White wins material.",
              pieces: { e1: "K", f7: "N", a1: "R", e8: "k", d7: "q", a8: "r" }
            },
            {
              title: "White to move: mate in one",
              pattern: "Checkmate",
              story: "The black king is trapped. Find the queen move that gives checkmate.",
              hint: "The queen wants to stand next to the king on h7, protected by the white king line and bishop.",
              answer: "h5h7",
              explain: "Qh5-h7# attacks the king. The king cannot capture the queen or escape, so it is checkmate.",
              pieces: { g1: "K", h5: "Q", c2: "B", h8: "k", g7: "p", f7: "p" }
            },
            {
              title: "White to move: pin the knight",
              pattern: "Pin",
              story: "A pinned piece is stuck because moving it would expose something more valuable.",
              hint: "Use the bishop to aim through the knight toward the king.",
              answer: "c4b5",
              explain: "Bc4-b5 pins the knight on c6 to the king on e8. The knight becomes hard to move.",
              pieces: { e1: "K", c4: "B", d1: "Q", e8: "k", c6: "n", d7: "q" }
            },
            {
              title: "White to move: skewer the king",
              pattern: "Skewer",
              story: "A skewer attacks a valuable piece first. When it moves, another piece behind it is lost.",
              hint: "Put the rook on the open e-file.",
              answer: "a1e1",
              explain: "Ra1-e1+ checks the king on e8. When the king moves, the queen on e7 is behind it.",
              pieces: { g1: "K", a1: "R", e8: "k", e7: "q", a8: "r" }
            },
            {
              title: "White to move: remove the defender",
              pattern: "Defender",
              story: "Sometimes the smartest move is to capture the piece that protects the target.",
              hint: "The black knight protects the bishop. Can your queen capture that defender?",
              answer: "d1d7",
              explain: "Qd1-d7+ removes a key defender and gives check. White wins a strong piece and keeps the attack.",
              pieces: { g1: "K", d1: "Q", c4: "B", g5: "N", g8: "k", d7: "n", c8: "b", h7: "p" }
            }
          ];

          let puzzleNumber = 0;
          let selected = "";
          let chosenMove = "";
          let score = 0;
          let streak = 0;

          // SECTION C: Turn a board square like "e4" into row and column numbers.
          function squareToPoint(square) {
            const files = "abcdefgh";
            return {
              x: files.indexOf(square[0]),
              y: 8 - Number(square[1])
            };
          }

          // SECTION D: Turn row and column numbers back into a board square.
          function pointToSquare(x, y) {
            const files = "abcdefgh";
            return files[x] + (8 - y);
          }

          // SECTION E: Draw the board from the current puzzle.
          function drawBoard() {
            board.innerHTML = "";
            const puzzle = puzzles[puzzleNumber];

            for (let y = 0; y < 8; y++) {
              for (let x = 0; x < 8; x++) {
                const name = pointToSquare(x, y);
                const square = document.createElement("div");
                square.className = "square " + ((x + y) % 2 === 0 ? "light" : "dark");
                square.onclick = function() {
                  chooseSquare(name);
                };

                if (name === selected) {
                  square.classList.add("selected");
                }
                if (chosenMove.slice(2, 4) === name) {
                  square.classList.add("target");
                }
                if (chosenMove === puzzle.answer && puzzle.answer.includes(name)) {
                  square.classList.add("last");
                }

                if (puzzle.pieces[name]) {
                  const piece = puzzle.pieces[name];
                  square.textContent = piece;
                  square.classList.add(piece === piece.toUpperCase() ? "white-piece" : "black-piece");
                }

                const coords = document.createElement("span");
                coords.className = "coords";
                coords.textContent = name;
                square.appendChild(coords);
                board.appendChild(square);
              }
            }
          }

          // SECTION F: Load one puzzle into the lesson panel.
          function showPuzzle() {
            const puzzle = puzzles[puzzleNumber];
            selected = "";
            chosenMove = "";
            titleText.textContent = puzzle.title;
            storyText.textContent = puzzle.story;
            patternText.textContent = puzzle.pattern;
            moveText.textContent = "none";
            message.textContent = "Click a piece, then click its best square.";
            explain.textContent = "";
            levelText.textContent = puzzleNumber + 1;
            scoreText.textContent = score;
            streakText.textContent = streak;
            meterFill.style.width = ((puzzleNumber) / puzzles.length * 100) + "%";
            drawBoard();
          }

          // SECTION G: Click logic. First click chooses a piece. Second click chooses its target.
          function chooseSquare(squareName) {
            const puzzle = puzzles[puzzleNumber];

            if (selected === "") {
              if (puzzle.pieces[squareName]) {
                selected = squareName;
                chosenMove = "";
                moveText.textContent = selected + " -> ?";
                message.textContent = "Now choose the square for that piece.";
              } else {
                message.textContent = "Choose a square that has a piece.";
              }
            } else {
              chosenMove = selected + squareName;
              moveText.textContent = selected + " -> " + squareName;
              message.textContent = "Good. Now press Check Move.";
            }

            drawBoard();
          }

          // SECTION H: Check the student's move.
          function checkAnswer() {
            const puzzle = puzzles[puzzleNumber];

            if (chosenMove === puzzle.answer) {
              score += 10 + streak * 2;
              streak += 1;
              message.textContent = "Correct. That is a smart chess idea.";
              explain.textContent = puzzle.explain;
              scoreText.textContent = score;
              streakText.textContent = streak;
              meterFill.style.width = ((puzzleNumber + 1) / puzzles.length * 100) + "%";
            } else if (chosenMove === "") {
              message.textContent = "Pick a move first.";
            } else {
              streak = 0;
              message.textContent = "Not quite. Try to find the pattern: " + puzzle.pattern + ".";
              explain.textContent = "Use the hint if you are stuck.";
              streakText.textContent = streak;
            }
          }

          // SECTION I: Give a small clue, but not the full answer.
          function showHint() {
            message.textContent = puzzles[puzzleNumber].hint;
          }

          // SECTION J: Show the answer and explain why it works.
          function showAnswer() {
            const puzzle = puzzles[puzzleNumber];
            selected = puzzle.answer.slice(0, 2);
            chosenMove = puzzle.answer;
            moveText.textContent = selected + " -> " + puzzle.answer.slice(2, 4);
            message.textContent = "Answer shown. Study the idea, then try the next one.";
            explain.textContent = puzzle.explain;
            drawBoard();
          }

          // SECTION K: Move to the next puzzle.
          function nextPuzzle() {
            if (puzzleNumber < puzzles.length - 1) {
              puzzleNumber += 1;
              showPuzzle();
            } else {
              message.textContent = "Lab complete. Final IQ score: " + score + ".";
              explain.textContent = "Restart the lab to practice the patterns again.";
              meterFill.style.width = "100%";
            }
          }

          // SECTION L: Start over from puzzle one.
          function resetLab() {
            puzzleNumber = 0;
            selected = "";
            chosenMove = "";
            score = 0;
            streak = 0;
            showPuzzle();
          }

          showPuzzle();
        </script>
      </body>
    </html>
    """


# SECTION 5: Create our two websites.
# Each variable stores one finished HTML page.
CHESS_PAGE = chess_game()

TECH_PAGE = page(
    "Tech Lab",
    "Tech Lab",
    "Technology is how people use tools, computers, and ideas to solve problems.",
    [
        "Code is a set of instructions for a computer.",
        "Websites are made with HTML, CSS, and sometimes Python.",
        "Debugging means finding and fixing mistakes.",
    ],
    "#315f9c",
)


# SECTION 6: Teach the server how to answer browser requests.
# A class is a blueprint. This one describes how our server should behave.
class WebsiteHandler(BaseHTTPRequestHandler):
    # do_GET runs when a browser asks for a page.
    def do_GET(self):
        if self.path == "/" or self.path == "/chess":
            self.send_page(CHESS_PAGE)
        elif self.path == "/tech":
            self.send_page(TECH_PAGE)
        else:
            self.send_error(404, "Page not found")

    # This helper sends HTML back to the browser.
    def send_page(self, html):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


# SECTION 7: Start the app.
# This only runs when we start the file directly with: python app.py
if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), WebsiteHandler)
    try:
        print(f"Visit http://{HOST}:{PORT}/chess or http://{HOST}:{PORT}/tech")
    except OSError:
        pass
    server.serve_forever()
