
# Q1.You will have a number of elements and in the next n lines element of a list.
# You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.
#For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']

org_list = ['great','hello','hiyo','abc']
org_list.sort(key=lambda x: x[-2])
print(org_list)


#Q2 A student will not be allowed to sit in the exam if his/her attendance is less than 75%. 
# if he/she has medical causes reduce attendance criteria to 60%. Ask the user if he/she has a medical cause or not 
# ( 'Y' or 'N' ) and print accordingly. You were given a total no classes and total classes attended by the student

total_classes = int(input("Enter the total number of classes: "))
attended_classes = int(input("Enter the total number of classes attended: "))
medical_cause = input("Do you have a medical cause? (Y/N): ")

attendance_percentage = (attended_classes / total_classes) * 100

if medical_cause == "Y":
    if attendance_percentage >= 60:
        print("You are eligible to sit in the exam.")
    else:
        print("Sorry, you are not eligible to sit in the exam as your attendance is below 60%.")
else:
    if attendance_percentage >= 75:
        print("You are eligible to sit in the exam.")
    else:
        print("Sorry, you are not eligible to sit in the exam as your attendance is below 75%.") 

