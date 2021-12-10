## This file generates the SQL Shell script that will be run to initialize the data from the necessary files

## Setup 
base_statement = 'util.importTable("C:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/DATA/'
mid_statement = '.txt", {table:"'
end_statement = '", skipRows: 1, fieldsTerminatedBy:"$"})'
# end_statement = '", skipRows: 1, linesTerminatedBy:"\\r\\n", fieldsTerminatedBy:"$"})'
# base_statement = 'LOAD DATA INFILE \'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'
# mid_statement = '.txt\' REPLACE INTO TABLE '
# end_statement = ' CHARACTER SET utf8 FIELDS TERMINATED BY \'$\' LINES TERMINATED BY \'\\n\' IGNORE 1 ROWS;'
# -- LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/DEMO20Q1.txt' REPLACE INTO TABLE demo CHARACTER SET utf8 FIELDS TERMINATED BY '$' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

## Declare all year and quarter strings
year = ["21"]
# year = ["04", "05", "06", "07", "08", "09", "10", "11",
#         "12", "13", "14", "15", "16", "17", "18", "19", "20"]

quarter = ["Q3"]
# quarter = ["Q1", "Q2", "Q3", "Q4"]

## List of database names
db_names = ["DEMO", "DRUG", "INDI", "OUTC", "REAC", "RPSR", "STAT", "THER"]

## Open .sql script file
f = open("testfile.sql", "x")

## Prewritten string to declare all tables.

table_create = """CREATE DATABASE faers;\r\n\r\nUSE faers;\r\n\r\ncreate table demo
(\r\nprimaryid varchar(255),\r\ncaseid varchar(255),\r\ncaseversion varchar(255),\r\n
i_f_code varchar(255),\r\nevent_dt varchar(255),\r\nmfr_dt varchar(255),
\r\ninit_fda_dt varchar(255),\r\nfda_dt varchar(255),\r\nrept_cod varchar(255),
\r\nauth_num varchar(255),\r\nmfr_num varchar(255),\r\nmfr_sndr varchar(255),
\r\nlit_ref longtext,\r\nage varchar(255),\r\nage_cod varchar(255),
\r\nage_grp varchar(255),\r\nsex varchar(255),\r\ne_sub varchar(255),
\r\nwt varchar(255),\r\nwt_cod varchar(255),\r\nrept_dt varchar(255),
\r\nto_mfr varchar(255),\r\noccp_cod varchar(255),\r\nreporter_country varchar(255),
\r\noccr_country varchar(255));\r\n\r\ncreate table drug (\r\nprimaryid varchar(255),
\r\ncaseid varchar(255),\r\ndrug_seq varchar(255),\r\nrole_cod varchar(255),
\r\ndrugname varchar(255),\r\nprod_ai longtext,\r\nval_vbm varchar(255),
\r\nroute varchar(255),\r\ndose_vbm varchar(255),\r\ncum_dose_chr varchar(255),
\r\ncum_dose_unit varchar(255),\r\ndechal varchar(255),\r\nrechal varchar(255),
\r\nlot_num varchar(255),\r\nexp_dt varchar(255),\r\nnda_num varchar(255),
\r\ndose_amt varchar(255),\r\ndose_unit varchar(255),\r\ndose_form varchar(255),
\r\ndose_freq varchar(255));\r\n\r\ncreate table indi (\r\nprimaryid varchar(255),
\r\ncaseid varchar(255), \r\nindi_drug_seq varchar(255), \r\nindi_pt varchar(255));
\r\n\r\ncreate table outc ( \r\nprimaryid varchar(255),\r\ncaseid varchar(255),
\r\noutc_cod varchar(255));\r\n\r\ncreate table reac (\r\nprimaryid varchar(255),
\r\ncaseid varchar(255),\r\npt varchar(255),\r\ndrug_rec_act varchar(255));
\r\n\r\ncreate table rpsr (\r\nprimaryid varchar(255),\r\ncaseid varchar(255),
\r\nrpsr_cod varchar(255));\r\n\r\ncreate table ther (\r\nprimaryid varchar(255),
\r\ncaseid varchar(255),\r\ndsg_drug_seq varchar(255),\r\nstart_dt varchar(255),
\r\nend_dt varchar(255),\r\ndur varchar(255),\r\ndur_cod varchar(255));\r\n\r\n"""

## Write script to top of file.
# f.write(table_create)
# f.write("\r\n\r\n")

## Include each combination of year, quarter, and database name in list.
for i in range(0, len(db_names)):
    for j in range(0, len(year)):
        for k in range(0, len(quarter)):
            temp = base_statement + db_names[i] + year[j] + quarter[k] + mid_statement + db_names[i] + end_statement
            f.write(temp)
            f.write("\r\n")

## Close file
f.close()

