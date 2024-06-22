--Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.--


SELECT number, 
  CASE  WHEN number % 2 = 0 THEN 'Even'
        ELSE 'Odd' END
        AS is_even
FROM numbers