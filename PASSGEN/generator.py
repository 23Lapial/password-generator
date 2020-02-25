#!/usr/bin/env python3

temp_pass = str(input()).lower()

password = []

# Upper every other character(starts at index 0)
for index, character in enumerate(temp_pass):
    if index % 2 == 1:
        password.append(temp_pass[index].lower())
    else:
        password.append(temp_pass[index].upper())

print(''.join(sorted(password, reverse=True)))
