# :scroll: SQL-Data-Base :books:
## :clipboard: Basic-Commands :pushpin:

### :fire: Fire!!! :fire:
![This is picture.](/Images/Inspiration_n_love/Napoleon.jpg "Go Go Go")

> * :hand: [Begin](#scroll-sql-data-base-books) :point_right:

* :shipit: **SELECT** :octocat:
    ```
    - SELECT column1, column2, ... 
    FROM table_name;
    Ex. 
    SELECT CustomerName, City 
    FROM Customers;
    - SELECT DISTINCT column1, column2, ... 
    FROM table_name;
    Ex. 
    SELECT DISTINCT Country 
    FROM Customers;
    - SELECT COUNT(DISTINCT column) 
    FROM table_name;
    Ex. 
    SELECT COUNT(DISTINCT Country) 
    FROM Customers;
    ```
* :alien: **WHERE** :milky_way:
    ```
    - SELECT column1, column2, ... 
    FROM table_name 
    WHERE condition;
    Ex. 
    SELECT * 
    FROM Customers 
    WHERE Country='Mexico';
    > ถ้าเป็นตัวเลขไม่จำเป็นต้องมี '' แต่ ถ้าเป็นตัวอักษรหรือคำอะ ต้องมี ''
    > ประเภทของ Condition จะมี ดังนี้
        - WHERE column = 
        - WHERE column >
        - WHERE column <
        - WHERE column <=
        - WHERE column >=
        - WHERE column <> || WHERE NOT column = 
        - WHERE column BETWEEN 50 OR 60
        - WHERE column LIKE 's%' ขยายๆ s% หมายถึง คำที่ขึ้นต้นด้วยตัวอักษร S
        - WHERE column IN ('Paris', 'London') 
    ```
* :page_with_curl: **ORDER BY** :scroll:
    ```
    - SELECT column1, column2, ... 
    FROM table_name 
    ORDER BY column1, column2, ... ASC|DESC;
    EX. 
    SELECT * 
    FROM Customers 
    ORDER BY Country ASC, CustomerName DESC;
    > ASC - Ascending คือค่า Default ของการจัดเรียง (Order By)
    > DESC - Descending คือ ค่าของการจัดเรียงแบบ Reverse
    > เลือกใช้อย่างใดอย่างนึงพอ ใน แต่ละ Column อะนะ
    ```
* :camera: **And Operator** :video_camera:
    ```
    - SELECT column1, column2, ... 
    FROM table_name 
    WHERE condition1 AND condition2 ...;
    - Condition ต้องจริงทั้งหมดนะ ถ้ามีอันไหนไม่จริงก็แตกเอาออกมาไม่ได้
    EX. 
    SELECT * FROM Customers
    WHERE Country = 'Spain' AND CustomerName LIKE 'G%';
    ```
* :heavy_plus_sign: **Combining AND and OR** :heavy_multiplication_x:
    ```
    Ex. 
    SELECT * 
    FROM Customers
    WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');
    > ถ้าไม่มีวงเล็บอะ ผลลัพธ์ที่จะได้ คือ เราจะได้คนที่ชื่อขึ้นด้วยตัว G ที่อยู่ประเทศ Spain แต่เราจะได้คนที่ชื่อขึ้นต้นด้วยตัว R อะจากประเทศบ้างก็ไม่รู้
    ```
* :house: **OR Operator** :house_with_garden:
    ```
    - SELECT column1, column2, ... 
    FROM table_name 
    WHERE condition1 OR condition2 OR condition3 ...;
    > Condition ไม่จำเป็นต้องจริงทั้งหมดก็แค่มีจริงอย่างใดอย่างนึงทำเลย
    ```
* :x: **NOT Operator** :heavy_exclamation_mark:	
    ```
    - SELECT column1, column2, ... 
    FROM table_name 
    WHERE NOT condition;
    > ตัวอย่างการวาง NOT หน้า Column
    EX. 
    SELECT * 
    FROM Customers 
    WHERE NOT Country = 'Spain';
    > ตัวอย่างการวาง NOT หน้า Condition
    Ex. 
    SELECT * 
    FROM Customers 
    WHERE CustomerName NOT LIKE 'A%';
    ```
* :email: **INSERT INTO** :mailbox:
    ```
    - INSERT INTO table_name (column1, column2, column3, ...) 
    VALUES (value1, value2, value3, ...);
    EX. 
    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) 
    VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
    > ถ้าไม่ได้ใส่ค่าตาม Column นั้นๆ จะกลายเป็น NULL
    ```
* :thought_balloon: **NULL Values** :speech_balloon:
    ```
    - IS NULL Syntax = ทำให้ Column กลายเป็น NULL
    SELECT column_names
    FROM table_name
    WHERE column_name IS NULL;
    Ex. 
    SELECT CustomerName, ContactName, Address
    FROM Customers
    WHERE Address IS NULL;
    - IS NOT NULL Syntax = ปกติ
    SELECT column_names
    FROM table_name
    WHERE column_name IS NOT NULL;
    EX.
    SELECT CustomerName, ContactName, Address
    FROM Customers
    WHERE Address IS NOT NULL;
    ```
* :small_red_triangle: **UPDATE Statement** :small_red_triangle_down:
    ```
    - UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
    EX.
    UPDATE Customers
    SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
    WHERE CustomerID = 1;
    ```