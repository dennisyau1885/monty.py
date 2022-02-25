aws cloudformation list-stacks | jq -c '.StackSummaries[]|{N:.StackName, S:.StackStatus}'
