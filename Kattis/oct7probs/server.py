total_tasks, total_time = [int(x) for x in input().strip().split()]
task_time = [int(x) for x in input().strip().split()]

count = 0
total_time_used = 0
while(count <= (total_tasks - 1) and (total_time_used + task_time[count]) <= total_time):
    total_time_used += task_time[count]
    count += 1

print(count)