

use faers;


util.importTable("C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/DEMO20Q1.txt", {table:"DEMO", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"})

util.importTable("file:///C:\ZC\Research/FAERS/data/faers_ascii_2020Q1/ASCII/DRUG20Q1.txt", {table:"DRUG", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"});

util.importTable("file:///C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/INDI20Q1.txt", {table:"indi", skipRows: 1, fieldsTerminatedBy:"$"});

util.importTable("file:///C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/OUTC20Q1.txt", {table:"OUTC", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"});

util.importTable("file:///C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/REAC20Q1.txt", {table:"REAC", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"});

util.importTable("file:///C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/RPSR20Q1.txt", {table:"RPSR", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"});

util.importTable("file:///C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/STAT20Q1.txt", {table:"STAT", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"});

util.importTable("file:///C:/ZC/Research/FAERS/data/faers_ascii_2020Q1/ASCII/THER20Q1.txt", {table:"THER", skipRows: 1, linesTerminatedBy:"\r\n", fieldsTerminatedBy:"$"});

