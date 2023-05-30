# It's the end of the semester and you got your marks from, Geometry, Algebra, Physics classes. If the average score is 7 and above print "Good job!", if the average score is between 6 and 4 print "You need to work harder!", if the average score is below 4 print "Failed, you really need to work harder!". 10, 12, 20

geometry_mark = 10
algebra_mark = 12
physics_mark = 20

average_score = (geometry_mark + algebra_mark + physics_mark) / 3

if average_score >= 7:
    print("Good job!")
elif average_score >= 4:
    print("You need to work harder!")
else:
    print("Failed, you really need to work harder!")
