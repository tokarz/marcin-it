-- 1. Select all students who are not enrolled in any course.
SELECT * FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id;
-- 2. Select all courses that have no students enrolled.
SELECT * FROM courses
LEFT JOIN enrollments ON courses.course_id = enrollments.student_id;
-- 3. How many students are enrolled in each course?
SELECT courses.course_name , COUNT(*) AS student_count FROM enrollments
JOIN courses ON enrollments.course_id = courses.course_id
GROUP BY courses.course_name;
-- 4. List all students with their total number of enrolled courses.
SELECT students.name , COUNT(enrollments.course_id) AS total_courses
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.course_id
GROUP BY students.name;
-- 5. List all enrollments with student name, course name, and enrollment date.
SELECT students.name , courses.course_name , enrollments.enrollment_date
FROM enrollments
JOIN students ON enrollments.student_id = students.student_id
JOIN courses ON enrollments.course_id = courses.course_id;
-- 6. Show students who are enrolled in more than one course.
SELECT students.name , COUNT(Enrollments.course_id) AS total_courses
FROM students
JOIN enrollments ON students.student_id = enrollments.student_id
GROUP BY students.name;
-- 7. Count total enrollments per student.
SELECT students.name , COUNT(enrollments.enrollment_id) AS total_enrollments
FROM students
LEFT JOIN enrollments on students.student_id = enrollments.enrollment_id
GROUP BY students.name;
