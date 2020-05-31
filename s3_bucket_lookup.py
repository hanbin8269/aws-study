import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# ================ 버킷 이름 조회 =========

response = s3.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]

print('Bucket List : %s'% buckets)

# =========================================

