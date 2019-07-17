# s3_presigned_url

S3 署名つきURLを発行する

# Usage

あらかじめクレデンシャル情報を環境変数に埋め込んでおく。[direnv](https://github.com/direnv/direnv) の利用を推奨する。

```
export AWS_ACCESS_KEY_ID=xxxxxxxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxx
```

```
pipenv run python ./s3_presigned_url.py --bucket <YOUR BUCKET NAME> --key <YOUR KEY>
```