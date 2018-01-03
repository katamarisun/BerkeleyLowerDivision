.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  select seven, denero from students;

CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 8 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select fall.date, fall.number, fall.pet, fall.color, spring.color from students as fall, sp16students as spring where 
  		 fall.date = spring.date and fall.pet = spring.pet and fall.number = spring.number;

CREATE TABLE sevens AS
  select students.seven from students, checkboxes where students.time = checkboxes.time and checkboxes.'7' = 'True' and students.number = 7;

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color from students as a, students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;
