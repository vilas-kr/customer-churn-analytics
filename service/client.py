import boto3

class Client:
    s3_client = None
    redshift_data_client = None

    @staticmethod
    def get_s3_client():
        if Client.s3_client:
            return Client.s3_client
        
        Client.s3_client = boto3.client('s3')
        return Client.s3_client

    @staticmethod
    def get_redshift_client():
        if Client.redshift_data_client:
            return Client.redshift_data_client
        
        Client.redshift_data_client = boto3.client('redshift-data')
        return Client.redshift_data_client