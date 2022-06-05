import os, sys

import warnings

def installA():

    # Add Key
    os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF")

    # Add Source
    os.system('echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-vs.list')

    # Update
    os.system('sudo apt update')

    # Install Dependencies
    os.system('sudo apt -y install build-essential gcc g++ make cmake libelf-dev llvm clang libxml2 libxml2-dev libzstd1 git libgtest-dev apt-transport-https dirmngr monodevelop googletest google-mock libgmock-dev libjson-glib-dev')

    # Install eBPF BCC
    os.system('sudo apt-get install bpfcc-tools linux-headers-$(uname -r) -y')

    return True

def installB():
    if not os.path.exists("/opt/sysinternalsEBPF"):
        os.system("cd")
        os.system("git clone https://github.com/Sysinternals/SysinternalsEBPF.git")
        os.system("cd SysinternalsEBPF && mkdir build")
        os.system("cd SysinternalsEBPF/build && cmake ..")
        os.system("cd SysinternalsEBPF/build && make")
        # os.system("cd SysinternalsEBPF/build && sudo make install")
        # os.system("cp -r SysinternalsEBPF /opt/sysinternalsEBPF")
        os.system("cd SysinternalsEBPF/build && sudo ./libsysinternalsEBPFinstaller")

    else:
        warnings.warn("[ SKPPING ] SysinternalsEBPF already exists in `opt`")

    return True

def installC():
    os.system("git clone --recurse-submodules https://github.com/Sysinternals/SysmonForLinux.git")
    os.system("cd SysmonForLinux && mkdir build")
    os.system("cd SysmonForLinux/build && cmake ..")
    os.system("cd SysmonForLinux/build && make")

    return True