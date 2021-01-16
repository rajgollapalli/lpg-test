import boto3
import os
import datetime
import time

region_name = 'eu-west-1'
aws_access_key_id = '<Please paste the access key>'
aws_secret_access_key = '<Please paste the secrete key>'
bucket_name = '<name a unique S3 bucket name>'

def s3_create_bucket(bucket_name):
    check_bucket = s3.Bucket(bucket_name)

    if check_bucket.creation_date:
        print("The bucket exists")
    else:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
            'LocationConstraint': region_name})


def s3_upload_file(bucket_name, file_name):
    content = "String content to write to a new S3 file"
    s3.Object(bucket_name, file_name).put(Body=content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s3 = boto3.resource(
        's3',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    ## Create a bucket
    s3_create_bucket(bucket_name)

    past = time.time() - 1 * 60 * 60  # 1 hour

    ## Loop through all files in the directory and upload files into the S3 bucket
    ## Prefix the path by the dyear month day and hour of the file creation
    for top, dirs, files in os.walk('resources/data/'):
        for nm in files:
            stat = os.stat(os.path.join(top,nm))
            modified_timestamp=datetime.datetime.fromtimestamp(stat.st_mtime)

            # Pick files modified in the last hour only
            if stat.st_mtime >= past:
                print(os.path.join(top,nm))
                s3_upload_file(bucket_name,str(modified_timestamp.year)+"/"+str(modified_timestamp.month)+"/"+str(modified_timestamp.day)+"/"+str(modified_timestamp.hour)+"/"+nm)