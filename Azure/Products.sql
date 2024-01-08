--Data Pipeline

--Statement to pull the csv information
SELECT
     Category, COUNT(*) AS ProductCount
 FROM
     OPENROWSET(
         BULK 'https://datalakexxxxxxx.dfs.core.windows.net/files/product_data/products.csv',
         FORMAT = 'CSV',
         PARSER_VERSION='2.0',
         HEADER_ROW = TRUE
     ) AS [result]
 GROUP BY Category;

--Generated Chart

--Spark Analysis
%%pyspark
df = spark.read.load('abfss://files@datalakeowgmyf1.dfs.core.windows.net/product_data/products.csv', format='csv'
## If header exists uncomment line below
##, header=True
)
display(df.limit(10))

--Using a dedicated SQL Pool 
 SELECT d.CalendarYear, d.MonthNumberOfYear, d.EnglishMonthName,
        p.EnglishProductName AS Product, SUM(o.OrderQuantity) AS UnitsSold
 FROM dbo.FactInternetSales AS o
 JOIN dbo.DimDate AS d ON o.OrderDateKey = d.DateKey
 JOIN dbo.DimProduct AS p ON o.ProductKey = p.ProductKey
 GROUP BY d.CalendarYear, d.MonthNumberOfYear, d.EnglishMonthName, p.EnglishProductName
 ORDER BY d.MonthNumberOfYear
