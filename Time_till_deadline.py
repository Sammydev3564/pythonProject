from datetime import datetime
user_input= input("Enter your goal with a deadline, seperate it with a colon \n")
input_list=user_input.split(":")

goal= input_list[0]
deadline= input_list[1]

deadline_date= datetime.strptime(deadline, "%m.%d.%Y")
today_date=datetime.today()
time_till= deadline_date - today_date

hours_till=int(time_till.total_seconds() /60 /60)
print(f"dear user! time remaining to deadline : {goal} is {hours_till} hours")