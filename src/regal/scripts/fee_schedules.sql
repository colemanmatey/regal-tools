SELECT
	ROW_NUMBER() OVER (ORDER BY classid, gender DESC, fname, lname) AS 'S/N',
	admissionNumber AS 'Student No.',
	CONCAT(fname, ' ', lname) AS 'Name',
	feePayable * -1 AS 'Arrears',
    '' AS 'Part',
    '' AS 'Part' ,
    '' AS 'Part' ,
    '' AS 'Bal' 
FROM
	dbo.studentTbl
WHERE
	status = 'Active'
AND
	classid=?
ORDER BY 
	classid, gender DESC, fname, lname
	