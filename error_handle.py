file = open('youtube.txt', 'w')

try:
    file.write('hello aur code')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('hello aur python')