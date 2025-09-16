from flask import Flask, render_template_string
import random
from rich.console import Console
from rich.text import Text

console = Console()

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated."
]

signature = "✨ Crafted with ❤️ by Narendra Singh Kholiya ✨"

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Quotes App</title>
    <style>
      body { font-family: Arial, sans-serif; text-align: center; margin-top: 10%; background: #f8f9fa; }
      .quote { font-size: 1.5rem; color: #333; }
      .author { margin-top: 1rem; color: #8e44ad; font-weight: bold; }
    </style>
  </head>
  <body>
    <h1 class="quote">{{ quote }}</h1>
    <p class="author">{{ signature }}</p>
  </body>
</html>
"""

@app.route("/")
def home():
    q = random.choice(quotes)
    console.print(f"[bold cyan]Serving quote:[/] {q}")
    return render_template_string(HTML, quote=q, signature=signature)

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it’s accessible from outside the container
    app.run(host="0.0.0.0", port=8080, debug=False)
