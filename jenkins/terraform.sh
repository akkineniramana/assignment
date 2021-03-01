#!/bin/sh

ACTION = $1

if [ "$ACTION" = "create" ] 
then
  terraform init
  terraform plan
  terraform apply --auto-approve
elif [ "$ACTION" = "delete" ]
then
  terraform destroy --auto-approve
fi
