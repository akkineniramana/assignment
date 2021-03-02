# Assignment

##### sample flask app which will connect to mysql database to fetch the user. It has only one route which will show hello user: username(from database)

#### To test the app Locally, run below commands
```bash
docker-compose up 
## try localhost:5000 in the browser

## to deploy in minikube kubernetes cluster
minikube start --kubernetes-version v1.19.0
kubectl apply -f kube-manifest

## after sometime check the status of deployments using below command
kubectl get all

# if everything is fine then run below command
minikube service api-service

```

#### I have used terraform to create the kubernetes cluster in AWS

```bash 
aws configure
# provide aws secret key, access key and region

cd terraform
terraform init
terraform plan
terraform apply --auto-approve

```

#### terraform apply will take 10 to 15min to spin eks cluster in AWS

- After the cluster creation is done, kubeconfig_my-cluster file will be created in terraform folder. This will be used to connect to eks cluster using kubectl

```bash
export KUBECONFIG="${PWD}/kubeconfig_my-cluster"
kubectl get nodes

```

#### Deploy helloworld app  in eks cluster

```bash 
cd ..

kubectl apply -f kube-manifest

kubectl get all ## to see all pods and svc running fine or not

```

#### once everything is running fine run below command to get loadbalancer url
```bash
kubectl get svc

# from the above command output take api-service external-ip and  paste in the browser with port 5000
# examle : http://external-ip:5000/  => this will show sample hello world data which will fetch user from database
```

#### After testing, delete the cluster using below commands
```bash
cd terraform
terraform destroy --auto-approve
```

#### created Jenkins pipeline to create and destroy the cluster, respective declarative jenkins file is in jenkins folder(Asuming terraform is installed on jenkins node or docker node and configuring AWS credentials as env variables)
