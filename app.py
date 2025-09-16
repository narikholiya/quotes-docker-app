# app.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Quotes list
QUOTES = [
    "Believe you can and you're halfway there.",
    "Do what you can, with what you have, where you are.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Happiness depends upon ourselves.",
    "Don't watch the clock; do what it does. Keep going.",
]

CREATOR = "✨ Project created by Narendra Singh Kholiya ✨"


def build_html():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8" />
        <title>Animated Quotes</title>
        <style>
            body {{
                background: linear-gradient(120deg, #84fab0, #8fd3f4);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
            }}
            .container {{
                text-align: center;
                background: rgba(255,255,255,0.85);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                max-width: 600px;
                width: 80%;
            }}
            #quote {{
                font-size: 1.6rem;
                font-weight: 600;
                min-height: 90px;
            }}
            .author {{
                margin-top: 25px;
                font-size: 1rem;
                color: #444;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div id="quote"></div>
            <div class="author">{CREATOR}</div>
        </div>
        <script>
            const quotes = {QUOTES};
            const el = document.getElementById('quote');
            let index = 0;

            function getRandomColor() {{
                const colors = ['#ff6b6b','#6bcdfc','#ffd93d','#6bffb3','#b36bff'];
                return colors[Math.floor(Math.random()*colors.length)];
            }}

            function typeWriter(text, i, fnCallback) {{
                if (i < text.length) {{
                    el.innerHTML = text.substring(0, i+1) + '<span style="opacity:0;">|</span>';
                    setTimeout(() => typeWriter(text, i + 1, fnCallback), 50);
                }} else if (typeof fnCallback === 'function') {{
                    setTimeout(fnCallback, 2000);
                }}
            }}

            function startAnimation() {{
                const quote = quotes[index];
                el.style.color = getRandomColor();
                typeWriter(quote, 0, () => {{
                    index = (index + 1) % quotes.length;
                    setTimeout(startAnimation, 1000);
                }});
            }}

            startAnimation();
        </script>
    </body>
    </html>
    """


@app.get("/", response_class=HTMLResponse)
def home():
    return build_html()
