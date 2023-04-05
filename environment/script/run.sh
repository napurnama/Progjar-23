sudo chmod -R a+rwx /home/jovyan
sudo apt-get update
sudo apt-get install apache2-utils
# start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''  --NotebookApp.ip='0.0.0.0' --Notebook.autoreload=True --NotebookApp.notebook_dir=/home/jovyan/work --allow-root
start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''  --NotebookApp.ip='0.0.0.0' --Notebook.autoreload=True --NotebookApp.notebook_dir=/home/jovyan/work
