Architecture / Design Consideration
------------------------------------------------------------------
I considered AWS S3 as a data lake based on the comments on the test description about using redshift as a DWH. Once the files are on S3, they can be copied into redshift

#

Project Structure
-
SQL directory
--
task-1.sql - Contains the SQL for Task 1
task-2.sql - Contains the SQL for Task 2

resources/data/
--
This directory contains the data for google trends. The thought process here is that the files would arrive here on an hourly basis and would get processed.

src
--
main.py - contains the main python script to upload files into the AWS S3 data lake

test_main.py - this script would test the S3 bucket and the local file system to ensure the files have been uploaded into the data lake
#
Configuration
-
On both the main.py and the test_main.py, please input correct values into these variables before testing these scripts

aws_access_key_id
aws_secret_access_key
bucket_name --> this must be unique

Again, the idea is to use these either automatically configure using 'aws configure' or as in my case I was using environment variables for these parameters

#
Running the code
-
If an IDE like Anaconda or PyCharm is used, the code can be run on them. Please ensure the package for AWS 'boto3' is imported before the run
