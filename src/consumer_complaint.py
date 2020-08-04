import csv
from datetime import datetime

result = {};
with open('input/complaints.csv', mode='r') as f:
    file = csv.DictReader(f)
    for data in file:
#         print(data['Product'])
        product = data['Product']
        date=data['Date received']
        #year= date[0:4]
        #dt = datetime.strptime(date, '%Y-%m-%d')
        #year=str(dt.year) 

        try:
                dArr = date.split('-')
                for year in dArr:
                    try:
                            if len(year) == 4 and int(year):
                                #print(year)
                                company = data['Company']
                                if result.get(product) == None:
                                    result[product] = {year : {'totalComplaints' : 1, 'companies':{company : 1}}}
                                else:
                                    if result[product].get(year) == None:
                                        result[product][year] = {'totalComplaints' : 1, 'companies':{company : 1}}
                                    else:
                                        totalComplaints = result[product][year]['totalComplaints']
                                        result[product][year]['totalComplaints'] = totalComplaints + 1

                                        if  result[product][year]['companies'].get(company) != None:
                                            totalComplaintsPerCompany = result[product][year]['companies'][company] + 1
                                            result[product][year]['companies'][company] = totalComplaintsPerCompany
                                        else:
                                            result[product][year]['companies'][company] = 1
                    except:
                            print('not a valid date')
        except:
               print('could not parese the date')

# print(result)
# sortedResult= sorted(result)
# result={k: result[k] for k in sortedResult}
for product in sorted(result.keys()):
    print('product '+product)

with open('output/report.csv', mode='w') as f:
    for x in sorted(result.keys()):
        #print('Product : '+ x)
        space= "," in x 
        productName=''
        if space:
           # print('"' + x + '"')
            
            productName='\"' + x + '\"'
        else:
           # print('Product : '+ x)
            
             productName= x
        #print('--------------------')
        for m in sorted(result[x].keys()):
            f.write(productName.lower())
            #print('Year : '+ m + ' totalComplaints : '+ str(result[x][m]['totalComplaints']))
            # print('Year : '+ m + ' totalComplaints : '+ str(result[x][m]['totalComplaints']) + ' totalCompanies '+ str(len(result[x][m]['companies'])))
            f.write(','+ m + ','+ str(result[x][m]['totalComplaints']) + ','+ str(len(result[x][m]['companies'])))
            highestComplaints = 0
            compnayNameofHighest = ''
            for company, total in result[x][m]['companies'].items():
                if total > highestComplaints :
                    highestComplaints = total
                    compnayNameofHighest = company
                # print(company + ' : ' + str(total))
                # print('Highest complaints of :'+compnayNameofHighest + ' with total complaints '+ str(highestComplaints))
                # print(result[x][m]['totalComplaints'])
                # print((highestComplaints*100) / (result[x][m]['totalComplaints'] + 0.0))
            percentage = round((highestComplaints*100) / (result[x][m]['totalComplaints'] + 0.0))

            # print('percentage '+ str(int(percentage)))
            f.write(','+ str(int(percentage)))
            f.write('\n')
            # print('--------------------')
           
        
        
    #print('________________')
