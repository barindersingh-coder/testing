from flask import Flask, render_template, request, redirect

app = Flask(__name__)

jobs = {}

@app.route("/", methods=["GET", "POST"])
def create_job():

    if request.method == "POST":

        company = request.form["company"]
        title = request.form["title"]
        description = request.form["description"]
        skills = request.form["skills"]

        job_id = len(jobs) + 1

        jobs[job_id] = {
            "company": company,
            "title": title,
            "description": description,
            "skills": skills
        }

        return redirect(f"/job/{job_id}")

    return render_template("form.html")


@app.route("/job/<int:job_id>")
def job(job_id):

    if job_id not in jobs:
        return "Job Not Found"

    return render_template(
        "job.html",
        job=jobs[job_id]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
