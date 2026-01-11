import gradio as gr

# ----------------------------------
# Convert marks to grade points
# ----------------------------------
def mark_to_grade_point(mark):
    if mark >= 90:
        return 10
    elif mark >= 80:
        return 9
    elif mark >= 70:
        return 8
    elif mark >= 60:
        return 7
    elif mark >= 50:
        return 6
    elif mark >= 40:
        return 5
    else:
        return 0

# ----------------------------------
# Core calculation logic
# ----------------------------------
def calculate_cgpa_percentage(marks):
    if not marks:
        return 0.0, 0.0

    # Convert marks to grade points
    grade_points = [mark_to_grade_point(m) for m in marks]

    # CGPA calculation
    cgpa = sum(grade_points) / len(grade_points)

    # Percentage calculation
    percentage = cgpa * 9.5

    return round(cgpa, 2), round(percentage, 2)

# ----------------------------------
# Wrapper for Gradio input
# ----------------------------------
def process_marks(marks_text):
    try:
        # Parse comma-separated marks
        marks = [float(m.strip()) for m in marks_text.split(",") if m.strip()]

        # Validation
        for m in marks:
            if m < 0 or m > 100:
                return "Invalid marks entered", ""

        cgpa, percentage = calculate_cgpa_percentage(marks)
        return f"{cgpa}", f"{percentage}%"

    except Exception:
        return "Error", "Please enter valid numbers separated by commas"

# ----------------------------------
# Gradio UI
# ----------------------------------
interface = gr.Interface(
    fn=process_marks,
    inputs=gr.Textbox(
        label="Enter marks for each subject (comma separated)",
        placeholder="Example: 78, 85, 90, 72, 88"
    ),
    outputs=[
        gr.Textbox(label="CGPA"),
        gr.Textbox(label="Percentage")
    ],
    title="Engineering CGPA & Percentage Calculator",
    description="Calculate CGPA and percentage based on number of subjects and obtained marks"
)

# ----------------------------------
# Entry point (required)
# ----------------------------------
interface.launch()
