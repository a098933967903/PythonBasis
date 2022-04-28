'''
file = open("text.txt",mode="w",encoding="utf-8")
file.write("Meow\n駭客")
file.close
'''

with open("text.txt",mode="w",encoding="utf-8") as file:
    file.write("MeowHecker")
