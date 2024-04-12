from flask import Flask, render_template, request
from langchain_openai import OpenAI
OPENAI_API_KEY = "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"

app = Flask(__name__)
llm = OpenAI(api_key=OPENAI_API_KEY)
prompt: str = """Step1. Analyze the three provided habits, create a short one paragraph description on tips of how to 
work on these habits 
Step2. Output EXACTLY 3 lines of text in this format, fill in a.i_event_idea_here with a task user 
can use to work on this habit the habit should be a few words only, so that it can be added to a calendar:
const title1 = "a.i1_event_idea_here";
const title2 = "a.i2_event_idea_here";
const title3 = "a.i3_event_idea_here";

Habits:
"""


@app.route("/", methods=["GET", "POST"])
def hello_world():  # put application's code here
    if request.method == "POST":
        habit1 = request.form["habit 1"]
        habit2 = request.form["habit 2"]
        habit3 = request.form["habit 3"]
        response = llm.invoke(prompt + habit1 + habit2 + habit3)  # invoke openAi api call
        message = response

        return render_template("index.html", message=message)
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
