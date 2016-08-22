Log-bilinear-language-models
============================
lbl: the original version <br>
hlbl: a hierachical version with huffman tree <br>
lbl_mp: lbl with multiprocessing and cythonised training  <br>
setup: used to compile the extension module <br>

Installation
============================
  1. Clone the repository <br>
  ```
  git clone https://github.com/aanodin/Log-bilinear-language-models
  ```
  
  2. Install Python 2.7 and dependencies <br>
  ```
  sudo aptitude install libatlas-base-dev gfortran python python-dev build-essential g++
  ```
  
  3. Install Python modules <br>
  ```
  sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
  sudo /sbin/mkswap /var/swap.1
  sudo /sbin/swapon /var/swap.1
  sudo pip install numpy
  sudo pip install scipy
  sudo pip install cython
  sudo pip install argparse
  sudo swapoff /var/swap.1
  sudo rm /var/swap.1
  ```
  
  3. Installing the tool from repository<br>
  ```
  cd Log-bilinear-language-models
  python setup.py install
  ```

Usage
============================
  1. Train the model:<br>
  ```
  python main.py --train input.txt --save-net network.hdf5
  ```
  2. Evaluate other (or the same :)) file:<br>
  ```
  python main.py --ppl input.txt --net network.hdf5
  ```
  3. Evaluate using ARPA language model:<br>
  ```
  python main.py --ppl input.txt --net network.hdf5 --arpa ClarinLM.lm.1 0.2
  ```
  4. Evaluate using ARPA language model and save new model:<br>
  ```
  python main.py --ppl input.txt --net network.hdf5 --arpa ClarinLM.lm.1 0.2 --save-lm newClarinLM.lm.1
  ```

