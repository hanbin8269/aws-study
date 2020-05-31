import boto3

s3 = boto3.client('s3')

filename = 'test_json.json'

bucket_name = 'shem1234'

# 첫번째 매개변수 : 로컬에서 올릴 파일 이름
# 두번째 매개변수 : S3 버킷 이름
# 세번째 매개변수 : 버킷에 저장될 파일 이름.

s3.upload_file(filename, bucket_name,filename)
