# Generate rollback SQL and redo SQL from MySQL binlog 
### Description
The script is used to analyze MySQL binlog and generate rollback SQL
### Usage
- Step 1: Modify parameters in ./config.py 

```
If you want to generate results in local files, "LocalDatabase" in config.py is not required.
```
 
- Step 2: Run script: python ./BinlogAnalyzer.py file [file|db] 

```
Usage 1 - generate results in files   : python ./BinlogAnalyzer.py file
Usage 2 - generate results in database: python ./BinlogAnalyzer.py db
```
### Requirements
-  System  : Linux
-  Python  : Python 2.7
-  binlog  : binlog file from MySQL 5.1 - 5.7
