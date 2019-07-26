print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    	print("Your Grade is Excellent");
    elif(average>=81 and average<=90):
    	print("Your Grade is Very good");
    elif(average>=71 and average<=80):
    	print("Your Grade is Good");
    elif(average>=61 and average<=70):
    	print("Your Grade is Bad");
    elif(average>=51 and average<=60):
    	print("Your Grade is sad");
    elif(average>=41 and average<=50):
    	print("Your Grade is weak");
    elif(average>=0 and average<=40):
    	print("Your Grade is fair");
    else:
    	print("Strange Grade..!!");
