# 1. student_marks.csv contains the marks and other details for some students.
# Write a python program to:
# 1. Open the file in read mode
# 2. Create a dictionary from the given data
# 3. Add a new field to the dictionary total\_marks and store the total marks of
# the students.
# 4. Add a new field to the dictionary Average and store the average marks of the
# students.
# 5. Create a new file and write this information to the new file
# (https://www.kaggle.com/arunkumar413/studentmarks)
# 2. Create a new CSV file with the newly created total marks and average marks.

import csv      
# importing the csv library
# function for total and average marks
def calc_totalAndAverage(marks):
    # total marks calculations
    total_marks = sum(marks)

    # average marks calculations
    average_marks = total_marks / len(marks)

    return (total_marks, average_marks)

# function for file read mode in csv
def read_csv(file_path):
    #Initialize an empty list to store student data
    student_data = []

    # opening the file in read mode
    with open(file_path, mode='r') as file:
        # Create a CSV reader object to read the file
        csv_reader = csv.DictReader(file)
        
        # Print the fieldnames (column names) to debug
        print("Column names: ",csv_reader.fieldnames)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # converting the row in dictionary
            student = dict(row)
            # extract and convert the marks from strings to integer
            # handling errors
            try:
                marks = [int(student['Maths']), int(student['Science']), int(student['English'])]
            
            except KeyError as e:
                print(f"Column {e} not found in csv file. Please check the column name")
                # stop
                break

            # total and average marks calculations
            total_marks, average_marks = calc_totalAndAverage(marks)

            # adding the total and average marks to the student dictionary
            student['Total_marks'] = total_marks
            student['Average_marks'] = average_marks

            # adding the updated student dictionary to list
            student_data.append(student)
    
    return student_data

# function for file write mode in csv
def write_csv(file_path, data, columns):
    # opening the file in write mode
    with open(file_path, mode='w', newline='') as file:
        # creating a csv writer object to write file
        csv_writer =csv.DictWriter(file, fieldnames=columns)

        # write the column header names to the csv file
        csv_writer.writeheader()

        # looping in the student dictionary in the data list
        for student in data:
            # Write the student dictionary as a row in the CSV file
            csv_writer.writerow(student)


def main():
    # Define the path to the input CSV file
    input_file_path = r"c:\Users\Godismyfriend\Downloads\student_marks.csv"

    # Read the student data from the input CSV file
    student_data = read_csv(input_file_path)

    # Define the columns for the output CSV file
    columns = ['Student_name', 'Maths', 'Science', 'English', 'total marks', 'Average']

    # Define the path to the output CSV file
    output_file_path = "student_marks_update.csv"

    # Write the updated student data to the output CSV file
    write_csv(output_file_path, student_data, columns)  

# main
if __name__ == "__main__":
    main()    

