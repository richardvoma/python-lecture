# You are developing a program for a teacher to grade their students' exams. The program should prompt the teacher to enter the number of questions on the exam, the number of questions the student answered correctly, and the number of points each question is worth. The program should then calculate the student's grade as a percentage, and print out a message indicating whether the student passed or failed the exam.


# ask the teacher to enter exam details
num_questions = int(input("Enter the number of questions on the exam: "))
num_correct = int(
    input("Enter the number of questions the student answered correctly: "))
points_per_question = float(
    input("Enter the number of points each question is worth: "))
# calculating the student number of points(by multiplying the number of question answers by the point)
max_num_points = num_correct*points_per_question

# calculate the student score
total_score = (points_per_question/num_questions)*100
# Calculate the student's grade as a percentage
grade = (num_correct / num_questions) * 100

# Print out the student's grade and pass/fail status
if grade >= 60:
    print("print the student pass the exam")
else:
    print("print the student fail the exam")
