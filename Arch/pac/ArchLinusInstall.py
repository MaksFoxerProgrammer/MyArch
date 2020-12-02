import os
class ArchLinuxInstall(object):
    """
    Итоговый, единственный класс, устанавливающий Арч!
    """
    root = ''
    boot = '0'
    home = '0'
    sd = ''
    user = ''
    comp = ''


    def hi(self):
        print('\n\n\tДобро пожаловать в скрипт установки Arch Linux!!!')
        os.system('lsblk')
        input('\n\tНажмите Enter для продолжения...')



    def DiskLayout(self):
        os.system('clear')
        os.system('lsblk')
        sd = input('\n\tВыберете диск для разметки (например, sda): ')

        os.system('sudo cfdisk /dev/' + sd)
        os.system('clear')
        print('\tВаша разметка дисков:')
        os.system('lsblk /dev/' + sd)

        print('\n')

        self.root = input("Введите раздел для ROOT (ошибки быть не должно, не предусмотрено!): ")
        self.boot = input("Введите раздел для BOOT (ошибки быть не должно, не предусмотрено!)(0 для пропуска): ")
        self.home = input("Введите раздел для HOME (ошибки быть не должно, не предусмотрено!)(0 для пропуска): ")

        os.system('mkfs.ext4 /dev/' + self.root + ' -L root')
        os.system('mount /dev/' + self.root + ' /mnt')

        if (self.boot != '0'):
            os.system('mkfs.ext2  /dev/' + self.boot + ' -L boot')
            os.system('mkdir /mnt/boot')
            os.system('mount /dev/' + self.boot + ' /mnt/boot')
        else:
            print('\tboot пропущен\n\n')

        if (self.home != '0'):
            os.system('mkfs.ext2  /dev/' + self.home + ' -L home')
            os.system('mkdir /mnt/home')
            os.system('mount /dev/' + self.home + ' /mnt/home')
        else:
            print('\thome пропущен\n\n')

        print('\n\tВаша разметка дисков:')
        os.system('lsblk /dev/' + sd)
        input('\n\n\tНажимте Enter для продолжения...')



    def Base(self):
        os.system('clear')
        print('\tБазовая установка окружения\n\n')
        os.system('''
        pacstrap /mnt python3 git base linux linux-headers dhcpcd which netctl inetutils  base-devel  wget linux-firmware nano wpa_supplicant dialog
        genfstab -pU /mnt >> /mnt/etc/fstab''')

        print("""
            Приводим /etc/mkinitcpio.conf (/mnt/etc/mkinitcpio.conf) новой системы к сл. содержанию. Находим параметры HOOKS и убираем autodetect (необходимо, чтобы загрузочный образ не был привязан к железкам, на которых производится сборка). Остальное меняем на свой лад.

                HOOKS="base udev modconf block filesystems keyboard fsck"
                ...
                COMPRESSION="xz"

            Также чтобы на флешку записывалось меньше данных, можно монтировать /var/tmp и /var/log в оперативную память. Для этого добавляем в fstab строки:

                tmpfs /tmp   tmpfs   nodev,nosuid   0   0
                tmpfs /var/tmp tmpfs defaults 0 0
                tmpfs /var/log tmpfs defaults 0 0
            
            =============================================================================

            После остановки, выполнить 2-ю часть!
            git clone https://github.com/MaksFoxerProgrammer/MyArch.git && cd MyArch && sudo python3 Arch/pac/ArchLinusInstall.py
            Выбираем ВТОРОЙ пункт меню !
        """)

        os.system('arch-chroot /mnt')


    
    def install1(self):
        self.hi()
        self.DiskLayout()
        self.Base()



    def hi2(self):
        os.system('clear')
        print('''
        Добро пожаловать во вторую часть установки!
        Тут мы доставим остальные компоненты системы, и настроим их!\n\n
        ''')
        os.system('lsblk')
        self.sd = input("Введите раздел для grub (ошибки быть не должно, не предусмотрено!): ")
        self.user = input("Введите имя пользователя (ошибки быть не должно, не предусмотрено!): ")
        self.comp = input("Введите имя компьютера (ошибки быть не должно, не предусмотрено!): ")



    def users(self):
        os.system('clear')
        print('\tНастроим пользователя...\n\n')
        os.system('useradd -m -g users -G wheel -s /bin/bash ' + self.user)

        print('\tНастроим пароль ' + self.user + ': ')
        os.system('passwd ' + self.user)

        print('\n\n\tНастроим пароль админа: ')
        os.system('passwd')
        
        os.system('echo \'%wheel ALL=(ALL) NOPASSWD: ALL\' >> /etc/sudoers')



    def grub(self):
        os.system('clear')
        print('\tСтавим загрузчик...\n\n')
        os.system('pacman -S grub   --noconfirm')
        os.system('grub-install /dev/' + self.sd)
        os.system('grub-mkconfig -o /boot/grub/grub.cfg')

        print('\n\n\tСтавим xorg...\n\n')
        os.system('pacman -Sy xorg-server xorg-drivers --noconfirm')



    def network(self):
        os.system('clear')
        print('\tСтавим сеть...\n\n')
        os.system('pacman -Sy networkmanager networkmanager-openvpn network-manager-applet ppp dialog wpa_supplicant --noconfirm')
        os.system('systemctl enable NetworkManager.service')
        os.system('systemctl enable dhcpcd.service')



    def time(self):
        os.system('clear')
        print('\tСтавим время и имя компьютера...\n\n')
        os.system('timedatectl set-ntp true')
        os.system('echo ' + self.comp + ' > /etc/hostname')
        os.system('ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime')



    def language(self):
        os.system('clear')
        print('\tСтавим язык системы...\n\n')
        os.system('echo "en_US.UTF-8 UTF-8" > /etc/locale.gen')
        os.system('echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen')
        os.system('locale-gen')
        os.system('echo \'LANG="ru_RU.UTF-8"\' > /etc/locale.conf')
        os.system('echo "KEYMAP=ru" >> /etc/vconsole.conf')
        os.system('echo "FONT=cyr-sun16" >> /etc/vconsole.conf')



    def repos(self):
        os.system('clear')
        print('\tДобавляем необходимые репозитории...\n\n')
        os.system('echo \'[multilib]\' >> /etc/pacman.conf')
        os.system('echo \'Include = /etc/pacman.d/mirrorlist\' >> /etc/pacman.conf')


    def fonts(self):
        os.system('clear')
        print('\tСтавим шрифты...\n\n')
        os.system('pacman -S  ttf-arphic-ukai git ttf-liberation ttf-dejavu ttf-arphic-uming ttf-fireflysung ttf-sazanami --noconfirm')



    def aur(self):
        os.system('clear')
        os.system('mkdir ~/downloads')
        os.system('cd ~/downloads')
        print('\tУстановка AUR (yay)\n\n')
        os.system('sudo pacman -Syu')
        os.system('sudo pacman -S wget --noconfirm')
        os.system('wget git.io/yay-install.sh && sh yay-install.sh --noconfirm')
        # os.system('')



    def graphicalEnvironment(self):
        os.system('clear')
        # print('\n\nСтавим Gnome...')
        # os.system('pacman -Syy')
        # os.system('pacman -S gnome gnome-extra  --noconfirm')
        os.system('cd ~/downloads')

        print('\n\tСтавим XFCE...\n\n')
        os.system('pacman -S xfce4 xfce4-goodies --noconfirm')

        print('\n\tСтавим i3...\n\n')
        os.system('pacman -S i3 i3-wm i3status  dmenu  --noconfirm')
        os.system('pacman -Sy nitrogen  --noconfirm')

        print('\n\tСтавим gdm...\n\n')
        os.system('pacman -S gdm --noconfirm')
        os.system('systemctl enable gdm.service -f')
        """
        echo 'Cтавим DM'
        pacman -S lxdm --noconfirm
        systemctl enable lxdm
        """

        v = input('Ставим xfce с настройками? (1 - да, остальное - нет): ')
        if v=='1':
            print('Качаем и устанавливаем настройки Xfce')
            # Чтобы сделать копию ваших настоек перейдите в домашнюю директорию ~/username 
            # открйте в этой категории терминал и выполните команду ниже
            # Предварительно можно очистить конфиг от всего лишнего
            # tar -czf config.tar.gz .config
            # Выгрузите архив в интернет и скорректируйте ссылку на свою.
            # wget https://github.com/ordanax/arch/raw/master/attach/config.tar.gz
            os.system('wget https://github.com/MaksFoxerProgrammer/MyArch/raw/main/attach/config.tar.gz')
            os.system('sudo rm -rf ~/.config/xfce4/*')
            os.system('sudo tar -xzf config.tar.gz -C ~/')
            print('\n\tУдаление тем по умолчанию')
            os.system('sudo rm -rf /usr/share/themes/*')
            print('\n\tУстановка тем')
            os.system('yay -S x-arc-shadow papirus-maia-icon-theme-git breeze-default-cursor-theme --noconfirm')
            os.system('sudo pacman -S capitaine-cursors --noconfirm')
            print('\n\tСтавим лого ArchLinux в меню')
            os.system('wget https://github.com/MaksFoxerProgrammer/MyArch/raw/main/attach/archlinux_logo.png')
            os.system('sudo mv -f ~/downloads/arch_logo.png /usr/share/pixmaps/arch_logo.png')
            print('\n\tУдаляем лишнее из xfce4')
            os.system('sudo pacman -Rs xfburn orage parole mousepad xfce4-appfinder xfce4-clipman-plugin xfce4-timer-plugin xfce4-time-out-plugin xfce4-artwork xfce4-taskmanager xfce4-smartbookmark-plugin xfce4-sensors-plugin xfce4-screenshooter xfce4-notes-plugin xfce4-netload-plugin xfce4-mpc-plugin xfce4-mount-plugin xfce4-mailwatch-plugin xfce4-genmon-plugin xfce4-fsguard-plugin xfce4-eyes-plugin xfce4-diskperf-plugin xfce4-dict xfce4-cpugraph-plugin xfce4-cpufreq-plugin')
            print('\n\tСтавим обои на рабочий стол')
            os.system('wget https://github.com/MaksFoxerProgrammer/MyArch/raw/main/attach/bg.jpg')
            os.system('sudo rm -rf /usr/share/backgrounds/xfce/*')#Удаляем стандартные обои
            os.system('sudo mv -f ~/downloads/bg.jpg /usr/share/backgrounds/xfce/bg.jpg')
            # os.system('')

        v = input('Ставим i3 с настройками? (1 - да, остальное - нет): ')
        if v=='1':
            os.system('pacman -S pacman -S i3-wm polybar dmenu pcmanfm ttf-font-awesome feh gvfs udiskie xorg-xbacklight ristretto tumbler compton jq --noconfirm')
            os.system('yay -S polybar ttf-weather-icons ttf-clear-sans')
            os.system('wget https://github.com/MaksFoxerProgrammer/MyArch/raw/main/attach/config_i3wm.tar.gz')
            os.system('sudo rm -rf ~/.config/i3/*')
            os.system('sudo rm -rf ~/.config/polybar/*')
            os.system('sudo tar -xzf config_i3wm.tar.gz -C ~/')
            # os.system('')



    def mainPrograms(self):
        os.system('clear')
        print('\tСтавим основные приложения...\n\n')
        os.system('pacman -Sy pulseaudio-bluetooth alsa-utils pulseaudio-equalizer-ladspa   --noconfirm')
        os.system('systemctl enable bluetooth.service')



    def utilities(self):
        os.system('clear')
        print('\tСтавим утилиты...\n\n')
        os.system('''
        pacman -Sy exfat-utils ntfs-3g   --noconfirm
        pacman -Sy exfat-utils ntfs-3g   --noconfirm
        pacman -Sy unzip unrar lha file-roller p7zip unace lrzip  --noconfirm
        pacman -S gvfs-afc gvfs-mtp --noconfirm
        pacman -S blueman --noconfirm
        pacman -S htop xterm --noconfirm
        pacman -S filezilla --noconfirm''')



    def customApplication(self):
        os.system('clear')
        print('\tСтавим пользовательские приложения...\n\n')
        os.system('pacman -S neofetch  --noconfirm')
        os.system('pacman -S vlc  --noconfirm')
        os.system('pacman -S gparted  --noconfirm')
        os.system('pacman -S telegram-desktop   --noconfirm')
        os.system('pacman -S spectacle flameshot --noconfirm')
        os.system('pacman -S firefox firefox-i18n-ru --noconfirm ')
        os.system('pacman -S chromium --noconfirm')
        os.system('pacman -S libreoffice-still libreoffice-still-ru --noconfirm')
        os.system('pacman -S openssh --noconfirm')
        os.system('pacman -Sy --noconfirm')
        os.system('sudo pacman -S --needed base-devel git wget yajl')
        os.system('curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg')
        os.system('    echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf')
        os.system('sudo pacman -Syu sublime-text --noconfirm')



    def additionalApplication(self):
        os.system('clear')
        print('\tОстальные приложения\n\n')
        os.system('''
        cd /home/''' + self.user + '''
        git clone https://aur.archlinux.org/vk-messenger.git
        chown -R ''' + self.user + ''':users /home/''' + self.user + '''/vk-messenger
        chown -R ''' + self.user + ''':users /home/''' + self.user + '''/vk-messenger/PKGBUILD 
        cd /home/''' + self.user + '''/vk-messenger  
        sudo -u ''' + self.user + '''  makepkg -si --noconfirm  
        rm -Rf /home/''' + self.user + '''/vk-messenger''')



    def gitsett(self):
        os.system('clear')  
        print('\tНастраиваем git\n\n')
        os.system('''
        git config --global user.name "maks"
        git config --global user.email "maksim.z.2000@mail.ru"

        git config --global core.autocrlf input
	    git config --global core.safecrlf warn

        git config --global core.quotepath off

        git config --global alias.co checkout
        git config --global alias.ci commit
        git config --global alias.st status
        git config --global alias.br branch
        git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
        git config --global alias.type 'cat-file -t'
        git config --global alias.dump 'cat-file -p'
        ''')     



    def install2(self):
        self.hi2()
        self.users()
        self.grub()
        self.network()
        self.time()
        self.language()
        self.repos()
        self.fonts()
        self.aur()
        self.graphicalEnvironment()
        self.mainPrograms()
        self.utilities()
        self.customApplication()
        self.additionalApplication()
        self.gitsett()



if __name__ == '__main__':
    v = input('''
    Введите вариант установки:
    1 - Установка первичной системы
    2 - Конечная установка и настройка
    Ваш выбор6: ''')

    arch = ArchLinuxInstall()

    if v=='1':
        arch.install1()
    elif v =='2':
        arch.install2()


