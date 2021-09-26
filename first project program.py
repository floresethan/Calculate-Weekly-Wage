# I JUST MADE MY OWN PROGRAM TO HELP USERS CALCULATE HOW MUCH MONEY THEY WOULD MAKE BASED ON THE HOURS THEY WORKED
# INCLUDING OVERTIME AT A (Y * HOURLY PAY) * (X HOUR WORKED OVERTIME)
# LETS GO.
name = input("Please enter your name: ")
job = input("Please enter the name of the company you work for: ")
hours_worked = input("Please enter the amount of hours you are required to work for " + job + ": ")
rate_per_hour = input("Please enter your hourly pay: ")
overtime_worked = input("Please enter the amount of overtime, in hours, you worked this week: ")
overtime_modifier = input("Please enter the multiplier of money " + job + " gives you for working X amount of hours overtime: ")
hours_worked_no_overtime = float(hours_worked) * float(rate_per_hour)
hours_worked_with_overtime = float(hours_worked_no_overtime) + ((float(rate_per_hour) * float(overtime_worked)) * float(overtime_modifier))
yearly_salary = float(hours_worked_no_overtime) * 52
yearly_salary_overtime = float(hours_worked_with_overtime) * 52
if float(hours_worked) + float(overtime_worked) <= float(hours_worked):
    print("You worked no overtime this week for a paycheck of, " + str(hours_worked_no_overtime) + ".")
    print("That is " + str(yearly_salary) + " dollars a year if you worked no overtime.")
    print("Try harder next week, " + name + ". You can do it!")
elif float(hours_worked) + float(overtime_worked) > float(hours_worked):
    print("Congratulations, " + name + ", you worked " + str(float(overtime_worked) + float(hours_worked)) + " hours this week at " + job + " for a paycheck of: " + str(hours_worked_with_overtime) + ".")
    print("That is " + str(hours_worked_with_overtime - hours_worked_no_overtime) + " extra dollars for working " + overtime_worked + " extra hours this week.")
    print("In other words, that is " + str(yearly_salary_overtime) + " dollars a year if you worked ." + overtime_worked + " days every week.")
    print("You would have made " + str(hours_worked_no_overtime) + " dollars this week if you did not work overtime.")
    print("Great job, " + name + "!")
print("Program finished. Thank you, " + name + ".")















