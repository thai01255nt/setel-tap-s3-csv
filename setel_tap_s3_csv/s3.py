from tap_s3_csv.s3 import *


@retry_pattern()
def get_file_handle_custom(config: Dict, s3_path: str) -> Iterator:
    """
    Get a iterator of file located in the s3 path
    :param config: tap config
    :param s3_path: file path in S3
    :return: file Body iterator
    """
    bucket = config['bucket']
    aws_endpoint_url = config.get('aws_endpoint_url')

    # override default endpoint for non aws s3 services
    if aws_endpoint_url is not None:
        s3_resource = boto3.resource('s3', endpoint_url=aws_endpoint_url)
        s3_client = boto3.client('s3', endpoint_url=aws_endpoint_url)
    else:
        s3_resource = boto3.resource('s3')
        s3_client = boto3.client('s3')

    s3_bucket = s3_resource.Bucket(bucket)
    s3_object = s3_bucket.Object(s3_path)
    tags = s3_client.get_object_tagging(
        Bucket=bucket,
        Key=s3_path
    )
    return s3_object.get()['Body'], tags.get('TagSet', [])
