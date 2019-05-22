print("Cloning github directory")
!pwd
!git clone https://github.com/fastai/fastbook.git
%cd fastbook
%pip install -r requirements.txt
!python3 -m pip install --upgrade Pillow

print("Setup Colab..")

!curl -s https://course.fast.ai/setup/colab | bash
