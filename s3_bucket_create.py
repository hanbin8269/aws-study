import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# create_bucket()을 통해 버킷 생성
s3.create_bucket(
    Bucket='shem4321', 
    CreateBucketConfiguration = {'LocationConstraint' : 'ap-northeast-2'})