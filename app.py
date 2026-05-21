"""
Tiny Two-Website Python Project

Audience: kids ages 6-12 learning how a Python web server works.

Run this file, then open:
  http://localhost:8000/chess
  http://localhost:8000/tech

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
          </div>
        </main>
      </body>
    </html>
    """


# SECTION 4: Create our two tiny websites.
# Each variable stores one finished HTML page.
CHESS_PAGE = page(
    "Chess Club",
    "Chess Club",
    "Chess is a thinking game. Every move is like a tiny plan.",
    [
        "The king is important, so keep it safe.",
        "Pawns move slowly, but they can become powerful.",
        "A good player asks: what can my opponent do next?",
    ],
    "#2f6f4e",
)

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


# SECTION 5: Teach the server how to answer browser requests.
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


# SECTION 6: Start the app.
# This only runs when we start the file directly with: python app.py
if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), WebsiteHandler)
    print(f"Visit http://{HOST}:{PORT}/chess or http://{HOST}:{PORT}/tech")
    server.serve_forever()
