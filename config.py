#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
from pymysql.cursors import DictCursor

#---------------------------------------------------------------------------------------------------------
# Required arguments, used to filter sqls from binlog file
#---------------------------------------------------------------------------------------------------------
binlogFile = '/home/mysql_1/mysql11301/log/bin_log/mysql_bin_1.000065'

#---------------------------------------------------------------------------------------------------------
# Optional arguments, used to filter sqls from binlog file
#---------------------------------------------------------------------------------------------------------
schemaName = 'db_ops'
tableName  = 'monitor_dbmonitorinfo'
#tableName  = ''
startTime  = ''
endTime    = ''
#endTime    = '2017-09-12 00:00:00'
startPos   = ''
endPos     = ''

#---------------------------------------------------------------------------------------------------------
# The instance where you get your binlog file from, used to get DDL of the tables.
# Min privilege:
#    GRANT SELECT ON db_ops.* to  src_db_user@'127.0.0.1' identified by 'FBD38AC9A3C' ;
#---------------------------------------------------------------------------------------------------------
BinlogSource = {
      'host':'127.0.0.1',
      'port':11301,
      'user':'src_db_user',
      'password':'FBD38AC9A3C',
      'charset':'utf8',
      'cursorclass':pymysql.cursors.DictCursor,
      }

#---------------------------------------------------------------------------------------------------------
# Note: If you are running with "python ./BinlogAnalyzer.py db" , below settings are required
# This database is used to store result redo SQLs and undo SQLs when analyzer is running with db mode
# Min privilege:
#    GRANT SELECT,INSERT,CREATE,DROP,ALTER,INDEX ON test.* to result_view@'%' identified by 'FBD38AC9A3C' ; 
#---------------------------------------------------------------------------------------------------------
LocalDatabase = {
      'host':'127.0.0.1',
      'port':11301,
      'user':'result_view',
      'password':'FBD38AC9A3C',
      'db':'test',
      'charset':'utf8',
      'cursorclass':pymysql.cursors.DictCursor,
      }

