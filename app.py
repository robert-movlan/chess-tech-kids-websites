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


# SECTION 4: Create the moving chess game page.
# This function returns one full HTML page with CSS and JavaScript inside it.
def chess_game():
    """
    Build a fast little game called Knight Dash.

    The player moves the knight with arrow keys, collects stars for points,
    and avoids moving pawns. This is not full chess yet. It is a playful first
    step that teaches kids the idea of a board, pieces, score, and events.
    """

    return """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Knight Dash</title>
        <style>
          body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f7f4ec;
            color: #202020;
          }
          header {
            background: #2f6f4e;
            color: white;
            padding: 18px;
            text-align: center;
          }
          nav a {
            color: white;
            font-weight: bold;
            margin: 0 8px;
          }
          main {
            max-width: 760px;
            margin: 18px auto;
            padding: 0 16px;
          }
          .scoreboard {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 12px;
            font-weight: bold;
          }
          .scoreboard div {
            background: white;
            border: 2px solid #202020;
            border-radius: 8px;
            padding: 10px;
            flex: 1;
            text-align: center;
          }
          #board {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            width: min(92vw, 560px);
            aspect-ratio: 1;
            margin: 0 auto;
            border: 4px solid #202020;
          }
          .square {
            display: grid;
            place-items: center;
            font-size: clamp(20px, 7vw, 44px);
            font-weight: bold;
            user-select: none;
          }
          .light {
            background: #f0d9b5;
          }
          .dark {
            background: #b58863;
          }
          .knight {
            color: #183a7a;
            text-shadow: 0 2px white;
          }
          .pawn {
            color: #7a1d1d;
          }
          .star {
            color: #d49a00;
          }
          .controls {
            display: grid;
            grid-template-columns: repeat(3, 58px);
            gap: 8px;
            justify-content: center;
            margin: 14px 0;
          }
          button {
            height: 48px;
            border: 2px solid #202020;
            border-radius: 8px;
            background: white;
            font-size: 22px;
            font-weight: bold;
          }
          .wide {
            grid-column: span 3;
            width: 100%;
          }
          #message {
            text-align: center;
            font-weight: bold;
            min-height: 24px;
          }
        </style>
      </head>
      <body>
        <header>
          <h1>Knight Dash</h1>
          <nav>
            <a href="/chess">Chess Game</a>
            <a href="/tech">Tech Site</a>
          </nav>
        </header>

        <main>
          <div class="scoreboard">
            <div>Score: <span id="score">0</span></div>
            <div>Lives: <span id="lives">3</span></div>
            <div>Speed: <span id="speed">1</span></div>
          </div>

          <div id="board"></div>

          <div class="controls">
            <span></span>
            <button onclick="moveKnight(0, -1)">^</button>
            <span></span>
            <button onclick="moveKnight(-1, 0)">&lt;</button>
            <button onclick="newGame()">Go</button>
            <button onclick="moveKnight(1, 0)">&gt;</button>
            <span></span>
            <button onclick="moveKnight(0, 1)">v</button>
            <span></span>
            <button class="wide" onclick="newGame()">New Game</button>
          </div>

          <p id="message">Collect stars. Dodge the pawns.</p>
        </main>

        <script>
          // SECTION A: These variables remember the game state.
          const board = document.getElementById("board");
          const scoreText = document.getElementById("score");
          const livesText = document.getElementById("lives");
          const speedText = document.getElementById("speed");
          const message = document.getElementById("message");
          const size = 8;

          let knight;
          let star;
          let pawns;
          let score;
          let lives;
          let speed;
          let timer;

          // SECTION B: Pick a random board square.
          function randomSpot() {
            return {
              x: Math.floor(Math.random() * size),
              y: Math.floor(Math.random() * size)
            };
          }

          // SECTION C: Check if two pieces are on the same square.
          function sameSpot(a, b) {
            return a.x === b.x && a.y === b.y;
          }

          // SECTION D: Start or restart the game.
          function newGame() {
            knight = { x: 3, y: 6 };
            star = randomSpot();
            pawns = [
              { x: 0, y: 0 },
              { x: 4, y: 1 },
              { x: 7, y: 2 }
            ];
            score = 0;
            lives = 3;
            speed = 1;
            clearInterval(timer);
            timer = setInterval(movePawns, 650);
            message.textContent = "Collect stars. Dodge the pawns.";
            drawBoard();
          }

          // SECTION E: Draw the 8 by 8 board.
          function drawBoard() {
            board.innerHTML = "";

            for (let y = 0; y < size; y++) {
              for (let x = 0; x < size; x++) {
                const square = document.createElement("div");
                square.className = "square " + ((x + y) % 2 === 0 ? "light" : "dark");

                if (sameSpot(knight, { x: x, y: y })) {
                  square.textContent = "N";
                  square.classList.add("knight");
                } else if (sameSpot(star, { x: x, y: y })) {
                  square.textContent = "*";
                  square.classList.add("star");
                } else {
                  for (const pawn of pawns) {
                    if (sameSpot(pawn, { x: x, y: y })) {
                      square.textContent = "P";
                      square.classList.add("pawn");
                    }
                  }
                }

                board.appendChild(square);
              }
            }

            scoreText.textContent = score;
            livesText.textContent = lives;
            speedText.textContent = speed;
          }

          // SECTION F: Move the knight with buttons or arrow keys.
          function moveKnight(dx, dy) {
            knight.x = Math.max(0, Math.min(size - 1, knight.x + dx));
            knight.y = Math.max(0, Math.min(size - 1, knight.y + dy));
            checkGame();
            drawBoard();
          }

          // SECTION G: Move every pawn toward the knight.
          function movePawns() {
            for (const pawn of pawns) {
              if (Math.random() < 0.5) {
                pawn.x += Math.sign(knight.x - pawn.x);
              } else {
                pawn.y += Math.sign(knight.y - pawn.y);
              }
            }

            checkGame();
            drawBoard();
          }

          // SECTION H: Handle stars, hits, and game over.
          function checkGame() {
            if (sameSpot(knight, star)) {
              score += 10;
              star = randomSpot();
              message.textContent = "Nice move!";

              if (score % 30 === 0) {
                speed += 1;
                clearInterval(timer);
                timer = setInterval(movePawns, Math.max(180, 650 - speed * 70));
              }
            }

            for (const pawn of pawns) {
              if (sameSpot(knight, pawn)) {
                lives -= 1;
                knight = { x: 3, y: 6 };
                message.textContent = "A pawn tagged you!";
              }
            }

            if (lives <= 0) {
              clearInterval(timer);
              message.textContent = "Game over. Press New Game.";
            }
          }

          // SECTION I: Listen for keyboard arrows.
          document.addEventListener("keydown", function(event) {
            if (event.key === "ArrowUp") {
              moveKnight(0, -1);
            } else if (event.key === "ArrowDown") {
              moveKnight(0, 1);
            } else if (event.key === "ArrowLeft") {
              moveKnight(-1, 0);
            } else if (event.key === "ArrowRight") {
              moveKnight(1, 0);
            }
          });

          newGame();
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
