SELECT DISTINCT 
    classid 
FROM
    dbo.studentTbl
WHERE
    classid NOT IN (
        'NURSERY-1',
        'NURSERY-1B',
        'NURSERY-2C',
        'KG-1D',
        'KG-1E',
        'KG-2E',
        'BASIC-STAGE-3D',
        'BASIC-STAGE-4D',
        'BASIC-STAGE-7',
        'BASIC-STAGE-8',
        'BASIC-STAGE-9',
        'UNASSIGNED',
        'ALUMNI'
    )
ORDER BY 
    classid ASC;
