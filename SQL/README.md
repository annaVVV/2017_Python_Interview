# SQL Query Interview Questions and Answers

### Question 1: SQL Query to find second highest salary of Employee
Answer: There are many ways to find second highest salary of Employee in SQL, you can either use SQL Join or Subquery to solve this problem. Here is SQL query using Subquery:

```
select MAX(Salary) from Employee WHERE Salary NOT IN (select MAX(Salary) from Employee ); 
```
See How to find second highest salary in SQL for more ways to solve this problem.

### Question 2: SQL Query to find Max Salary from each department.
Answer: You can find the maximum salary for each department by grouping all records by DeptId and then using MAX() function to calculate maximum salary in each group or each department.
```
SELECT DeptID, MAX(Salary) FROM Employee  GROUP BY DeptID. 
```
These questions become more interesting if Interviewer will ask you to print department name instead of department id, in that case, you need to join Employee table with Department using foreign key DeptID, make sure you do LEFT or RIGHT OUTER JOIN to include departments without any employee as well.  Here is the query
```
SELECT DeptName, MAX(Salary) FROM Employee e RIGHT JOIN Department d ON e.DeptId = d.DeptID GROUP BY DeptName;
```
In this query, we have used RIGHT OUTER JOIN because we need the name of the department from Department table which is on the right side of JOIN clause, even if there is no reference of dept_id on Employee table. 

### Question 3: Write SQL Query to display the current date.
Answer: SQL has built-in function called GetDate() which returns the current timestamp. This will work in Microsoft SQL Server, other vendors like Oracle and MySQL also has equivalent functions.
```
SELECT GetDate(); 
```
Question 4: Write an SQL Query to check whether date passed to Query is the date of given format or not.
Answer: SQL has IsDate() function which is used to check passed value is a date or not of specified format, it returns 1(true) or 0(false) accordingly. Remember ISDATE() is an MSSQL function and it may not work on Oracle, MySQL or any other database but there would be something similar.
```
SELECT  ISDATE('1/08/13') AS "MM/DD/YY"; 
```
It will return 0 because passed date is not in correct format.

### Question 5: Write an SQL Query to print the name of the distinct employee whose DOB is between 01/01/1960 to 31/12/1975.
Answer: This SQL query is tricky, but you can use BETWEEN clause to get all records whose date fall between two dates.
```
SELECT DISTINCT EmpName FROM Employees WHERE DOB  BETWEEN ‘01/01/1960’ AND ‘31/12/1975’;
```

### Question 6: Write an SQL Query find number of employees according to gender  whose DOB is between 01/01/1960 to 31/12/1975.
```
SELECT COUNT(*), sex from Employees  WHERE  DOB BETWEEN '01/01/1960' AND '31/12/1975'  GROUP BY sex;
```

### Question 7: Write an SQL Query to find an employee whose Salary is equal or greater than 10000.
```
SELECT EmpName FROM  Employees WHERE  Salary>=10000;
```

### Question 8: Write an SQL Query to find name of employee whose name Start with ‘M’
``` 
SELECT * FROM Employees WHERE EmpName like 'M%';
```

### Question 9: find all Employee records containing the word "Joe", regardless of whether it was stored as JOE, Joe, or joe.
```
SELECT * from Employees  WHERE  UPPER(EmpName) like '%JOE%';
```

### Question 10: Write an SQL Query to find  the year from date.
Answer:  Here is how you can find Year from a Date in SQL Server 2008 
```
SELECT YEAR(GETDATE()) as "Year";
```

### Question 11: Write SQL Query to find duplicate rows in a database? and then write SQL query to delete them?
Answer: You can use the following query to select distinct records:
```
SELECT * FROM emp a WHERE rowid = (SELECT MAX(rowid) FROM EMP b WHERE a.empno=b.empno)
```
to Delete:
```
DELETE FROM emp a WHERE rowid != (SELECT MAX(rowid) FROM emp b WHERE a.empno=b.empno);
```

### Question 12: There is a table which contains two column Student and Marks, you need to find all the students, whose marks are greater than average marks i.e. list of above average students.
Answer: This query can be written using subquery as shown below:
```
SELECT student, marks from table where marks > SELECT AVG(marks) from table)
```

## SQL Query Interview Questions and Answers

### Question 13: How do you find all employees which are also manager? .
You have given a standard employee table with an additional column mgr_id, which contains employee id of the manager.
Employee department SQL Query question
Answer: You need to know about self-join to solve this problem. In Self Join, you can join two instances of the same table to find out additional details as shown below
```
SELECT e.name, m.name FROM Employee e, Employee m WHERE e.mgr_id = m.emp_id;
```
this will show employee name and manager name in two column e.g.

name  manager_name
John   David

One follow-up is to modify this query to include employees which don't have a manager. To solve that, instead of using the inner join, just use left outer join, this will also include employees without managers.


### Question 14: You have a composite index of three columns, and you only provide the value of two columns in WHERE clause of a select query? Will Index be used for this operation? For example if Index is on EmpId, EmpFirstName, and EmpSecondName and you write query like
```
SELECT * FROM Employee WHERE EmpId=2 and EmpFirstName='Radhe'
```
If the given two columns are secondary index column then the index will not invoke, but if the given 2 columns contain the primary index(first column while creating index) then the index will invoke. In this case, Index will be used because EmpId and EmpFirstName are primary columns


Read more: http://www.java67.com/2013/04/10-frequently-asked-sql-query-interview-questions-answers-database.html#ixzz4q7PhtAHJ
