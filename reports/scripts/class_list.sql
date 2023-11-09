SELECT
	ROW_NUMBER() OVER (ORDER BY gender DESC, fname, lname) AS 'S/N',
	admissionNumber AS 'Student No.',
	CONCAT(fname, ' ', lname) AS 'Name',
	classid AS 'Class',
	feePayable * -1 AS 'Arrears'
FROM
	dbo.studentTbl
WHERE
	status = 'Active'
AND
	classid=?
ORDER BY 
	gender DESC, fname, lname
