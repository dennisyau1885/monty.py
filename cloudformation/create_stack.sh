aws cloudformation create-stack \
  --capabilities CAPABILITY_NAMED_IAM \
  --stack-name lambda01 \
  --template-body file://$(pwd)/lambda.cf.yml
