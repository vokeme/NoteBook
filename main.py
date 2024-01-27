from data import write_note, see_all, logs
import time


print("Welcome to YNoteBook!")
time.sleep(1.5)
print("There you can see available actions:")
time.sleep(1.5)
print("")
print("1. Write new note")
print("2. See all notes and their id")
print("")
time.sleep(1.5)

while True:
	print("Now write number of action that you want to happen (write 0 to exit)")
	choice = int(input())

	if choice == 1:
		print("Now write anything that you want and when you are finished just write !quit")
		while True:
			line = input()
			if line == "!quit":
				logs(choice)
				write_note(line)
				break
			else:
				write_note(line)

	elif choice == 2:
		logs(choice)
		see_all()

	elif choice == 0:
		break
