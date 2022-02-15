# # invited list = Nneh, C and Noble
# invited = ["Nneh", "C", "Noble"]

# print(invited[0].upper() +", you are invited to my dinner")
# print(invited[1].lower() +", you are invited to my dinner")
# print(invited[2].title() +", you are invited to my dinner\n")

# # Second Section of the code: Changing Guest List 
# print('Im so sorry to inform everyone that my sweet mum ' +invited[0]+ 
#       ' can"t make it to the dinner again\n')

# invited[0] = "my_mummy"
# print(invited[-3]+ " " +", you are hereby invited to my dinner")
# print(invited[-2]+ " " +", you are still invited to my dinner")
# print(invited[-1]+ " " +", you are still invited to my dinner\n")

# # 3.5 more guest
# # more invited persons = Mike, Soso and Genesis
# print("I'm so happy to inform us all that i found a bigger dinner table for six\n")

# invited.insert(0, "Mike")
# invited.insert(3, "Soso")
# invited.insert(5, "Genesis")

# # 3.6 shrinking guest list
# print("I'm so sorry the proposed dinner table can't arrive eaarly so i'm left with space for two\n")

# unvited = invited.pop()
# print(unvited + " i'm so sorry to inform you that the dinner table won't get here early again so you are no longer invited")
# unvited = invited.pop()
# print(unvited + " i'm so sorry to inform you that the dinner table won't get here early again so you are no longer invited")
# unvited = invited.pop()
# print(unvited + " i'm so sorry to inform you that the dinner table won't get here early again so you are no longer invited")
# unvited = invited.pop()
# print(unvited + " i'm so sorry to inform you that the dinner table won't get here early again so you are no longer invited\n")

# print(invited[0]+ " you are still invited")
# print(invited[1].title()+ " you are still invited")

# del invited[0]
# del invited[0]
# print(invited)
# num = 10000000000
# dividers=[3,4,5,6,7,8,9,10]

# for i in range(num):
#     for j in dividers:
        
#         if i/j == (num-1) :
#             print(i, j)
out = str(help("modules pyQt5"))
path = 'C:\\Users\\Admin\\Documents\\My Resume\\text.txt'
with open(path,"w") as file:
    file.write(out)