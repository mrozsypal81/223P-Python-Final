# CWID 889478913
# Name Michael Rozsypal
# Problem 2




import pandas as pd

df = pd.DataFrame()

#enter customer data into dataframe
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

#for tracking every product being entered into dataframe
prodlist = []


#enter product data into dataframe
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
                        prodlist.append(word2)
                    elif temp == ' QUANTITY ':
                        print("Going into QUANTITY")
                        rowIndex = df[df['CUSTOMER ID ']==CID].index[0]
                        intword = int(word2)
                        df.loc[rowIndex,lastprod] = intword
        linenumber = linenumber + 1

#Will fill any Nan Values that occur with 0
for i in prodlist:
    df[i].fillna(0)
    df[i] = pd.to_numeric(df[i])
print("++++++++++++++++++Printing Dataframe++++++++++++++++++")
print(df)
print("++++++++++++++++++Printing Dataframe++++++++++++++++++")

#If the correlation is possitve and closer to 1 then it is a positive correlation
#IF the correlation is negative closer to -1 then it is a negative correlation
#if the correlation is close to 0 then it has no correlation
#The data means nothing because the values are all random and made up
def prodcor(p1,p2):
    print("Inside prodcor")
    corr = df[p1].corr(df[p2])
    print("The correlation between the two products is ",corr)

#If the correlation is possitve and closer to 1 then it is a positive correlation
#IF the correlation is negative closer to -1 then it is a negative correlation
#if the correlation is close to 0 then it has no correlation
#The data means nothing because the values are all random and made up
def prodcorgen(p1,p2):
    print("Inside prodcorgen")
    grouped = df.groupby([" GENDER "])[[p1,p2]].corr()
    #df.groupby('ID')[['Val1','Val2']].corr().iloc[0::2]['Val2']
    print("The correlation between the two products based on gender is ")
    print(grouped)

prodcor(' prod3 ',' prod4 ')
prodcorgen(' prod1 ',' prod2 ')
