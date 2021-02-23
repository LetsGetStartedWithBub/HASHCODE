'''
There are 3 teams with 2,3 and 4
'''
def main():
    # File is being read
    file_object= open("./a_example","r+")
    li_new=[]   # For storing final output list of elements
    c=0         #To make sure that element in 1 list should be taken without \n
    for i in file_object:
        if c==0:
            # Form a list of elements
            li = list(i.split(" ")) 
            # For removing the \n character from the list at 0 position ['5','2','1','1','\n']
            # Else one more character will be added as \n
            li = li[0:4]
            print(li)
            # First list without \n is removed
            li_new.append(li)
            c=c+1
        else:
            # As first line is already read and (c+1) condition is checked therefore in all 
            # the other lines where \n is present
            # will be removed by using strip() 
            li = list(i.split(" ")) 
            final_list = []
            for i in li:
                final_list.append(i.strip())
            print("final_list",final_list)
            #After having both the lists now we can add them to generate a final list
            li_new.append(final_list)
            c=c+1
    return li_new

if __name__=='__main__':
    a=main()
    # nested list of elements is received
    print(a)
    l1 = a[0]
    '''
    available_pizza = total pizza at pizzaria
    t2 = the number of 2-person teams
    t3 = the number of 3-person teams
    t4 = the number of 4-person teams
    '''
