from flask import Flask, jsonify, render_template, request
from timetable_generator import timetable_generator

app = Flask(__name__)

generator = timetable_generator()

# Generate initial timetable
generator.generate_timetable()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate")
def generate():

    timetable = generator.generate_timetable()

    return jsonify({
        "success": True,
        "timetable": timetable,
        "statistics": generator.get_statistics(),
        "faculty_workload": generator.get_faculty_workload(),
        "room_utilization": generator.get_room_utilization(),
        "department_statistics": generator.get_department_statistics(),
        "conflicts": generator.get_conflict_details()
    })


@app.route("/statistics")
def statistics():

    return jsonify({
        "statistics": generator.get_statistics(),
        "faculty_workload": generator.get_faculty_workload(),
        "room_utilization": generator.get_room_utilization(),
        "department_statistics": generator.get_department_statistics()
    })


@app.route("/conflicts")
def conflicts():

    return jsonify(generator.get_conflict_details())


@app.route("/department/<dept>")
def department_filter(dept):

    result = generator.filter_department(dept.upper())

    return jsonify(result)


@app.route("/search")
def search():

    course = request.args.get("course", "")

    result = generator.search_course(course)

    return jsonify(result)


@app.route("/faculty")
def faculty():

    return jsonify(generator.get_faculty_workload())


@app.route("/rooms")
def rooms():

    return jsonify(generator.get_room_utilization())


@app.route("/departments")
def departments():

    return jsonify(generator.get_department_statistics())


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5002
    )