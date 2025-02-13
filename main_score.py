from flask import Flask
from utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            content = file.read().strip()
            if not content.isdigit():
                raise ValueError("Invalid score format")
            score = content

        # Return the HTML with the score
        return f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    except (FileNotFoundError, IOError, ValueError) as e:
        # Return the error message in HTML if there is an issue
        error_message = f"Error: {str(e)}"
        return f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">{error_message}</div></h1>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run("0.0.0.0", port=8777, debug=True)
