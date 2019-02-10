
#a
course_code=input('Enter course code: ')


#b
course_code=course_code.strip()

#c

if not len(course_code) == 6:
    print('Course code must have 6 characters.')
else:
    subject=course_code[0:3]
    course_number=course_code[3:6]

    if not subject.isalpha():
        print('You have entered an invalid code.')


    elif not course_number.isdigit():
        print('You have entered an invalid code.')

    else:
        print('Subject: ',subject)
        print('Course_number: ',course_number)




