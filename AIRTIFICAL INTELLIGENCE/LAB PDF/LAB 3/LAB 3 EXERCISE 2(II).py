def append_to_file(file_name, message):
    with open(file_name, 'a') as file:
        file.write(message)

file_name = 'student.txt'
message = "Now we are AI students"

append_to_file(file_name, message)
