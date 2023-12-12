WITH CombinedData AS (
	SELECT
		admissionNumber AS 'Student No.',
		CONCAT(fname, ' ', lname) AS 'Name',
		classid AS 'Class',
		(feePayable + 700) * -1 AS 'Arrears'
	FROM
		dbo.studentTbl
	WHERE 
		feePayable < -700  
		AND status = 'Active' 
		AND departmentid IN ('PRE-SCHOOL', 'LOWER-PRIMARY', 'UPPER-PRIMARY')
	UNION
	SELECT
		admissionNumber AS 'Student No.',
		CONCAT(fname, ' ', lname) AS 'Name',
		classid AS 'Class',
		(feePayable + 750) * -1 AS 'Arrears'
	FROM
		dbo.studentTbl
	WHERE 
		feePayable < -750  
		AND status = 'Active' 
		AND departmentid = 'JHS'
)

SELECT 
	ROW_NUMBER() OVER (ORDER BY Class) AS 'S/N',
	[Student No.],
	Name,
	Class,
	Arrears
FROM
	CombinedData
ORDER BY Class
