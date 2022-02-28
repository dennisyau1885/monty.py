YML   = $(wildcard *.yml)
STACK = $(YML:%.yml=%)
FILE  = file://$(shell pwd)/$(YML)

all: list endpoints test

list:
	@aws cloudformation list-stacks \
	| jq -c \
	'.StackSummaries[:1][]|{StackName,StackStatus,CreationTime}'

create:
	@aws cloudformation create-stack \
	--capabilities CAPABILITY_NAMED_IAM \
	--stack-name ${STACK} \
	--template-body ${FILE}

update:
	@aws cloudformation update-stack \
	--capabilities CAPABILITY_NAMED_IAM \
	--stack-name ${STACK} \
	--template-body ${FILE}

delete:
	@aws cloudformation delete-stack --stack-name ${STACK}

endpoints:
	@aws apigatewayv2 get-apis \
	| jq -c '.Items[]|{Name,ApiEndpoint}'

# Note $\ as continuation and $ to escape $NAME
test:
	$(eval ENDPOINT=$(shell aws apigatewayv2 get-apis $\
	| jq -r --arg NAME ${STACK} $\
		'.Items[]|select (.Name == $$NAME )|.ApiEndpoint'))
	curl ${ENDPOINT}

events:
	@aws cloudformation describe-stack-events \
	--stack-name ${STACK} \
	| jq '.StackEvents |sort_by(.Timestamp) |.[] '
