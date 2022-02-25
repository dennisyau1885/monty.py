#!/usr/bin/env bash

set -o pipefail

mapfile -t ak < <( \
  aws iam create-access-key --user-name github-actions-monty \
  | jq -r '.AccessKey | .AccessKeyId, .SecretAccessKey' \
)

if [[ ${#ak[@]} ]]; then
  echo "aws iam list-access-keys --user github-actions-monty"
  echo "aws iam delete-access-key --user-name github-actions-monty --access-key-id \$access_key_id_to_delete"
  exit 1
fi

gh secret set AWS_ACCESS_KEY_ID --body "${ak[0]}"
gh secret set AWS_SECRET_ACCESS_KEY --body "${ak[1]}"
gh secret set AWS_REGION --body "eu-west-2"
