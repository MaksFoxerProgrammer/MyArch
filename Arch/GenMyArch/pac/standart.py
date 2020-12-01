import os
from pac import fun

def standart():

    os.system('lsblk')

    root = input("Введите раздел для root (ошибки быть не должно, не предусмотрено!): ")
    boot = input("Введите раздел для boot (ошибки быть не должно, не предусмотрено!): ")
    sd = input("Введите раздел для grub (ошибки быть не должно, не предусмотрено!): ")
    user = input("Введите имя пользователя (ошибки быть не должно, не предусмотрено!): ")

    os.system('mkfs.ext4 /dev/' + root + ' -L root')
    os.system('mount /dev/' + root + ' /mnt')

    if (boot != '0'):
        os.system('mkfs.ext2  /dev/' + boot + ' -L boot')
        os.system('mkdir /mnt/boot')
        os.system('mount /dev/' + boot + ' /mnt/boot')

    os.system('pacstrap /mnt base linux linux-headers dhcpcd which netctl inetutils  base-devel  wget linux-firmware nano wpa_supplicant dialog')

    os.system('genfstab -pU /mnt >> /mnt/etc/fstab')

    """
        Приводим /etc/mkinitcpio.conf (/mnt/etc/mkinitcpio.conf) новой системы к сл. содержанию. Находим параметры HOOKS и убираем autodetect (необходимо, чтобы загрузочный образ не был привязан к железкам, на которых производится сборка). Остальное меняем на свой лад.

            HOOKS="base udev modconf block filesystems keyboard fsck"
            ...
            COMPRESSION="xz"

        Также чтобы на флешку записывалось меньше данных, можно монтировать /var/tmp и /var/log в оперативную память. Для этого добавляем в fstab строки:

            tmpfs /tmp   tmpfs   nodev,nosuid   0   0
            tmpfs /var/tmp tmpfs defaults 0 0
            tmpfs /var/log tmpfs defaults 0 0
    """

    os.system('arch-chroot /mnt')
    """Судя по всему все остальное
    в отдельный файл, который скопировать
    и запустить в arch-xhroot..."""

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

    os.system('pacman -S  ttf-arphic-ukai git ttf-liberation ttf-dejavu ttf-arphic-uming ttf-fireflysung ttf-sazanami --noconfirm')

    os.system('pacman -S firefox firefox-i18n-ru --noconfirm ')

    os.system('pacman -S chromium --noconfirm')

    os.system('pacman -S libreoffice-still libreoffice-still-ru --noconfirm')

    os.system('pacman -S openssh --noconfirm')

    os.system('pacman -Sy --noconfirm')

    os.system('sudo pacman -S --needed base-devel git wget yajl')

    os.system('curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg')
    os.system('    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf')
    os.system('sudo pacman -Syu sublime-text')

    # os.system('')
 


    os.system('passwd')
    os.system('passwd' + user)
