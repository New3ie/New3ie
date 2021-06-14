import os 
username = 'Noo3'
password = 'root'       
# Membuat user
os.system(f'useradd -m {username}')                  
# Menambahkan user ke sudo                           
os.system(f'adduser {username} sudo')                
# Set password user ke root
os.system(f"echo '{username}:{password}' | sudo chpasswd")
# Merubah default shell dr sh ke bash                
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
print('User dibuat') 
pip install colab_ssh --upgrade &&> /dev/null
from colab_ssh import launch_ssh_cloudflared
launch_ssh_cloudflared(password=password)
