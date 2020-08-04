import csv
from datetime import datetime
#Nexted dictionary of analysed report
result = {};
#reading of file-complaints.csv
with open('input/complaints.csv', mode='r') as f:
    file = csv.DictReader(f)
    #checking each row and extracting product and date 
    for data in file:        
        product = data['Product']
        date=data['Date received']
         
        #IF Data is missing- it will be handeled by try except block
        try:
            #Extracting year from date
                dArr = date.split('-')
                for year in dArr:
                    try:
                            #checking year should be integer only
                            if len(year) == 4 and int(year):
                                #print(year)
                                company = data['Company']
                                #If result dictionary is empty
                                if result.get(product) == None:
                                    result[product] = {year : {'totalComplaints' : 1, 'companies':{company : 1}}}
                                else:
                                    #making pairs in dictionary with product, year & company count 
                                    if result[product].get(year) == None:
                                        result[product][year] = {'totalComplaints' : 1, 'companies':{company : 1}}
                                    else:
                                        #counting total complaints
                                        totalComplaints = result[product][year]['totalComplaints']
                                        result[product][year]['totalComplaints'] = totalComplaints + 1
                                        #compnies atleast having one complaint
                                        if  result[product][year]['companies'].get(company) != None:
                                            totalComplaintsPerCompany = result[product][year]['companies'][company] + 1
                                            result[product][year]['companies'][company] = totalComplaintsPerCompany
                                        else:
                                            result[product][year]['companies'][company] = 1
                    except:
                            print('not a valid date')
        except:
               print('could not parese the date')

#sorting of Product dictionary with Keys(product name)
for product in sorted(result.keys()):
    #print('product '+product)

#writing a report.csv
with open('output/report.csv', mode='w') as f:
    for x in sorted(result.keys()):
        #check if product name contain comma 
        space= "," in x 
        productName=''
        if space: 
            #Product name contains comma so put it in double quotes         
            productName='\"' + x + '\"'
        else:
            
             productName= x
        #print('--------------------')
        for m in sorted(result[x].keys()):
            #writing product name in LOWER CASE
            f.write(productName.lower())
            #writing year, number of complaints and compnies having complaints
            f.write(','+ m + ','+ str(result[x][m]['totalComplaints']) + ','+ str(len(result[x][m]['companies'])))
            highestComplaints = 0
            compnayNameofHighest = ''
            #calculation of percentage of total complaints filed against one company 
            for company, total in result[x][m]['companies'].items():
                if total > highestComplaints :
                    highestComplaints = total
                    compnayNameofHighest = company
               
            percentage = round((highestComplaints*100) / (result[x][m]['totalComplaints'] + 0.0))

            f.write(','+ str(int(percentage)))
            f.write('\n')
            
           