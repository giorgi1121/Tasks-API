from tasks import TaskClient

client = TaskClient()

def main():
	while True:
		crud_function = input("Choose one operation from following - Create, Read, Update, Delete: ").lower().strip()
		if crud_function == "create":
			return create()
		elif crud_function == "read":
			return read()
		elif crud_function == "update":
			return update()
		elif crud_function == "delete":
			return delete()
		else:
			continue

def read():
	while True:
		read_what = input("Choose what to read: task by id or all tasks: ").lower().strip()
		if read_what in ["task", "task by id", "by id", "tasks", "all tasks"]:
			break
		else:
			continue

	if read_what in ["task", "task by id", "by id"]:
		while True:
			try:
				task_id = int(input("Enter task id: "))
			except ValueError:
				continue
			else:
				return print(client.get_task(task_id))
	elif read_what in ["tasks", "all tasks"]:
		return print(client.get_all_tasks())

def create():
	while True:
		try:
			id = int(input("What is id? "))
		except ValueError:
			continue
		else:
			while True:
				try:
					title = input("What is title? ")
				except ValueError:
					continue
				else:
					while True:
						try:
							completed = input("What is completed - True or False: ").title().strip()

							if completed not in ["True", "False"]:
								raise ValueError
						except ValueError:
							continue
						else:
							return print(client.create_task(id= id, title = title, completed = completed))

def update():
	while True:
		try:
			id = int(input("Enter id of the task you want to change: "))
		except ValueError:
			continue
		else:
			while True:
				try:
					new_id = int(input("Enter new id: "))
				except ValueError:
					continue
				else:
					while True:
						try:
							new_title = input("Enter new title: ").strip()
						except ValueError:
							continue
						else:
							while True:
								try:
									new_completed = input("Task is completed or not - Enter True or False: ").lower().strip()
									if new_completed not in ["true", "false"]:
										raise ValueError
								except ValueError:
									continue
								else:
									return print(client.update_task(task_id= id, id= new_id, title= new_title, completed= new_completed))	

def delete():
	while True:
		try:
			id = int(input("Enter id of the task you want to delete: "))
		except ValueError:
			continue
		else:
			return print(client.delete_task(id))


if __name__ == "__main__":
	main()
