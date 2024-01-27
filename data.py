from datetime import date
date = date.today()


def write_note(line):
	with open('data.txt', 'a') as f:
		if line == "!quit":
			f.write("\n-------------------------\n")
			ad = check_id()
			f.write(ad + '\n')
			f.write("________________________\n")
		else:
			f.write(line + "\n")


def see_all():
	with open('data.txt', 'r') as f:
		get_lines = f.readlines()
		for i in get_lines:
			print(i)
		return get_lines


def logs(act):
	with open('logs.txt', 'a') as f:
		f.write('\n')
		if act == 1:
			f.write(f"You created new note! {date}")
		elif act == 2:
			f.write(f"You checked your notes! {date}")
		f.write('\n')


def check_id():
	with open('data.txt', 'r') as f:
		ad = 0
		for i in f:
			if i.rstrip() == "-------------------------":
				ad += 1

		return str(ad)
