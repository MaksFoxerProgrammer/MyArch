import os

os.system('pacman -S grub   --noconfirm')
os.system('grub-install /dev/' + sd)
os.system('grub-mkconfig -o /boot/grub/grub.cfg')

os.system('timedatectl set-ntp true')
os.system('echo Arch > /etc/hostname')
os.system('ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime')

os.system('echo "en_US.UTF-8 UTF-8" > /etc/locale.gen')
os.system('echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen')
os.system('locale-gen')
os.system('echo \'LANG="ru_RU.UTF-8"\' > /etc/locale.conf')
os.system('echo "KEYMAP=ru" >> /etc/vconsole.conf')
os.system('echo "FONT=cyr-sun16" >> /etc/vconsole.conf')

os.system('useradd -m -g users -G wheel -s /bin/bash ' + user)

os.system('echo \'%wheel ALL=(ALL) NOPASSWD: ALL\' >> /etc/sudoers')

os.system('echo \'[multilib]\' >> /etc/pacman.conf')
os.system('echo \'Include = /etc/pacman.d/mirrorlist\' >> /etc/pacman.conf')

os.system('pacman -Sy xorg-server xorg-drivers --noconfirm')

os.system('pacman -Syy')
os.system('pacman -S gnome gnome-extra  --noconfirm')
os.system('pacman -S i3 i3-wm i3status  dmenu  --noconfirm')
os.system('pacman -Sy nitrogen  --noconfirm')
os.system('pacman -S gdm --noconfirm')
os.system('systemctl enable gdm.service -f')

os.system('pacman -Sy networkmanager networkmanager-openvpn network-manager-applet ppp --noconfirm')
os.system('systemctl enable NetworkManager.service')

os.system('systemctl enable dhcpcd.service')

os.system('pacman -Sy pulseaudio-bluetooth alsa-utils pulseaudio-equalizer-ladspa   --noconfirm')
os.system('systemctl enable bluetooth.service')

os.system('pacman -Sy exfat-utils ntfs-3g   --noconfirm')

os.system('pacman -Sy unzip unrar lha file-roller p7zip unace lrzip  --noconfirm')

os.system('pacman -S gvfs-afc gvfs-mtp --noconfirm')

os.system('pacman -S blueman --noconfirm')

os.system('pacman -S htop xterm --noconfirm')

os.system('pacman -S filezilla --noconfirm')

os.system('pacman -S neofetch  --noconfirm')

os.system('pacman -S vlc  --noconfirm')

os.system('pacman -S gparted  --noconfirm')

os.system('pacman -S telegram-desktop   --noconfirm')

os.system('pacman -S spectacle flameshot --noconfirm')

os.system(
    'pacman -S  ttf-arphic-ukai git ttf-liberation ttf-dejavu ttf-arphic-uming ttf-fireflysung ttf-sazanami --noconfirm')

os.system('pacman -S firefox firefox-i18n-ru --noconfirm ')

os.system('pacman -S chromium --noconfirm')

os.system('pacman -S libreoffice-still libreoffice-still-ru --noconfirm')

os.system('pacman -S openssh --noconfirm')

os.system('pacman -Sy --noconfirm')

os.system('sudo pacman -S --needed base-devel git wget yajl')

os.system(
    'curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg')
os.system(
    '    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf')
os.system('sudo pacman -Syu sublime-text')

# os.system('')


os.system('passwd')
os.system('passwd' + user)