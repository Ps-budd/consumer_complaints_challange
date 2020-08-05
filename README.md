# consumer_complaints_challange

# Table of contents

1. [Problem](README.md#Problem)
2. [Input](README.md#Input)
3. [Approach & Algorithm](README.md#Approach)
4. [Output](README.md#Output)
5. [Test-cases](README.md#Test-cases)
5. [Run Instructions](README.md#Run-Instructions)
6. [Contact](README.md#Contact)


# Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate : **number of complaints** , **number of companies receiving a complaint** and **highest percentage of complaints directed at a single companyfor** each financial product & year.
  
# Input 
Raw data could be found [here](https://github.com/insightdatascience/consumer_complaints) under the __Input Dataset__ tab
for this soltuion they have provided `complaints.csv` which contain data of complaints for different product.
For example you can find the input snippet in the Test-cases tab.

# Approach
My steps to solve this problem is<br>
  read file contents line by line<br>
  understand schema from header<br>
  clean data row if necessary<br>
  insert required data into dictionary<br>
  sort dictionary<br>
  write data to output file<br>
  
### Version 1:
  In the begning in order to solve problem i read the file and put data into dictionary data sctructure as it perfectly suit the prblem and less execution time of it. I was     creating different dictionary for different header.
  
But later on I realised the data is very large, not clean and data parsing fails for some rows. so i cleaned the data before adding to dictionary.

### Version 2:
 Since data is large so i came up with new solution by making **Nested Dictionary(Dictionary of Dictionary)**, which is more suitable to the problem, and it makes more sense for the analysis I have to perform.
 so I cleaned the data and then performed the parsing and inserted into dictionary.
 used following-  
      **Python <br>
      dictionary data structure**
 once `complaints.py` starts reading the data it starts making pairs of Products with year and total number of complaints for this product and year pair with the use of nested Dictionary data structure. once your dictionary is ready you have Analysed report.

### Algorithm
step 1: Create result Dictionary<br>
step 2: Open complaints.csv in read mode<br>
step 3: check each row from `complaints.csv` and extract product & date<br>
      3.1 if row has missing value in any product, year or company. discard row and go back to step 2.
step 4: extract year from date<br>
step 5: if resul key is empty <br>
        5.1 put the product, year complaintcount=1 & compnies=1 in result<br>
        5.2 similarly check for nested dictonary year key<br>
step 6: increase the complaints count by 1<br>
step 7: calculate total complaints per compnies<br>
step 8 : open report.csv in writing mode<br>
step 9: sort the result dictionary- key wise<br>
step10: if product name contain comma put product name in double quotes<br>
step 11:write product name(lowercase), year, total number of complaints, compnies having complaints <br>
step 12: calculate percentage= round((highestComplaints*100) / totalComplaints) <br>
step 13: put percentage into report.csv<br>

# Output
This program creates 1 output file:
`report.csv` which contain report for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.
`report.csv` holds the each record in that order- product,year,total number of complaints received for that product and year,total number of companies receiving at least one complaint for that product and year,highest percentage of total complaints filed against one company 

# Test-cases
__Test 1__
      input- complaints.csv file with missing values of year <br>
  
  ``` 
  Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
  ```
      output- missing value handled properly<br>
   ```
   "credit reporting, credit repair services, or other personal consumer reports",2019,2,2,50
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100

   ```
      
<b>Test 2</b>
      input- complaints.csv file with missing values of compnies<br>
      output- report file do not add the missing company in total compny count<br>
      
      
 <b>Test 3</b>
     input- complaints.csv file with missing values of product <br>
      output- missing value handled properly and calculation of percentage of total complaints filed against one company  is correct<br>
     

<b>Test 4</b>
      input- test case provided by insight_datascience team<br>
      output- report.csv matchs the result to insight data science output.<br>
      
 <b>Test 5</b>
      input- complaints.csv file(~900mb) provided by insight_datascience team<br>
      output- report.csv matchs the result. <br>
      **Note**- large dataset tested. Test 5-input doesn't contain complaints.csv file becasue git hub do not allow file exceed 100mb.<br>
