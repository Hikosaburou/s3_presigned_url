# -*- coding:utf-8 -*-
# !/usr/bin/env python

import boto3
import argparse


def get_presigned_url(bucket, key):
    s3 = boto3.client('s3')
    return s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=3600,
        HttpMethod='GET'
    )


def main():
    psr = argparse.ArgumentParser()
    psr.add_argument('--bucket')
    psr.add_argument('--key')
    args = psr.parse_args()

    print(get_presigned_url(args.bucket, args.key))


if __name__ == '__main__':
    main()
