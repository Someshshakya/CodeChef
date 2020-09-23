'''
NAVHW_054: Write a program to store the names of 25 people in your classroom, in reverse order.
	
	Input:
    Ram
	Shyam
	Sam
	Ravi
	Pallavi

	Output:
	Pallavi
	Ravi
	Sam
	Shyam
	Ram
'''
num_of_people = int(input("number of people to store them in reverse order:   "))
people_list = []
for i in range(num_of_people):
    people_list.append(input("Enter name of the person:-   "))

# To print the people in the reverse order
for j in range(len(people_list)-1,-1,-1):
    print(people_list[j])