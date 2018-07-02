# detectron-results-visualization


## Steps

 - train your dataset with saving log : `python2 tools/train_net.py --cfg configs/XXX.yaml | tee ./trainingoutput.txt`   
 
 -  : run `pip install fire matplotlib` to install the requirements 
 - copy the file named `visualization.py` to you `detectron/tools` path
 - cd path `detectron/tools` and run command `python visualization.py ../trainingoutput.txt`
