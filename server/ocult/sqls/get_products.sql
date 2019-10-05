SELECT
    CPRD.PROD_CODIGO as 'erpId',
    ISNULL(CPRD.CSI_ID, -1) as 'id',
	ISNULL(CPRD.VARIANTE_CSI_ID, -1) as 'variantId',
	ISNULL(CPRD.CATEGORIA_CSI_ID, -1) as 'mainDepartmentId',
	MARC.MARC_NOME as 'brand'
FROM
    CSI_PRODUTO CPRD
LEFT JOIN
	PRODUTOS PROD
	ON CPRD.PROD_ID = PROD.PROD_ID
LEFT JOIN
	MARCAS MARC
	ON PROD.MARC_ID = MARC.MARC_ID