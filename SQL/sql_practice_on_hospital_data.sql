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





