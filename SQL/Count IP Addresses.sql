/* Given a database of first and last IPv4 addresses, calculate the number of addresses between them (including the first one, excluding the last one).
Input

---------------------------------
|     Table    | Column | Type  |
|--------------+--------+-------|
| ip_addresses | id     | int   |
|              | first  | text  |
|              | last   | text  |
---------------------------------

Output

-------------------------
|   Column    |  Type   |
|-------------+---------|
| id          | int     |
| ips_between | bigint  |
-------------------------

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
Examples

* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246 */



select id, last::inet - first::inet as ips_between from ip_addresses;



