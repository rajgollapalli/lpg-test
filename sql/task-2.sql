-- This SQL have been developed using MariaDB as a source
select
	Department,
	Name ,
	Salary
from
	(
	select
		d.Name Department,
		Salary ,
		e.Name ,
		DENSE_RANK() OVER (PARTITION BY DepartmentId
	ORDER BY
		Salary DESC) AS rank
	from
		test.Employee e
	left join test.Department d on
		e.DepartmentId = d.Id) all_employee_departments
where
	rank <= 3