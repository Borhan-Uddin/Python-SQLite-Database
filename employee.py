import sqlite3
from emp import emp

con = sqlite3.connect("employee.db")

c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS employee ( first_name text, last_name text, salary integer)" )

def create_emp(emp):
	with con:
		c.execute("INSERT INTO employee VALUES(?,?,?)",(emp.first_name,emp.last_name,emp.salary))

def remove_emp(emp):
	with con:
		c.execute("DELETE FROM employee WHERE first_name = :first_name AND last_name=:last_name",{'first_name':emp.first_name,'last_name':emp.last_name})

def get_emp_salary(emp):

	c.execute("SELECT salary FROM employee WHERE first_name = :first AND last_name=:last",{'first':emp.first_name,'last':emp.last_name})
	return c.fetchall()

def upodate_emp(emp,salary):
	with con:
		c.execute("UPDATE employee SET salary = :salary WHERE first_name = :first AND last_name = :last",{'first':emp.first_name,'last':emp.last_name,'salary':salary})


#insert_q = " INSERT INTO employee VALUES (':first',:'last',:'salary')"
e1 = emp('Corey','Schefer',5000)
e2 = emp('Raihan','Ullah',3000)

create_emp(e1)
create_emp(e2)

print(get_emp_salary(e1))

remove_emp(e2)
#upodate_emp(e2,4000)

print(get_emp_salary(e2))

con.close()



