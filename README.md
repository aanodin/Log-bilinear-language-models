Log-bilinear-language-models
============================
lbl: the original version <br>
hlbl: a hierachical version with huffman tree <br>
lbl_mp: lbl with multiprocessing and cythonised training  <br>
setup: used to compile the extension module <br>

Installation
============================
1. Clone the repository
git clone https://github.com/aanodin/Log-bilinear-language-models

2. Install Python 2.7 and dependencies
sudo aptitude install libatlas-base-dev gfortran python python-dev build-essential g++

sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
sudo /sbin/mkswap /var/swap.1
sudo /sbin/swapon /var/swap.1

sudo pip install numpy
sudo pip install scipy
pip install cython

sudo swapoff /var/swap.1
sudo rm /var/swap.1

3. Installing the tool from repository
cd Log-bilinear-language-models
python setup.py install


