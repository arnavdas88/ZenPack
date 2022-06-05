import os, sys

def installA():
    '''
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
    echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-vs.list
    sudo apt update
    sudo apt -y install build-essential gcc g++ make cmake libelf-dev llvm clang libxml2 libxml2-dev libzstd1 git libgtest-dev apt-transport-https dirmngr monodevelop googletest google-mock libgmock-dev libjson-glib-dev
    '''
    pass

def installB():
    '''
    git clone --recurse-submodules https://github.com/Sysinternals/SysmonForLinux.git
    cd SysmonForLinux
    mkdir build
    cd build
    cmake ..
    make
    '''
    pass