
make setup

source ~/.udacity-devops/bin/activate

make all

az webapp up -n udacity-project2-wa -g udacity-project2-rg --sku F1
