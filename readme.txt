INSTALL FILES ARE LOCATED IN install_files

WINDOWS: - windows_install.bat
Install process

install git for windows https://gitforwindows.org/
install python 3.9.13 https://www.python.org/downloads/release/python-3913/
install microsoft C++ build tools https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false
When installer is open, click the "C++ tools for desktop" option
Restart windows
Navigate to where you wish to store the program and open a cmd prompt
paste this command in command prompt and press enter:

 " git clone https://github.com/softwarepyrate/LPC.git && %CD%\LPC\LPC_install\windows_install.bat "

Install complete



UBUNTU 22.04 LTS: - linux_install.sh
Install process

sudo apt install git -y && sudo apt update && sudo apt upgrade -y && sudo reboot
navigate to where you want to install the program and open the terminal
git clone https://github.com/softwarepyrate/LPC.git && cd LPC
source ./LPC_install/linux_install.sh
Install complete
