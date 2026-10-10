total_tasks=5
original_tasks=total_tasks

print(f"You have {original_tasks} to work today")

tasks_completed=0
task_num=1

while task_num <= total_tasks:
    if task_num == 1 : next_task =  "Clean your room"
    elif task_num == 2 : next_task = "Do your homework"
    elif task_num == 3 : next_task = "Clean the backyard"
    elif task_num == 4 : next_task = "Feed the dog"
    else: next_task = "Wash the dishes"
    
    answer=input(f"Have you fininished doing {task_num} task? (yes/no): ")

    if answer.lower() == "yes":
        tasks_completed += 1
        task_num += 1
        print("Good job now do your next task")
    else:
        print("You need to finish your task before moving on to the next one")

print("All tasks completed")
print("Good job completing today's checklist")

print("Now lets safely peek at an infinite while loop")
test_value=0
safety_count=0

while safety_count <=0:
    print("This condition never changes")
    safety_count +=1

    if safety_count == 3:
        print("This is a safety break to prevent an infinite loop as it will go on forever")
        break

print("Today's task summary")

print(f"Chores assigned today: {original_tasks}")
print(f"Chores completed today: {tasks_completed}")
print(f"Chores remaining today: {original_tasks - tasks_completed}")