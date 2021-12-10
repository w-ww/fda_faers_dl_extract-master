CREATE DATABASE faers;



USE faers;



create table demo
(

primaryid varchar(255),

caseid varchar(255),

caseversion varchar(255),


i_f_code varchar(255),

event_dt varchar(255),

mfr_dt varchar(255),


init_fda_dt varchar(255),

fda_dt varchar(255),

rept_cod varchar(255),


auth_num varchar(255),

mfr_num varchar(255),

mfr_sndr varchar(255),


lit_ref varchar(255),

age varchar(255),

age_cod varchar(255),


age_grp varchar(255),

sex varchar(255),

e_sub varchar(255),


wt varchar(255),

wt_cod varchar(255),

rept_dt varchar(255),


to_mfr varchar(255),

occp_cod varchar(255),

reporter_country varchar(255),


occr_country varchar(255));



create table drug (

primaryid varchar(255),


caseid varchar(255),

drug_seq varchar(255),

role_cod varchar(255),


drugname varchar(255),

prod_ai varchar(255),

val_vbm varchar(255),


route varchar(255),

dose_vbm varchar(255),

cum_dose_chr varchar(255),


cum_dose_unit varchar(255),

dechal varchar(255),

rechal varchar(255),


lot_num varchar(255),

exp_dt varchar(255),

nda_num varchar(255),


dose_amt varchar(255),

dose_unit varchar(255),

dose_form varchar(255),


dose_freq varchar(255));



create table indi (

primaryid varchar(255),


caseid varchar(255), 

indi_drug_seq varchar(255), 

indi_pt varchar(255));




create table outc ( 

primaryid varchar(255),

caseid varchar(255),


outc_cod varchar(255));



create table reac (

primaryid varchar(255),


caseid varchar(255),

pt varchar(255),

drug_rec_act varchar(255));




create table rpsr (

primaryid varchar(255),

caseid varchar(255),


rpsr_cod varchar(255));



create table ther (

primaryid varchar(255),


caseid varchar(255),

dsg_drug_seq varchar(255),

start_dt varchar(255),


end_dt varchar(255),

dur varchar(255),

dur_cod varchar(255));