# <h1>consumer_complaints_challange</h1>

<h2>Table of content</h2> <br>

<b>1. Problem statement</b><br>
<b>2. Solution appraoch</b><br>
<b>3. Algorithm</b><br>
<b>4. Test cases</b><br>


<h4>Problem</h4>
<P>For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.
  
  
<h4>Solution Approach</h4>
      Python used<br>
      dictionary data structure<br>
  <p> Read the complaints.csv file and starts making pairs of Products with year and total number of complaints for this product and year pair with the use of nested Dictionary data structure. once your dictionary is ready you have Analysis ready of complaints.csv file according to problem statement. From the help of prepared dictionary, analysis is performed and write into the report.csv file. 

<h4>Algorithm</h4>
step 1: Create result Dictionary<br>
step 2: Open complaints.csv in read mode<br>
step 3: check each row from complaints.csv and extract product & date<br>
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

<h4>OUTPUT</h4><br>
**Note**- output is sorted product wise and year wise<br>
<h7>Test Cases</h>
<b>Test 1</b>
      input- complaints.csv file with missing values of year <br>
      output- missing value handled properly<br>
      
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
