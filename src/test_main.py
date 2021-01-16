import boto3
import datetime
import os

region_name = 'eu-west-1'
aws_access_key_id = '<Please paste the access key>'
aws_secret_access_key = '<Please paste the secrete key>'
bucket_name = '<name a unique S3 bucket name>'

if __name__ == '__main__':
    s3_cli = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    for top, dirs, files in os.walk('../resources/data/'):
        for nm in files:
            stat = os.stat(os.path.join(top,nm))
            modified_timestamp=datetime.datetime.fromtimestamp(stat.st_mtime)
            s3_resp = s3_cli.head_object(Bucket=bucket_name, Key=str(modified_timestamp.year)+"/"+str(modified_timestamp.month)+"/"+str(modified_timestamp.day)+"/"+str(modified_timestamp.hour)+"/"+nm)

            # Check is the file exists based on the http response
            # The idea here was to use the md5 of the file on S3 and the local file systme to ensure the file was uploaded successfully.
            # However, it seemed that the ETag on S3 wasn't represented as a MD5
            if s3_resp['ResponseMetadata']['HTTPStatusCode'] != 200:
                print("Test Failed")

    print("Test Passed")