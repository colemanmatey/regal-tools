SELECT
	ROW_NUMBER() OVER (ORDER BY classid, gender DESC, fname, lname) AS 'S/N',
	admissionNumber AS 'Student No.',
	CONCAT(fname, ' ', lname) AS 'Name',
	classid AS 'Class',
	feePayable * -1 AS 'Arrears'
FROM
	dbo.studentTbl
WHERE 
	feePayable < 0  AND status = 'Active'
ORDER BY 
	classid, gender DESC, fname, lname
