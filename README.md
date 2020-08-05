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
__Test 1__<br>
      input- complaints.csv file with missing values of year <br>
  
  ``` 
  Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
  ```
      output- missing value handled properly- the output does not consider the missing year. for year:2019, Product: credit reporting, credit repair services, or other personal consumer reports ,there are  2 complaints which is having 50% complaints filed against one company <br>
   ```
   "credit reporting, credit repair services, or other personal consumer reports",2019,2,2,50
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100

   ```
      
__Test 2__<br>
      input- complaints.csv file with missing values of company name <br>
  
  ``` 
  Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
  ```
      output- There was 3 complaints but due to one compny name missing percentage is 33  <br>
   ```
   "credit reporting, credit repair services, or other personal consumer reports",2019,3,3,33
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100


   ```
     
      
      
 
     
__Test 3__
      input- `complaints.csv` file with missing values of product<br>
  
  ``` 
  Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24, ,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
  ```
      output- It shows one complaint in 2019 becuase this row product name is not match to other two. It is not affecting any other row. <br>
   ```
   " ,2019,1,1,100
"credit reporting, credit repair services, or other personal consumer reports",2019,3,3,33
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100


   ```

   
 __Test 4__
      input- `complaints.csv` file givien by **Insight data science team** <br>
  
  ``` 
  Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
  ```
      output- report.csv matchs the result to insight data science output.<br>
   ```
 "credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100

   ```     
 <b>Test 5</b>
      input- complaints.csv file(~900mb) provided by insight_datascience team<br>
      output- report.csv matchs the result. <br>
      **Note**- large dataset tested. Test 5-input doesn't contain complaints.csv file becasue git hub do not allow file exceed 100mb.<br>
__Test 5__
      input- **large data set** `complaints.csv` file which can be find [here](https://github.com/insightdatascience/consumer_complaints) <br>
  **Note- data is too large-can not push to github due to file size restrictions **
    ```  
      output- report.csv which shows following correct result.
   ```
  bank account or service,2012,12212,98,19
bank account or service,2013,13388,164,18
bank account or service,2014,14662,258,17
bank account or service,2015,17140,215,17
bank account or service,2016,21848,230,15
bank account or service,2017,6956,174,16
checking or savings account,2017,12763,183,17
checking or savings account,2018,21269,217,16
checking or savings account,2019,23496,284,14
checking or savings account,2020,6575,153,47
consumer loan,2012,1986,84,19
consumer loan,2013,3117,159,12
consumer loan,2014,5457,358,8
consumer loan,2015,7886,599,9
consumer loan,2016,9601,665,7
consumer loan,2017,3557,425,8
credit card,2011,1260,33,19
credit card,2012,15353,76,20
credit card,2013,13105,108,19
credit card,2014,13974,178,17
credit card,2015,17300,225,17
credit card,2016,21065,221,21
credit card,2017,7133,127,18
credit card or prepaid card,2017,15404,170,15
credit card or prepaid card,2018,24253,252,15
credit card or prepaid card,2019,25836,245,15
credit card or prepaid card,2020,4121,111,18
credit reporting,2012,1873,31,38
credit reporting,2013,14380,203,36
credit reporting,2014,29239,214,35
credit reporting,2015,34272,237,35
credit reporting,2016,44081,182,36
credit reporting,2017,16587,403,30
"credit reporting, credit repair services, or other personal consumer reports",2017,73394,1020,35
"credit reporting, credit repair services, or other personal consumer reports",2018,111732,1310,26
"credit reporting, credit repair services, or other personal consumer reports",2019,139414,1325,28
"credit reporting, credit repair services, or other personal consumer reports",2020,28098,548,29
debt collection,2013,11069,984,9
debt collection,2014,39139,1756,6
debt collection,2015,39724,2136,5
debt collection,2016,40468,2135,4
debt collection,2017,47954,2241,4
debt collection,2018,51234,2255,5
debt collection,2019,46664,2105,4
debt collection,2020,7378,1053,4
"money transfer, virtual currency, or money service",2017,3266,178,32
"money transfer, virtual currency, or money service",2018,5436,236,30
"money transfer, virtual currency, or money service",2019,5081,260,26
"money transfer, virtual currency, or money service",2020,696,93,21
money transfers,2013,559,58,30
money transfers,2014,1169,67,32
money transfers,2015,1619,79,32
money transfers,2016,1567,80,25
money transfers,2017,440,46,27
mortgage,2011,1276,66,33
mortgage,2012,38109,382,31
mortgage,2013,49400,454,25
mortgage,2014,42961,495,14
mortgage,2015,42345,680,12
mortgage,2016,41466,766,14
mortgage,2017,30577,772,12
mortgage,2018,24778,705,13
mortgage,2019,23779,658,9
mortgage,2020,4427,265,30
other financial service,2014,116,38,12
other financial service,2015,312,99,10
other financial service,2016,465,154,5
other financial service,2017,166,76,7
payday loan,2013,194,31,13
payday loan,2014,1706,159,17
payday loan,2015,1585,243,8
payday loan,2016,1565,213,17
payday loan,2017,493,107,12
"payday loan, title loan, or personal loan",2017,2958,392,6
"payday loan, title loan, or personal loan",2018,4391,470,5
"payday loan, title loan, or personal loan",2019,4355,478,4
"payday loan, title loan, or personal loan",2020,647,193,12
prepaid card,2014,336,29,22
prepaid card,2015,1784,48,42
prepaid card,2016,1250,51,21
prepaid card,2017,449,30,19
student loan,2012,2840,53,42
student loan,2013,3005,91,46
student loan,2014,4283,137,44
student loan,2015,4501,171,37
student loan,2016,8087,232,34
student loan,2017,17173,232,63
student loan,2018,8781,202,46
student loan,2019,7212,189,41
student loan,2020,1004,87,31
vehicle loan or lease,2017,3694,249,13
vehicle loan or lease,2018,5901,316,12
vehicle loan or lease,2019,5482,318,12
vehicle loan or lease,2020,825,128,12
virtual currency,2014,1,1,100
virtual currency,2015,7,1,100
virtual currency,2016,7,2,57
virtual currency,2017,3,1,100


   ```
