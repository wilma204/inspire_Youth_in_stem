#exception handling
f = open("C:\Users\Admin\Documents\inspire_Youth_In_stem\Week-4\test.txttest.txt")

print(f . readline())
filename=("C:\Users\Admin\Documents\inspire_Youth_In_stem\Week-4\test.txt")
try:
    
    with open(filename, 'r+w' ,encoding =None) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    msg="sorry the file does not exist"
    print(msg)#

file_name ='C:\\Users\Admin\Documents\\inspire_Youth_In_stem\Week-4\\test.txt'
f = open(file_name,'r+w',encodind=None)
print(file_name.readlines())