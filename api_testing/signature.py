import datetime


def generate():
    """
    1. Retrieve Timestamp from HTTP Header (X-BCA-Timestamp)
    2. Retrieve the API Key form HTTP Header (X-BCA-Key)
    3. Lookup the API Secret corresponding to the received key in internal store
    4. Retrieve client HMAC from HTTP Header lowercase hexadecimal format (X-BCA-Signature)
    5. Calculate HMAC using the API Secret as the HMAC secret key
    6. Compare client HMAC with calculated HMAC
    """

    X_BCA_Timestamp = datetime.datetime.now()
    X_BCA_Key = '41138489-1057-4e7e-ab93-9bc97b511cf6'
    api_secret = '22a2d25e-765d-41e1-8d29-da68dcb5698b'

