#1️⃣ Student Result Manager
#Features:
#Add student
#Calculate percentage
#Save results to file
					
print('Welcome , to the Student result manager')
ask = int(input('How many students : '))
ask2 = int(input('how many subjects : '))
m = int(input('total marks per subject : '))
lst = []

for i in range(ask):
	t = 0
	name = input('Enter name of the student : ')
	for j in range(ask2):
		marks = int(input(f"Enter marks in sub{j+1}"))
		t += marks
	per = (t/(ask2*m))*100
	lst2 = [name , t , per]
	lst.append(lst2)

file = open("results.txt", "w")

for i in lst:
	file.write(str(i) + "\n")
file.close()

print("Results saved to file.")
