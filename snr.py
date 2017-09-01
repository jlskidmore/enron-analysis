import os
from email.parser import Parser
#root = 'test1/'
root = 'maildir/allen-p'



def email_analyze(searchfile, emailList):
    with open(searchfile, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)

    #append to emailList with formatting for csv
    emailList.append(email['to'])
    emailList.append(",")
    emailList.append(email['from'])
    emailList.append("\n")

emailList = []

#traverse directory and run email_analyze function
for directory, subdirectory, filenames in  os.walk(root):
    for filename in filenames:
        email_analyze(os.path.join(directory, filename), emailList)

#all info into one csv file
with open("data.csv", "w") as f:
    f.write("source,target")
    f.write("\n")
    for email in emailList:
        f.write(str(email))
