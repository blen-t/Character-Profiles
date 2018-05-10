import time
import smtplib

localtime = time.asctime(time.localtime(time.time()))
records = open("profiles.txt", "a")


def repeat():
    count_status = 0
    while count_status < 25:
        again = int(input("\nEnter 1 if you would like proceed. Enter a different number if you would like to stop: "))
        if again != 1:
            quit()

        def name():
            print("\n--- PLEASE PRINT YOUR FAVORITE FICTIONAL CHARACTER'S NAME ---")
            last_name = input('Last Name: ').upper()
            first_name = input('First name: ').upper()
            middle_name = input('Middle name: ').upper()
            full_name = first_name + ' ' + middle_name + ' ' + last_name
            return full_name

        def age():
            print("\n--- PLEASE PRINT THE CURRENT AGE OF THE CHARACTER ---")
            age = int(input('What is their current age?: '))
            return str(age)

        def DOB():
            print("Enter the Date of Birth in the following for EACH of the entries below MM/DD/YYYY:")
            month = int(input("Please enter the MONTH(MM) they were born: "))
            day = int(input("Please enter the DAY(DD) they were born: "))
            year = int(input("Please enter the YEAR(YYYY) they were born: "))
            date_of_birth = str(month) + '/' + str(day) + '/' + str(year)
            return date_of_birth

        def gender():
            print("\n--- PLEASE PRINT THE GENDER OF THE CHARACTER ---")
            gender = input('What is their gender preference?: ').title()
            birthsex = input('What was their sex at birth? Note: This is confidential: ')
            return gender

        def height():
            print("\n--- PLEASE ENTER HEIGHT IN FEET AND INCHES ---")
            feet = int(input("What is their height in feet? ft: "))
            inches = int(input("What is their height in inches? Inches 0-11: "))
            height = str(feet) + "'" + str(inches) + '"'
            return height

        def weight():
            print("\n--- PLEASE PRINT THE WEIGHT OF THE CHARACTER ---")
            weight = float(input("What is their weight in pounds?: "))
            return str(weight)

        def health():
            print("\n--- PLEASE ANSWER THE FOLLOWING QUESTIONS ABOUT THE CHARACTER'S HEALTH ---")
            health = input("Was their last routine Doctor's Physical Exam within the past year? y/n: ").lower()
            if health == "n":
                health = int(input("How many years has it been? "))
                if health > 2:
                    health = "In need of a Doctor's Physical Exam"
                else:
                    health = "May need to get a Physical Exam"
            else:
                health = "Has been examined within the past year"
            return health

        def family():
            print("\n--- PLEASE ANSWER THE FOLLOWING QUESTIONS ABOUT THE CHARACTER'S FAMILY ---")
            relationship = input("Are they married? y/n: ").lower()
            if relationship == "n":
                relationship = input('Are they in a relationship? y/n: ').lower()
                if relationship == "n":
                    relationship = input("Are they a widower? y/n: ").lower()
                    if relationship == "y":
                        relationship = "A Widower"
                    else:
                        relationship = "Single"
                else:
                    relationship = input("Is their relationship a domestic relationship? y/n: ").lower()
                    if relationship == "n":
                        relationship = "In a relationship"
                    else:
                        relationship = "In a domestic relationship"
            else:
                children = int(input("How many kids do they have? "))
                if children == 0:
                    relationship = "Married with no kids"
                else:
                    relationship = "Married with " + str(children) + " kid(s)"
            return relationship

        def student():
            print("\n--- PLEASE PRINT Y/N ABOUT CHARACTER'S STUDENT STATUS ---")
            student = input("Are they currently a student? y/n: ").lower()
            if student == "n":
                student = "Not a student"
            else:
                student = "Is a student"
            return student

        def school():
            print("\n--- PLEASE ANSWER CHARACTER'S SCHOOL STATUS ---")
            attending = input("Do they currently attend school? y/n: ").lower()
            if attending == "y":
                school = input("What school do they attend? ").upper()
                living_status = input("Do they live on campus? y/n: ").lower()
                if living_status == "n":
                    living_status = "Lives off campus"
                else:
                    living_status = "Lives on campus"
            else:
                school = "Does not attend school"
            return school

        def driver():
            print("\n--- PLEASE PRINT CHARACTER'S DRIVING STATUS ---")
            driving_status = input("Do they currently drive? y/n: ").lower()
            if driving_status == "y":
                driving = input("What state did they get their license from? Enter the states abbreviation code (Maryland = MD): ").upper()
                driving_years = int(input("How many years have they been driving? "))
                driving_status = "Has a " + driving + " state license and has been driving for " + str(driving_years) + " years"
            else:
                driving_status = "Does not drive"
            return driving_status


        name = name()
        age = age()
        dob = DOB()
        gender = gender()
        height = height()
        weight = weight()
        health = health()
        family = family()
        student = student()
        school = school()
        driver = driver()

        records.write("\n" + localtime + "\n" + "Name: " + name)
        records.write("\tAge: " + age)
        records.write("\nD.O.B: " + dob)
        records.write("\tSex: " + gender)
        records.write("\nHeight: " + height)
        records.write("\tWeight: " + weight)
        records.write("\nHealth: " + health)
        records.write("\nRelationship/Family: " + family)
        records.write("\nStudent: " + student)
        records.write("\nSchool: " + school)
        records.write("\nDriver: " + driver + "\n")

        print('---------------------------------------------------------', '\nName:', name, '\tAge:', age, '\nD.0.B.:', dob, '\tSex:', gender, '\nHeight:', height, '\tWeight:', weight, '\nHealth:', health, '\nRelationship/Family:', family, '\nStudent:', student, '\nSchool:', school, '\nDriver:', driver)

        print("\nTHANK YOU FOR YOUR PATIENCE, YOU'RE ALL DONE! :)")

        TO = 'good.great.happy.news@gmail.com'
        SUBJECT = 'wow'
        TEXT = 'NEW PROFILE RECORD:\n' + '\nName: '+ name + '\tAge: ' + age + '\nD.0.B.: ' + dob + '\tSex: '+ gender + '\nHeight: '+ height + '\tWeight: ' + weight + '\nHealth: '+ health + '\nFamily: '+ family + '\nStudent: ' + student + '\nSchool: '+ school + '\nDriver: ' + driver
        # Gmail Sign In
        gmail_sender = 'supreme.plus1@gmail.com'
        gmail_passwd = 'infosci326'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        BODY = '\r\n'.join(['To: %s' % TO, 'From: %s' % gmail_sender, 'Subject: %s' % SUBJECT, '', TEXT])

        try:
            server.sendmail(gmail_sender, [TO], BODY)
            print('email sent')
        except:
            print('error sending mail')

            server.quit()

        count_status = count_status + 1
        print(count_status)


repeat()
