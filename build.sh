#!/usr/bin/env bash

SOURCE=${SOURCE:-~/monty.py/python}
BUILD=${BUILD:-~/monty.py/build}
TARGET=${TARGET:-spam_lambda.zip}
S3BUCKET=${S3BUCKET:-s3://dyau-lambda-artifacts}

cd $SOURCE
zip $BUILD/$TARGET *.py
zip -T $BUILD/$TARGET
aws s3 cp $BUILD/$TARGET $S3BUCKET/ || echo "FAILED: aws s3 cp $BUILD/$TARGET $S3BUCKET/"
