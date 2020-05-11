# CWID 889478913
# Name Michael Rozsypal
# Problem 2




import pandas as pd

df = pd.DataFrame()

with open('customer.txt','r') as f:
    #This is to get rid of the newline character
    mylist = f.read().splitlines() 
    linenumber = 0
    for line in mylist:
        for word in line.split(';'):
            print(word)
            temp = None
            x = 0
            for word2 in word.split(':'):
                print(word2)
                #this skips the first label
                if x == 0:
                    temp = word2
                    x = x + 1
                elif x == 1:
                    df.loc[linenumber,temp] = word2
        linenumber = linenumber + 1

with open('product.txt','r') as f:
    #This is to get rid of the newline character
    mylist = f.read().splitlines() 
    linenumber = 0
    CID = None
    lastprod = None
    for line in mylist:
        for word in line.split(';'):
            print(word)
            temp = None
            x = 0
            for word2 in word.split(':'):
                print(word2)
                #this skips the first label
                if x == 0:
                    temp = word2
                    temp = str(temp)
                    x = x + 1
                elif x == 1:
                    print("Going into switch temp is "+temp+"123")
                    print(type(temp))
                    if temp == 'CUSTOMER ID ':
                        print("Going into CUSTOMER ID")
                        CID = word2
                    elif temp == ' PRODUCT NAME ':
                        print("Going into PRODUCT NAME")
                        rowIndex = df[df['CUSTOMER ID ']==CID].index[0]
                        df.loc[rowIndex,word2] = '0'
                        lastprod = word2
                    elif temp == ' QUANTITY ':
                        print("Going into QUANTITY")
                        rowIndex = df[df['CUSTOMER ID ']==CID].index[0]
                        df.loc[rowIndex,lastprod] = word2
        linenumber = linenumber + 1

print(df)


