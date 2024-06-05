# SqlServerStatisticsParser

This repo contains a sample python script for parsing the IO and CPU statistics returned in SQL Server Management Studio when you set the following command in a SQL script: `SET STATISTICS IO, CPU ON`

Tested with message outputs from SSMS 2017




**Instructions:**
1. In SQL Server Management Studio, open a new Query tab
2. Enable Statistics IO/Time.
```
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
```
3. Run the desired query that you want to measure performance metrics on
4. Copy the messages from the Messages tab into the input.txt file content
5. Run the python script 
`python .\sqlstatsparser.py`
6. Summarised outputs of logical reads and time will be displayed
e.g.
```
CPU time: 39873 ms
Logical reads: 426222
Physical reads: 0
Read aheads: 48
Elapsed time: 7445 ms
Table 'TestTable1': 345687
Table 'Worktable': 54407
Table 'xml_index_nodes_893246237_256000': 24762
Table 'TestTable2': 1044
Table 'TestTable3': 310
Table 'Workfile': 0
```