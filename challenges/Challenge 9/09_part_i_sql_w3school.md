# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to a copy of this markdown file and submit in your student_submissions folder.

1. Which customers are from the UK?

SELECT * FROM [Customers] where Country='UK'

2. What is the name of the customer who has the most orders?

SELECT CustomerName, count(*) as OrderCount FROM [Customers]
JOIN Orders on Customers.CustomerID=Orders.CustomerID
GROUP BY Orders.CustomerID
ORDER BY OrderCount DESC


3. Which supplier has the highest average product price?

SELECT SupplierName, AVG(Products.Price) AS AverageProductPrice FROM [Products]
JOIN Suppliers on Suppliers.SupplierID=Products.SupplierID
GROUP BY Products.SupplierID
ORDER BY AVG(Products.Price) DESC

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

SELECT count(DISTINCT Country) FROM [Customers]

5. What category appears in the most orders?

6. What was the total cost for each order?

SELECT OrderID, SUM(Products.Price * OrderDetails.Quantity) FROM [OrderDetails]
JOIN Products ON Products.ProductID=OrderDetails.ProductID
GROUP BY OrderID

7. Which employee made the most sales (by total price)?

SELECT EmployeeID, SUM(Quantity * Price) as TotalSales FROM [Orders]
JOIN OrderDetails
ON Orders.OrderID = OrderDetails.OrderID
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
GROUP BY EmployeeID
ORDER BY TotalSales DESC


8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

SELECT * FROM Employees
WHERE Notes LIKE '%BS%'

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

SELECT COUNT(Products.ProductID) AS NoProducts, Suppliers.SupplierID, AVG(Products.Price) AS AverageProductPrice FROM Suppliers
JOIN Products ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
HAVING NoProducts > 3
