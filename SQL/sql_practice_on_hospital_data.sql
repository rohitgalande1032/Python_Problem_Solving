-- Q-1 : Show first name, last name, and gender of patients whose gender is 'M'
SELECT first_name, last_name, gender
FROM patients
WHERE gender = "M";

-- Q-2 : Show first name and last name of patients who does not have allergies(null)
SELECT first_name, last_name
FROM patients
WHERE allergies IS NULL;

-- Q-3 : Show first name of patients that start with letter "A"
SELECT first_name 
FROM patients
WHERE first_name LIKE "a%";  --Wildcard character (Pagination)

-- Q-4 : Show first name and last name of patients that weight within the range of 80 and 100
SELECT first_name, last_name 
FROM patients
WHERE weight BETWEEN 80 and 100;

-- Q-5 : Update the patient table for allegies column. if patients allergies is null then replace with "No Allergy"
UPDATE patients
SET allergies = "Not Allegies"
WHERE allergies IS NULL;

-- Q-6 : Show first name and last name concantinated into one column to show their full name
SELECT CONCAT(first_name, " ", last_name) AS full_name
FROM patients;

-- Q-7 : Show first name, last name and the full province name of each patient
-- Here are two tables patients(first_name, last_name, province_id...) and province_name(province_id, name...)

SELECT first_name, last_name, province_name
FROM patients JOIN province_name
ON patients.province_id = province_names.province_id;

-- Q-8 : Show how many patients have a birth date with 2010 as the birth year
SELECT COUNT(birth_date) 
FROM patients
WHERE bitrh_date LIKE "%2010%";

-- Q-9 : Show the first name, last name, height of the patient with the greatest height
SELECT first_name, last_name, MAX(height) as height
FROM patients
GROUP BY first_name, last_name
ORDER BY height DESC
LIMIT 1;

-- Q-10 : Show all columns for patients who have one of these patient_ids: 1, 45, 456, 345, 3000
SELECT * 
FROM patients
WHERE patient_ids IN (1, 45, 456, 345, 3000);  -- IN, NOT IN are memborship operators

-- Q-11 : Show total no.of operations
SELECT COUNT(admission_date)
FROM admissions;

-- Q-12 : Show all the colums from admission where the patient was admitted and discharged on the same day
SELECT * FROM admission
WHERE admission_date = discharge_date;

-- Q-13 : Show the patient id and the total no.of admissions for patient_id 567
SELECT patient_id, COUNT(admission_date)
FROM admissions
WHERE patient_id = 567

-- Q-14 : Based on the cities that our patients live in, show unique cities that are in province_id 'NS'
SELECT DISTINCT(city)
FROM patients
WHERE province_id = "NS";

-- Q 15 : Write a query to find first_name, last_name and birth_date of patients who has
--        height greater than 160 and weight greater than 70
SELECT first_name, last_name, birth_date
FROM patients
WHERE height > 160 and weight > 70;

-- Q 16 : Write a query to find list of patients first name, last name, and allergies where
--        allergies is not null and are from the city of 'Hamilton'
SELECT first_name, last_name, allergies
FROM patients
WHERE allergies is NOT NULL and city = "Hamilton";

-- Q-17 : Show unique birth years from patients and order them by ascending
SELECT DISTINCT(YEAR(birth_date)) as birth_year
FROM patients
ORDER BY birth_year;   -- By default order is ascending

-- Q-18 : Show only unique first names from the patients table
SELECT first_name 
FROM patients
GROUP BY first_name
HAVING COUNT(first_name) = 1;

-- Q-19 : Show patients_id and first_name from patients where their first_name start and ends
--        with 's' and is at least 6 characters long

SELECT patients_id, first_name
FROM patients
WHERE first_name LIKE "s%" and first_name LIKE "%s" and first_name LIKE "%______%";
-------------OR-----------------------
WHERE first_name LIKE "s%s" and first_name LIKE "%______%";
-------------OR-----------------------
WHERE first_name LIKE "s____%s";

-- Q-20 : Show patient_id, first_name from patients whose diagnosis is 'Dementia'.
--        Primary diagnosis is stored in the admission table
SELECT p.patient_id, p.first_name, p.last_name
FROM patients AS p 
    JOIN admission AS a
ON p.patient_id = a.patient_id
WHERE diagnosis = "Dementia";

-- Q-21 : Display every patient's first name. Order the list by length of each name and then by alphabetically
SELECT first_name
FROM patients
ORDER BY LEN(first_name) ASC;

-- Q-22 : Show the total amount of male patients and the total amount of female patients in the patient table
SELECT COUNT(gender = "M") AS Male, COUNT(gender="F") AS Female
FROM patients;

-- Q-23 : Show first_name and last_name, allergies from patients which have alleries to either 'Penicillin
--        or 'Morphine'. Show results ordered ascending by allegies then by first_name then last_name
SELECT first_name, last_name, allergies
FROM patients
WHERE allergies = "Penicillin" OR allergies = "Morphine"
ORDER BY allegies, first_name, last_name;

-- Q-24 : Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same dignosis
SELECT patient_id, dignosis
FROM admissions
GROUP BY patients_id, diagnosis
HAVING COUNT(patient_id=diagnosis) > 1;

-- Q-25 : Show the city and the total no.of patients in the city. Order from most to least patients 
--        and then by city name ascending
SELECT city, COUNT(*) AS tatal_no_of_patients
FROM patients
GROUP BY city
ORDER BY total_no_of_patients DESC, city;

-- Q-26 : . Show first name, last name and role of every person that is either patient or doctor. The
--          roles are either "Patient" or "Doctor"
SELECT first_name, last_name, "Patient" as role
FROM patients
UNION ALL --Combines the results of two queries into a single result set with duplicate values
SELECT first_name, last_name, "Doctor" as role
FROM doctors;


-- Q-27 : Show all allergies ordered by popularity. Remove NULL values from query.
select allergies, COUNT(*) as popular_allergies
from patients
where allergies is not NULL
group by allergies
order by popular_allergies DESC;

-- Q-28 : Show all patient's first_name, last_name, and birth_date who were born in the 1970s
--          decade. Sort the list starting from the earliest birth_date.
select first_name, last_name, birth_date
from patients 
where birth_date like "%197%"
order by birth_date ;

------------OR-----------------
select first_name, last_name, birth_date
from patients
where YEAR(birth_date) between 1970 and 1979
order by birth_date;

-- Q-29 : We want to display each patient's full name in a single column. Their last_name in all
--        upper letters must appear first, then first_name in all lower case letters. Separate the
--        last_name and first_name with a comma. Order the list by the first_name in decending
--        order. EX: SMITH,jane
select concat(upper(last_name), ",", lower(first_name)) as full_name
from patients
order by first_name desc;

-- Q-30 : Show the province_id(s), sum of height; where the total sum of its patient's height is
--        greater than or equal to 7,000.
select province_id, sum(height)
from patients
group by province_id
having sum(height) >= 7000;

-- Q-31 : Show the difference between the largest weight and smallest weight for patients with
--        the last name 'Maroni'
select (MAX(weight) - MIN(weight)) as weight_diff
from patients
where last_name = "Maroni";


-- Q-32 : Show all of the days of the month (1-31) and how many admission_dates occurred on
--        that day. Sort by the day with most admissions to least admissions.
select day(admission_date) day_num, count(patient_id) as total_admissions
from admissions
group by day_num
order by total_admissions desc;

-- Q-33 : Show all columns for patient_id 542's most recent admission_date.
select * from admissions
where patient_id = 542
order by admission_date desc
limit 1;

-- Q-34 :  Show patient_id, attending_doctor_id, and diagnosis for admissions that match one of
--         the two criteria: (A). patient_id is an odd number and attending_doctor_id is either 1, 5,
--         or (B). attending_doctor_id contains a 2 and the length of patient_id is 3 characters
select patient_id, attending_doctor_id, diagnosis
from admissions
where patient_id%2 <> 0 and attending_doctor_id in (1, 5)
or attending_doctor_id like  "%2%" and len(patient_id) = 3;

-- Q-35 : Show first_name, last_name, and the total number of admissions attended for each
--          doctor. Every admission has been attended by a doctor.
select first_name, last_name, count(admission_date) as total_admissions
from admissions a join doctors d
on a.attending_doctor_id = d.doctor_id
group by doctor_id;

-- Q-36 : For each doctor, display their id, full name, and the first and last admission date they attended.
select doctor_id, 
    concat(first_name," ",last_name) as full_name, 
    min(admission_date) as first_date_attended, 
    max(admission_date) as last_date_attended
from admission as a join doctor as d
on a.attending_doctor_id = d.doctor_id
group by doctor_id;


-- Q-37 : Display the total amount of patients for each province. Order by descending.
select pr.province_name, count(p.patient_id) as total_patients
from patients as p join province_names as pr
on p.province_id = pr.province_id
group by pr.province_name
order by p.total_patients desc;

-- Q-38 : For every admission, display the patient's full name, their admission diagnosis, and their
--        doctor's full name who diagnosed their problem.
select concat(p.first_name, " ", p.last_name) as patient_full_name, a.diagnosis,
       concat(d.first_name, " ", d.last_name)
from patients as p join admissions as 
on p.patient_id = a.patient_id
join doctors as d
on d.doctor_id = a.attending_doctor_id;

-- Q-39 : display the first name, last name and number of duplicate patients based on their first
--        name and last name.
select first_name, last_name, count(*) as no_of_duplicates
from patients
group by first_name, last_name
having count(*) > 1;

-- Q-40 : Display patient's full name, height in the units feet rounded to 1 decimal, weight in the
--        unit pounds rounded to 0 decimals, birth_date, gender non abbreviated. Convert CM to
--        feet by dividing by 30.48. Convert KG to pounds by multiplying by 2.205.
select concat(first_name, " ", last_name) as patient_full_name,
       round((height/30.48), 1) as height, 
       round((weight*2.205), 0) as weight, 
       birth_date,
       case
            when gender = "M" then "Male",
            when gender = "F" then "Female"
       end as gender
from patients;

-- Q-41 : Show patient_id, first_name, last_name from patients who do not have any records in
--        the admissions table. (Their patient_id does not exist in any admissions.patient_id rows.)

select p.patient_id, p.first_name, p.last_name 
from patients as p left join admission as a
on p.patient_id = a.patient_id
where p.patient_id is null;