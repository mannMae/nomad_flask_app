# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs
# from file import save_to_file
from flask import Flask, render_template

# keyword = input("Keyword?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)

app = Flask("JobScrapper")

@app.route("/")
def home():
    # return "<h1>HIHI</h1><a href='/hello'>go to hello</a>"
    return render_template("index.html", name="JM")

@app.route("/search")
def hello():
    return render_template("search.html")

app.run("")