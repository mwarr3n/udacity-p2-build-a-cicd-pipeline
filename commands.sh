
cd ~

git clone git@github.com:mwarr3n/udacity-p2-build-a-cicd-pipeline.git

cd udacity-p2-build-a-cicd-pipeline

make setup

source ~/.udacity-devops/bin/activate

make all

az webapp up -n udacity-project2-wa -g udacity-project2-rg --sku F1
