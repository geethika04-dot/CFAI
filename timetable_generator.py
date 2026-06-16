import random
from collections import defaultdict

class timetable_generator:

    def __init__(self):

        self.departments = {
            "CS": ["CS101", "CS102", "CS201", "CS202"],
            "MATH": ["MTH101", "MTH102", "MTH201", "MTH202"],
            "PHY": ["PHY101", "PHY102", "PHY201", "PHY202"],
            "EE": ["EE101", "EE102", "EE201", "EE202"],
            "ME": ["ME101", "ME102", "ME201", "ME202"],
            "BIO": ["BIO101", "BIO102", "BIO201", "BIO202"]
        }

        self.faculty = [
            "Dr Smith",
            "Dr Johnson",
            "Dr Williams",
            "Dr Brown",
            "Dr Jones",
            "Dr Garcia",
            "Dr Miller",
            "Dr Davis",
            "Dr Rodriguez",
            "Dr Martinez",
            "Dr Anderson",
            "Dr Thomas",
            "Dr Taylor",
            "Dr Moore",
            "Dr Jackson",
            "Dr Martin",
            "Dr Lee",
            "Dr White"
        ]

        self.rooms = [
            "R101", "R102", "R103",
            "R104", "R105", "R106",
            "R201", "R202", "R203",
            "R204", "R205", "R206",
            "LAB1", "LAB2", "LAB3"
        ]

        self.days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ]

        self.slots = [
            "09:00-10:00",
            "10:00-11:00",
            "11:00-12:00",
            "01:00-02:00",
            "02:00-03:00"
        ]

        self.schedule = []

    def generate_timetable(self):

        self.schedule = []

        for dept, courses in self.departments.items():

            for course in courses:

                day = random.choice(self.days)
                slot = random.choice(self.slots)
                room = random.choice(self.rooms)
                faculty = random.choice(self.faculty)

                self.schedule.append({
                    "department": dept,
                    "course": course,
                    "faculty": faculty,
                    "room": room,
                    "day": day,
                    "time": slot
                })

        return self.schedule

    def get_conflict_details(self):

        conflicts = []

        room_usage = {}
        faculty_usage = {}

        for item in self.schedule:

            room_key = (
                item["room"],
                item["day"],
                item["time"]
            )

            faculty_key = (
                item["faculty"],
                item["day"],
                item["time"]
            )

            if room_key in room_usage:
                conflicts.append({
                    "type": "Room Conflict",
                    "room": item["room"],
                    "day": item["day"],
                    "time": item["time"]
                })

            room_usage[room_key] = True

            if faculty_key in faculty_usage:
                conflicts.append({
                    "type": "Faculty Conflict",
                    "faculty": item["faculty"],
                    "day": item["day"],
                    "time": item["time"]
                })

            faculty_usage[faculty_key] = True

        return conflicts

    def get_statistics(self):

        conflicts = self.get_conflict_details()

        return {
            "total_courses": len(self.schedule),
            "total_faculty": len(self.faculty),
            "total_rooms": len(self.rooms),
            "conflicts": len(conflicts)
        }

    def get_faculty_workload(self):

        workload = defaultdict(int)

        for item in self.schedule:
            workload[item["faculty"]] += 1

        return dict(workload)

    def get_room_utilization(self):

        utilization = defaultdict(int)

        for item in self.schedule:
            utilization[item["room"]] += 1

        total_slots = len(self.days) * len(self.slots)

        result = {}

        for room in self.rooms:

            used = utilization[room]

            percent = round(
                (used / total_slots) * 100,
                2
            )

            result[room] = percent

        return result

    def get_department_statistics(self):

        stats = {}

        for dept in self.departments:

            count = 0

            for item in self.schedule:
                if item["department"] == dept:
                    count += 1

            stats[dept] = count

        return stats

    def search_course(self, course_name):

        results = []

        for item in self.schedule:

            if course_name.lower() in item["course"].lower():
                results.append(item)

        return results

    def filter_department(self, department):

        results = []

        for item in self.schedule:

            if item["department"] == department:
                results.append(item)

        return results