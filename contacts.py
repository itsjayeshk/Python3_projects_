contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Harry Potter', 'email': 'harry@example.com'},
        {'name': 'Hermione Granger', 'email': 'hermaione@example.com'},
        {'name': 'Ron Weasley', 'email': 'ron@example.com'},
        {'name': 'Draco Malfoy', 'email': 'draco@example.com'}
 ]
}
print('student emails:')
for students in contacts['students']:
    print(students['email'])