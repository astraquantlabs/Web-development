from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simple AI logic
def brain(text):
    text = text.lower()

    if "hello" in text:
        return "Hello 👋 I am AstraQuant AI."
    if "time" in text:
        import datetime
        return str(datetime.datetime.now())
    
    return "I am still learning... 🤖"

# Home page (frontend inside Python)
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AstraQuant Python AI</title>
        <style>
            body { background:black; color:#00ffcc; font-family:monospace; }
            input { padding:10px; width:70%; }
            button { padding:10px; }
        </style>
    </head>
    <body>

    <h2>🌑 AstraQuant Python AI</h2>

    <div id="chat"></div>

    <input id="msg" placeholder="Ask something..." />
    <button onclick="send()">Send</button>

    <script>
    async function send() {
        let msg = document.getElementById("msg").value;

        let res = await fetch("/chat", {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({message: msg})
        });

        let data = await res.json();

        document.getElementById("chat").innerHTML += 
            "<p>You: " + msg + "</p>" +
            "<p>AI: " + data.reply + "</p>";
    }
    </script>

    </body>
    </html>
    """)

# API route
@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]
    reply = brain(user)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)