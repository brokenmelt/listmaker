tasks =[]
file = open("list_task.txt","r")
for line in file :
  tasks.append(line.strip())

file.close()
while True:
   print("1.add")
   print("2.view")
   print("3.delete")
   print("4.exit")

   choice=input("enter your choice :")
   if choice == "1":
        t=input("enter your task:")
        tasks.append(t)
        file = open("list_task.txt","w")
        for t in tasks:
            file.write(t+"")
        file.close()
   elif choice == "2":
        for i,task in enumerate(tasks):
         print(i,task)
   elif choice =="3":
        num =int(input("enter the num"))
        tasks.pop()
        file=open("list_task.txt","w")
        for x in tasks:
            file.write(x+"")
        file.close()  
   elif choice == "4":
        break 
   else:
        print("invalid")
