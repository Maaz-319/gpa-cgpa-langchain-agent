COURSES = {
1: [("MS-251", "Probability & Statistics", 3.0),
    ("GE-160", "Applications of ICT", 3.0),
    ("GE-169", "Applied Physics", 3.0),
    ("GE-167", "Discrete Structures", 3.0),
    ("HQ-001", "Quran Translation - I", 0.5),
    ("GE-190", "Functional English", 3.0),],
2: [("CC-112", "Programming Fundamentals", 3.0),
    ("CC-112-L", "Programming Fundamentals Lab", 1.0),
    ("CC-110", "Digital Logic Design", 2.0),
    ("CC-110-L", "Digital Logic Design Lab", 1.0),
    ("MS-252", "Linear Algebra", 3.0),
    ("GE-191", "Expository Writing", 3.0),
    ("GE-163", "Islamic Studies", 2.0),
    ("HQ-002", "Quran Translation - II", 0.5),],
3: [("CC-211", "Object Oriented Programming", 3.0),
    ("CC-211-L", "Object Oriented Programming Lab", 1.0),
    ("CC-215", "Database Systems", 3.0),
    ("CC-215-L", "Database Systems Lab", 1.0),
    ("CC-210", "Computer Organization & Assembly Language", 3.0),
    ("GE-162", "Calculus & Analytical Geometry", 3.0),
    ("GE-192", "Introduction to Management", 2.0),
    ("HQ-003", "Quran Translation - III", 0.5),],
4: [("CC-213", "Data Structures", 3.0),
    ("CC-213-L", "Data Structures Lab", 1.0),
    ("CC-312", "Information Security", 3.0),
    ("CC-214", "Computer Networks", 3.0),
    ("CC-212", "Software Engineering", 3.0),
    ("DC-220", "Advanced Database Management Systems", 3.0),
    ("HQ-004", "Quran Translation - IV", 0.5),],
5: [("CC-313", "Analysis of Algorithms", 3.0),
    ("CC-310", "Artificial Intelligence", 3.0),
    ("DC-320", "Theory of Automata and Formal Languages", 3.0),
    ("DC-321", "Human Computer Interaction", 3.0),
    ("DC-322", "Computer Architecture", 3.0),
    ("EC-330", "Web Technologies / Elective", 3.0),
    ("HQ-005", "Quran Translation - V", 0.5),],
6: [("CC-311", "Operating Systems", 3.0),
    ("EC-333", "Mobile Application Development / Elective", 3.0),
    ("EC-324", "Software Construction & Development / Elective", 3.0),
    ("EC-335", "Machine Learning / Elective", 3.0),
    ("EC-334", "Game Design and Development / Elective", 3.0),
    ("MS-253", "Multivariable Calculus", 3.0),
    ("HQ-006", "Quran Translation - VI", 0.5),],
7: [("CC-411", "Final Year Project - I", 2.0),
    ("DC-328", "Parallel & Distributed Computing", 3.0),
    ("EC-345", "Computer Vision / Elective", 3.0),
    ("EC-425", "Software Quality Engineering / Elective", 3.0),
    ("MS-254", "Technical and Business Writing", 3.0),
    ("GE-263", "Entrepreneurship", 2.0),
    ("GE-262", "Professional Practices", 2.0),
    ("HQ-007", "Quran Translation - VII", 0.5),],
8: [("CC-412", "Final Year Project - II", 4.0),
    ("DC-421", "Compiler Construction", 3.0),
    ("UE-272", "Introduction to Marketing", 3.0),
    ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
    ("GE-363", "Civics and Community Engagement", 2.0),
    ("HQ-008", "Quran Translation - VIII", 0.5),],
}

GRADE_TABLE = [(85, 4.0), (80, 3.7), (75, 3.3), (70, 3.0), (65, 2.7), (61, 2.3), (58, 2.0), (55, 1.7), (50, 1.0), (0, 0.0)]


def marks_to_grade_points(marks: int) -> float | str:
    """Convert raw marks to PUCIT grade points. Get Grade Point from student's marks in a course"""
    if not isinstance(marks, (int, float)) or marks < 0:
        return "Error: marks must be a non-negative number"
    for threshold, point in GRADE_TABLE:
        if marks >= threshold:
            return point
    return 0.0


def calculate_semester_gpa(grade_points: list[float], credit_hours: list[float]) -> float | str:
    """Calculate one semester's GPA. Calculate GPA if grade points and credit hours for all semester courses are given"""
    if not grade_points or not credit_hours:
        return "Error: grade_points and credit_hours must not be empty"
    if len(grade_points) != len(credit_hours):
        return "Error: grade_points and credit_hours must have the same length"
    total_weighted = 0.0
    total_credits = 0.0
    for gp, ch in zip(grade_points, credit_hours):
        if not isinstance(gp, (int, float)) or not isinstance(ch, (int, float)):
            return "Error: all grade_points and credit_hours must be numbers"
        if ch < 0:
            return "Error: credit_hours must be non-negative"
        total_weighted += gp * ch
        total_credits += ch
    if total_credits == 0:
        return "Error: total credit hours cannot be zero"
    return round(total_weighted / total_credits, 2)


def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float, semester_gpa: float, semester_credit_hours: float) -> float | str:
    """Project the CGPA after completing one more semester. Use this when you know the current CGPA, completed credit hours, and the GPA in latest semester, and needs the updated cumulative GPA."""
    if not isinstance(current_cgpa, (int, float)) and not isinstance(completed_credit_hours, (int, float)) and not isinstance(semester_gpa, (int, float)) and not isinstance(semester_credit_hours, (int, float)):
        return "Error: all parameters must be numbers"
    if completed_credit_hours < 0 or semester_credit_hours <= 0:
        return "Error: completed_credit_hours must be non-negative and semester_credit_hours must be positive"
    if current_cgpa < 0 or current_cgpa > 4.0:
        return "Error: current_cgpa must be between 0.0 and 4.0"
    if semester_gpa < 0 or semester_gpa > 4.0:
        return "Error: semester_gpa must be between 0.0 and 4.0"
    
    new_total_ch = completed_credit_hours + semester_credit_hours
    return round((current_cgpa * completed_credit_hours + semester_gpa * semester_credit_hours) / new_total_ch, 2)


def required_gpa_for_target(target_cgpa: float, current_cgpa: float, completed_credit_hours: float, remaining_credit_hours: float) -> float | str:
    """Calculate the semester GPA needed to reach a target CGPA. Use this when you know target CGPA, current CGPA, completed credit hours, and remaining credit hours, and needs to find what GPA the student needs. Argument names: target_cgpa, current_cgpa, completed_credit_hours, remaining_credit_hours."""
    if not isinstance(target_cgpa, (int, float)) and not isinstance(current_cgpa, (int, float)) and not isinstance(completed_credit_hours, (int, float)) and not isinstance(remaining_credit_hours, (int, float)):
        return "Error: all parameters must be numbers"
    if remaining_credit_hours <= 0:
        return "Error: remaining_credit_hours must be positive"
    if current_cgpa < 0 or current_cgpa > 4.0:
        return "Error: current_cgpa must be between 0.0 and 4.0"
    if target_cgpa < 0 or target_cgpa > 4.0:
        return "Error: target_cgpa must be between 0.0 and 4.0"
    total_ch = completed_credit_hours + remaining_credit_hours
    return round((target_cgpa * total_ch - current_cgpa * completed_credit_hours) / remaining_credit_hours, 2)


def get_semester_courses(semester: int) -> str:
    """Return the courses and credit hours for any semester. Use this when you need which courses are taken in a specific semester and their credit hours, for example to calculate remaining credit hours"""
    if not isinstance(semester, int) or semester not in COURSES:
        return "Error: semester must be between 1 and 8"
    courses = COURSES[semester]
    return ", ".join(f"{code} ({ch})" for code, _, ch in courses)


def get_remaining_credit_hours(current_semester: int) -> float | str:
    """Total the credit hours remaining after a given semester. Use this when you need to know how many credit hours are left after a semester is completed, for example to calculate the GPA required to reach a target CGPA"""
    if not isinstance(current_semester, int) or current_semester < 1 or current_semester > 8:
        return "Error: current_semester must be between 1 and 8"
    total = 0.0
    for sem in range(current_semester + 1, 9):
        for _, _, ch in COURSES[sem]:
            total += ch
    return total


def save_report(filename: str, content: str) -> str:
    """Save a summary report to a text file and return confirmation.
    """
    if not isinstance(filename, str) or not filename.strip():
        return "Error: filename must be a non-empty string"
    if not isinstance(content, str) or not content.strip():
        return "Error: content must be a non-empty string"
    if not filename.endswith(".txt"):
        filename = filename + ".txt"
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"Report saved successfully as {filename}"
    except Exception as e:
        return f"Error: could not save report — {e}"