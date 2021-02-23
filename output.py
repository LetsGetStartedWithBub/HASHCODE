from more_pizza import main as process

def output(l):
    file1 = open("output.txt","w")
    for i in l:
        file1.writelines(i)
    file1.close()

b = process()
c= output(b)