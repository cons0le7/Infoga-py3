echo Installing Python2… 
apk add python2 
echo Downloading Python2 pip…
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
echo Installing Python2 pip… 
python2 get-pip.py
echo Installing dependencies…
pip install requests 
echo Installation complete. 