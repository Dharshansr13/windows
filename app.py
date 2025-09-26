from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    quotes = [
        "Believe in yourself, Dharshan!",
        "Every day is a new chance to grow.",
        "Success comes to those who never give up.",
        "Your hard work will pay off, Dharshan.",
        "Stay positive, stay strong!"
    ]
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dharshan's Positive Quotes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f8ff;
                text-align: center;
                margin-top: 100px;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                font-size: 20px;
                color: #16a085;
            }
        </style>
    </head>
    <body>
        <h1>Hello Dharshan 👋</h1>
        <h2>Here are some positive quotes for you:</h2>
        {% for q in quotes %}
            <p>🌟 {{ q }}</p>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, quotes=quotes)

if __name__ == "__main__":
    # Important: use host (not hosts)
    app.run(debug=True, port=5000, host="0.0.0.0")
