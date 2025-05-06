
-- Create the database (run this separately if your environment doesn't support CREATE DATABASE within a transaction)
-- Connect to your default database (e.g., postgres) and run:

-- TO odpal osobno i PAMIETAJ BY POZNIEJ OTWORZYC SQL EDITOR DLA TEJ BAZY! INACZEJ TABELE STWORZA SIE W ZLYM MIEJSCU!
CREATE DATABASE schooldb;

-- Drop tables if they already exist
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;

-- Create Students table
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create Courses table
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0)
);

-- Create Enrollments table
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE,
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE,
    enrollment_date DATE
);

-- Insert sample students
INSERT INTO Students (name, email) VALUES 
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Davis', 'charlie@example.com');

-- Insert sample courses
INSERT INTO Courses (course_name, credits) VALUES
('Mathematics', 5),
('History', 4),
('Physics', 3);

-- Insert sample enrollments
INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2023-09-01'),
(1, 2, '2023-09-01'),
(2, 3, '2023-09-02');

-- ======================
-- Join Examples
-- ======================

-- INNER JOIN: Get students and the courses they are enrolled in
SELECT s.name AS student_name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

-- LEFT JOIN: List all students and their enrollments (even if none)
SELECT s.name AS student_name, c.course_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c ON e.course_id = c.course_id;

-- RIGHT JOIN: List all courses and enrolled students (even if no one enrolled)
SELECT s.name AS student_name, c.course_name
FROM Students s
RIGHT JOIN Enrollments e ON s.student_id = e.student_id
RIGHT JOIN Courses c ON e.course_id = c.course_id;

-- ======================
-- Practice Questions
-- ======================

-- 1. Select all students who are not enrolled in any course.
-- 2. Select all courses that have no students enrolled.
-- 3. How many students are enrolled in each course?
-- 4. List all students with their total number of enrolled courses.
-- 5. List all enrollments with student name, course name, and enrollment date.
-- 6. Show students who are enrolled in more than one course.
-- 7. Count total enrollments per student.

-- Bonus: Create a view of all student-course pairs.
-- CREATE VIEW StudentCourseView AS
-- SELECT s.name AS student_name, c.course_name
-- FROM Students s
-- JOIN Enrollments e ON s.student_id = e.student_id
-- JOIN Courses c ON e.course_id = c.course_id;
