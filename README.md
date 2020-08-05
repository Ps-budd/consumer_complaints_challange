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
step 3: check eacch row from complaints.csv and extract product & date<br>
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
