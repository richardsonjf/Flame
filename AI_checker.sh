#!/bin/bash
grep "domain" -r Results/ > hidden_domains_result.txt
cp hidden_domains_result.txt Results/
rm hidden_domains_result.txt
grep "SELECT" -r Results/ > hidden_sql_result.txt
cp hidden_sql_result.txt Results/
rm hidden_sql_result.txt
grep "password" -r Results/ > hidden_password_result.txt
cp hidden_password_result.txt Results/
rm hidden_password_result.txt
grep "username" -r Results/ > hidden_username_result.txt
cp hidden_username_result.txt Results/
rm hidden_username_result.txt
grep "/api/" -r Results/ > hidden_api_result.txt
cp hidden_api_result.txt Results/
rm hidden_api_result.txt
grep "_api" -r Results/ > hidden_api2_result.txt
cp hidden_api2_result.txt Results/
rm hidden_api2_result.txt
grep "_api_" -r Results/ > hidden_api3_result.txt
cp hidden_api3_result.txt Results/
rm hidden_api3_result.txt
grep "api_" -r Results/ > hidden_api4_result.txt
cp hidden_api4_result.txt Results/
rm hidden_api4_result.txt
grep "/spi/" -r Results/ > hidden_spi_result.txt
cp hidden_spi_result.txt Results/
rm hidden_spi_result.txt
grep "/spin/" -r Results/ > hidden_spin_result.txt
cp hidden_spin_result.txt Results/
rm hidden_spin_result.txt
grep "ftp://" -r Results/ > hidden_ftp_result.txt
cp hidden_ftp_result.txt Results/
rm hidden_ftp_result.txt
grep "gopher" -r Results/ > hidden_gopher_result.txt
cp hidden_gopher_result.txt Results/
rm hidden_gopher_result.txt
grep "EndPoint" -r Results/ > hidden_EndPoint_result.txt
cp hidden_EndPoint_result.txt Results/
rm hidden_EndPoint_result.txt
grep "bucket" -r Results/ > hidden_bucket_result.txt
cp hidden_bucket_result.txt Results/
rm hidden_bucket_result.txt
grep "storage" -r Results/ > hidden_storage_result.txt
cp hidden_storage_result.txt Results/
rm hidden_storage_result.txt
grep "http://" -r Results/ > hidden_http_result.txt
cp hidden_http_result.txt Results/
rm hidden_http_result.txt
grep "https://" -r Results/ > hidden_https_result.txt
cp hidden_https_result.txt Results/
rm hidden_https_result.txt
echo "[HINT] Check /res/values and /res/xml folder, if exists!"
echo "";
