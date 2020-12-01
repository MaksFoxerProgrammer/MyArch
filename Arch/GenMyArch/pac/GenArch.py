import os
from pac import fun


def GenArch():
    ####################### Начало

    os.system('clear')
    print("Продолжаем..")

    res = []
    str = ''

    # str += ("#!/bin/bash\n"
    # 	"loadkeys ru\n"
    # 	"setfont cyr-sun16\n")

    ######################## Разметка

    os.system('lsblk')

    ind = fun.inp(2, "Нужна разметка диска? \n"
                     "1 - да\n"
                     "2 - нет\n"
                     "Ваш выбор: ")
    if ind == 1:
        os.system('lsblk')
        ind2 = input("Укажите диск (sda/sdb/sdc)")
        os.system('cfdisk /dev/' + ind2)
        os.system('clear')
        os.system('lsblk')

    root = input("Укажите ROOT раздел(sda/sdb 1.2.3.4 (sda5 например)): ")
    ind2 = fun.inp(2, "Выберете ФС \n"
                      "1 - ext4\n"
                      "2 - ext2\n"
                      "Ваш выбор: ")
    if ind2 == 1:
        os.system('mkfs.ext4 /dev/' + root + ' -L root')
    elif ind2 == 2:
        os.system('mkfs.ext2 /dev/' + root + ' -L root')

    os.system('mount /dev/' + root + ' /mnt')
    os.system('clear')
    os.system('lsblk')

    ind2 = fun.inp(2, "Нужен boot раздел? \n"
                      "1 - да\n"
                      "2 - нет\n"
                      "Ваш выбор: ")
    if ind2 == 1:
        boot = input("Укажите BOOT раздел(sda/sdb 1.2.3.4 (sda7 например)): ")
        os.system('mkfs.ext2  /dev/' + boot + ' -L boot')
        os.system('mkdir /mnt/boot')
        os.system('mount /dev/' + boot + ' /mnt/boot')

    os.system('clear')


    ######################## Подготовка

    print("Данный этап поможет вам избежать проблем с ключами Pacmаn, \n"
          "если используете не свежий образ ArchLinux для установки!\n")
    ind = fun.inp(2, "Обновим ключи? \n"
                     "1 - да\n"
                     "2 - нет\n"
                     "Ваш выбор: ")
    if ind == 1:
        str += ("pacman-key --refresh-keys\n")

    os.system('clear')

    ######################## wifi модуль

    print("Если у вас есть wifi модуль и вы сейчас его не используете, то для\n"
          "исключения ошибок в работе системы рекомендую '1'")
    ind = fun.inp(2, "Установка базовой системы, будете ли вы использовать wifi?\n"
                     "1 - да\n"
                     "2 - нет\n"
                     "Ваш выбор: ")
    if ind == 1:
        str += ("pacstrap /mnt base linux linux-headers dhcpcd "
                "which netctl inetutils  base-devel  wget linux-firmware  "
                "nano wpa_supplicant dialog\n")
    else:
        str += ("pacstrap /mnt base dhcpcd linux linux-headers "
                "which netctl inetutils base-devel  wget linux-firmware  nano\n")
        str += ("genfstab -pU /mnt >> /mnt/etc/fstab\n")
    os.system('clear')

    ########################

    # print("Если вы производите установку используя Wifi тогда рекомендую  '1'\n"
    #       "если проводной интернет тогда '2' ")
    # ind = fun.inp(2, "wifi или dhcpcd?\n"
    #                  "1 - wifi\n"
    #                  "2 - dhcpcd\n"
    #                  "Ваш выбор: ")

    ######################## Куда

    ind = fun.inp(2, "Установка на флешку?\n"
                     "1 - да\n"
                     "2 - нет\n"
                     "Ваш выбор: ")

    str += ("genfstab -pU /mnt >> /mnt/etc/fstab\n")

    if ind == 1:
        flag = True
    else:
        flag = False
    os.system('clear')

    ######################## Часть вторая

    str += ("arch-chroot /mnt\n")

    str += ("timedatectl set-ntp true\n")

    hostname = input("Введите имя компьютера: ")
    username = input("Введите имя пользователя: ")

    str += "echo " + hostname + " > /etc/hostname\n"

    ######################## Настроим localtime

    print("Настроим localtime")

    ind = fun.inp(27,
                  "Укажите город(1-27) и нажмите Enter\n"
                  "1 - Калининград        14 - Красноярск\n"
                  "2 - Киев               15 - Магадан\n"
                  "3 - Киров              16 - Новокузнецк\n"
                  "4 - Минск              17 - Новосибирск\n"
                  "5 - Москва             18 - Омск\n"
                  "6 - Самара             19 - Уральск\n"
                  "7 - Саратов            20 - Алматы\n"
                  "8 - Ульяновск          21 - Среднеколымск\n"
                  "9 - Запарожье          22 - Ташкент\n"
                  "10 - Чита              23 - Тбилиси\n"
                  "11 - Иркутск           24 - Томск\n"
                  "12 - Стамбул           25 - Якутск\n"
                  "13 - Камчатка          26 - Екатеринбург\n"
                  "            27 - Ереван\n"
                  "Выбор: ")
    if ind == 1:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Kaliningrad /etc/localtime\n")
    elif ind == 2:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime\n")
    elif ind == 3:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Kirov /etc/localtime\n")
    elif ind == 4:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Minsk /etc/localtime\n")
    elif ind == 5:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime\n")
    elif ind == 6:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Samara /etc/localtime\n")
    elif ind == 7:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Saratov /etc/localtime\n")
    elif ind == 8:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Ulyanovsk /etc/localtime\n")
    elif ind == 9:
        str += ("ln -sf /usr/share/zoneinfo/Europe/Zaporozhye /etc/localtime\n")
    elif ind == 10:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Chita /etc/localtime\n")
    elif ind == 11:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Irkutsk /etc/localtime\n")
    elif ind == 12:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Istanbul /etc/localtime\n")
    elif ind == 13:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Kamchatka /etc/localtime\n")
    elif ind == 14:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Krasnoyarsk /etc/localtime\n")
    elif ind == 15:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Magadan /etc/localtime\n")
    elif ind == 16:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Novokuznetsk /etc/localtime\n")
    elif ind == 17:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime\n")
    elif ind == 18:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Omsk /etc/localtime\n")
    elif ind == 19:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Oral /etc/localtime\n")
    elif ind == 20:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Almaty /etc/localtime\n")
    elif ind == 21:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Srednekolymsk /etc/localtime\n")
    elif ind == 22:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Tashkent /etc/localtime\n")
    elif ind == 23:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Tbilisi /etc/localtime\n")
    elif ind == 24:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Tomsk /etc/localtime\n")
    elif ind == 25:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Yakutsk /etc/localtime\n")
    elif ind == 26:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Yekaterinburg /etc/localtime\n")
    elif ind == 27:
        str += ("ln -sf /usr/share/zoneinfo/Asia/Yerevan /etc/localtime\n")

    ######################## Раскладка клавиатуры

    str += ("echo \"en_US.UTF-8 UTF-8\" > /etc/locale.gen\n")
    str += ("echo \"ru_RU.UTF-8 UTF-8\" >> /etc/locale.gen\n")
    str += ("locale-gen")
    str += ("echo 'LANG=\"ru_RU.UTF-8\"' > /etc/locale.conf\n")
    str += ("echo \"KEYMAP=ru\" >> /etc/vconsole.conf\n")
    str += ("echo \"FONT=cyr-sun16\" >> /etc/vconsole.conf\n")

    ######################## Пароль

    pas = input(" Укажите пароль для ROOT: ")
    str += ("passwd\n")
    str += (pas + "\n")
    str += (pas + "\n")

    str += ("useradd -m -g users -G wheel -s /bin/bash " + username + "\n")

    MyPas = input(" Укажите пароль для " + username + ": ")
    str += ("passwd " + username)
    str += (MyPas + "\n")
    str += (MyPas + "\n")

    print("Если на компьютере/сервере будет только один ArchLinux\n"
          "и вам не нужна мультибут  >>> тогда 2\n"
          "если же установка рядом в Windows или другой OS тогда 1")

    ind = fun.inp(2, "Нужен мультибут (установка рядом с другой OS)?\n"
                     "1 - да\n"
                     "2 - нет")

    if ind == 2:
        str += ("pacman -S grub   --noconfirm\n")
    elif ind == 1:
        str += ("pacman -S grub grub-customizer os-prober  --noconfirm\n")

    str += ("lsblk -f\n")
    boot = input("Укажите диск куда установить GRUB (sda/sdb): ")
    str += ("grub-install /dev/" + boot + "\n")
    str += ("grub-mkconfig -o /boot/grub/grub.cfg\n")
    str += ("mkinitcpio -p linux\n")

    ######################## sudo

    ind = fun.inp(3, "Настроим Sudo?\n"
                     "1 - с паролем\n"
                     "2 - без пароля\n"
                     "3 - Sudo не добавляем\n"
                     "Ваш выбор: ")

    if ind == 1:
        str += ("echo '%wheel ALL=(ALL) ALL' >> /etc/sudoers")
    elif ind == 2:
        str += ("echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers")

    ######################## multilib

    ind = fun.inp(2, "Настроим multilib? (32 in 64)\n"
                     "1 - да \n"
                     "2 - нет \n"
                     "Выбор: ")

    if ind == 1:
        str += ("echo '[multilib]' >> /etc/pacman.conf\n")
        str += ("echo 'Include = /etc/pacman.d/mirrorlist' >> /etc/pacman.conf\n")

    ######################## x-сервер

    ind = fun.inp(2, "Если вам не нужен X-сервер, тогда выбирайте пункт '2'\n"
                     "Установка производиться на vds или на ПК?\n"
                     "1 - ПК\n"
                     "2 - vds\n"
                     "Выбор: ")

    if ind == 1:
        ind2 = fun.inp(2, "Устанавливаем на виртуальную машину?\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 2:
            str += ("pacman -Sy xorg-server xorg-drivers --noconfirm\n")
        elif ind2 == 1:
            str += ("pacman -Sy xorg-server xorg-drivers xorg-xinit virtualbox-guest-utils --noconfirm\n")

    ######################## DE/WM

    ind = fun.inp(9, "Установим DE/WM?\n"
                     "1 - KDE(Plasma)\n"
                     "2 - xfce (В разработке)\n"
                     "3 - gmome\n"
                     "4 - lxde (В разработке)\n"
                     "5 - Deepin (В разработке)\n"
                     "6 - Mate (В разработке)\n"
                     "7 - Lxqt (В разработке)\n"
                     "8 - i3 (  конфиги стандартные, возможна установка с автовходом )\n"
                     "9 - пропустить\n"
                     "Выбор: ")

    if ind == 1:
        str += (
            "pacman -S  plasma plasma-meta plasma-pa plasma-desktop kde-system-meta kde-utilities-meta kio-extras kwalletmanager latte-dock  konsole  kwalletmanager --noconfirm\n")
        ind2 = fun.inp(2, "Если желаете использовать 2 окружения, "
                          "тогда укажите 0\n"
                          "Нужен автовход без DM?\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")

        if ind2 == 1:
            str += ("pacman -S xorg-xinit --noconfirm\n")
            str += ("cp /etc/X11/xinit/xinitrc /home/" + username + "/.xinitrc\n")
            str += ("chown " + username + ":users /home/" + username + "/.xinitrc\n")
            str += ("chmod +x /home/" + username + "/.xinitrc\n")
            str += ("sed -i 52,55d /home/" + username + "/.xinitrc\n")
            str += ("echo \"exec startplasma-x11 \" >> /home/" + username + "/.xinitrc\n")
            str += ("mkdir /etc/systemd/system/getty@tty1.service.d/\n")
            str += ("echo \" [Service] \" > /etc/systemd/system/getty@tty1.service.d/override.conf\n")

            str += ("echo \" ExecStart=\" >> /etc/systemd/system/getty@tty1.service.d/override.conf\n")
            str += (
                "echo   ExecStart=-/usr/bin/agetty --autologin $username --noclear %I 38400 linux >> /etc/systemd/system/getty@tty1.service.d/override.conf\n")
            str += ("echo ' [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx ' >> /etc/profile\n")

        str += ("pacman -R konqueror --noconfirm\n")

    elif ind == 2:
        str += ("pacman -S  xfce4  pavucontrol xfce4-goodies  --noconfirm\n")

    elif ind == 3:
        str += ("pacman -S gnome gnome-extra  --noconfirm\n")

    elif ind == 4:
        str += ("pacman -S lxde --noconfirm\n")

    elif ind == 5:
        str += ("pacman -S deepin deepin-extra --noconfirm\n")

    elif ind == 6:
        str += ("pacman -S  mate mate-extra  --noconfirm\n")

    elif ind == 7:
        str += ("pacman -S lxqt lxqt-qtplugin lxqt-themes oxygen-icons xscreensaver --noconfirm\n")

    elif ind == 8:
        str += ("pacman -S i3 i3-wm i3status dmenu --noconfirm\n")

    elif ind == 9:
        print("Пропущено")

    ######################## Второй

    ind = fun.inp(9, "Установим DE/WM?\n"
                     "1 - KDE(Plasma)\n"
                     "2 - xfce (В разработке)\n"
                     "3 - gmome\n"
                     "4 - lxde (В разработке)\n"
                     "5 - Deepin (В разработке)\n"
                     "6 - Mate (В разработке)\n"
                     "7 - Lxqt (В разработке)\n"
                     "8 - i3 (  конфиги стандартные, возможна установка с автовходом )\n"
                     "9 - пропустить\n"
                     "Выбор: ")

    if ind == 1:
        str += (
            "pacman -S  plasma plasma-meta plasma-pa plasma-desktop kde-system-meta kde-utilities-meta kio-extras kwalletmanager latte-dock  konsole  kwalletmanager --noconfirm\n")

    elif ind == 2:
        str += ("pacman -S  xfce4  pavucontrol xfce4-goodies  --noconfirm\n")

    elif ind == 3:
        str += ("pacman -S gnome gnome-extra  --noconfirm\n")

    elif ind == 4:
        str += ("pacman -S lxde --noconfirm\n")

    elif ind == 5:
        str += ("pacman -S deepin deepin-extra --noconfirm\n")

    elif ind == 6:
        str += ("pacman -S  mate mate-extra  --noconfirm\n")

    elif ind == 7:
        str += ("pacman -S lxqt lxqt-qtplugin lxqt-themes oxygen-icons xscreensaver --noconfirm\n")

    elif ind == 8:
        str += ("pacman -S i3 i3-wm i3status dmenu --noconfirm\n")

    elif ind == 9:
        print("Пропущено")

    ind = fun.inp(2, "Установим nitrogen?\n"
                     "1 - да\n"
                     "2 - нет\n"
                     "Выбор: ")

    if ind == 1:
        str += ("pacman -Sy nitrogen  --noconfirm\n")

    ######################## Менеджер входа

    ind = fun.inp(4, "Arch-wiki рекоендует для:\n"
                     "kde      <-> sddm\n"
                     "Lxqt     <-> sddm\n"
                     "xfce(i3) <-> lxdm\n"
                     "lxde     <-> lxdm\n"
                     "Gnome    <-> gdm\n"
                     "Deepin   <-> lxdm\n"
                     "Mate     <-> lxdm \n"
                     "Установка Менеджера входа в системуn\n"
                     "1 - Sddm\n"
                     "2 - lxdm \n"
                     "3 - gdm\n"
                     "4 - пропустить:\n"
                     "Выбор: ")

    if ind == 1:
        str += ("pacman -S sddm sddm-kcm --noconfirm\n")
        str += ("systemctl enable sddm.service -f\n")

    if ind == 2:
        str += ("pacman -S lxdm --noconfirm\n")
        str += ("systemctl enable lxdm.service -f\n")

    if ind == 3:
        str += ("pacman -S gdm --noconfirm\n")
        str += ("systemctl enable gdm.service -f\n")

    ######################## NetworkManager

    ind = fun.inp(2, "Нужен NetworkManager ?\n"
                     "1 - да\n"
                     "2 - нет \n"
                     "Выбор: ")

    if ind == 1:
        str += ("pacman -Sy networkmanager networkmanager-openvpn network-manager-applet ppp --noconfirm\n")
        str += ("systemctl enable NetworkManager.service\n")

    ######################## dhcpcd

    ind = fun.inp(2,
                  "Добавим dhcpcd в автозагрузку( для проводного интернета, который  получает настройки от роутера ) ?\n"
                  "1 - да\n"
                  "2 - нет \n"
                  "Выбор: ")

    if ind == 1:
        str += ("systemctl enable dhcpcd.service\n")

    ######################## поддержка звука

    ind = fun.inp(2, "Нужна поддержка звука?\n"
                     "1 - да\n"
                     "2 - нет \n"
                     "Выбор: ")

    if ind == 1:
        str += ("pacman -Sy pulseaudio-bluetooth alsa-utils pulseaudio-equalizer-ladspa   --noconfirm\n")
        str += ("systemctl enable bluetooth.service\n")

    ######################## ntfs и fat

    ind = fun.inp(2, "Нужна поддержка ntfs и fat?\n"
                     "1 - да\n"
                     "2 - нет \n"
                     "Выбор:")

    if ind == 1:
        str += ("pacman -Sy exfat-utils ntfs-3g   --noconfirm\n")

    ######################## архив

    ind = fun.inp(3, "Нужны программы для работы с архивами??\n"
                     "1 - ark ( Plasma(kde)- так же можно и для другого de )\n"
                     "2 - file-roller легковесный архиватор ( для xfce-lxqt-lxde-gnome )\n"
                     "3 - нет: \n"
                     "Выбор: ")

    if ind == 1:
        str += ("pacman -Sy unzip unrar  lha ark --noconfirm\n")

    if ind == 2:
        str += ("pacman -Sy unzip unrar lha file-roller p7zip unace lrzip  --noconfirm \n")

    ######################## Установка дополнительных программ ( установка всех программ по желанию )

    ind = fun.inp(2, "Установка дополнительных программ ( установка всех программ по желанию )?\n"
                     ">> blueman\n"
                     ">> htop\n"
                     ">> fiezilla\n"
                     ">> gwenview\n"
                     ">> steam\n"
                     ">> neofetch\n"
                     ">> screenfetch\n"
                     ">> vlc\n"
                     ">> gparted\n"
                     ">> telegram-desktop\n"
                     ">> spectacle\n"
                     ">> flameshot\n"
                     "===============\n"
                     "1 - да \n"
                     "2 - нет \n"
                     "Выбор: ")

    if ind == 1:

        ind2 = fun.inp(4, "Будете ли вы подключать Android или Iphone к ПК через USB?\n"
                          "1 - Android\n"
                          "2 - Iphone\n"
                          "3 - оба варианта\n"
                          "4 - пропустить:\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S gvfs-mtp --noconfirm\n")
        if ind2 == 2:
            str += ("pacman -S gvfs-afc --noconfirm\n")
        if ind2 == 3:
            str += ("pacman -S gvfs-afc gvfs-mtp --noconfirm\n")

        ############

        ind2 = fun.inp(2, "blueman --диспетчер blutooth устройств\n"
                          "полезно для i3\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S blueman --noconfirm\n")

        ############

        ind2 = fun.inp(2, "htop--диспетчер задач для linux\n"
                          "1 - да \n"
                          "0 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S htop xterm --noconfirm\n")

        ############

        ind2 = fun.inp(2, "Filezilla - графический клиент для работы с FTP/SFTP\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S filezilla --noconfirm\n")

        ############

        ind2 = fun.inp(2, "gwenview - программа для просмотра изображений для gnome и xfce есть собственное\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S gwenview --noconfirm\n")

        ############

        ind2 = fun.inp(2, "Steam - магазин игр\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S steam steam-native-runtime --noconfirm\n")

        ############

        ind2 = fun.inp(2, "neofetch - вывод данных о системе с лого в консоли\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S neofetch  --noconfirm\n")

        ############

        ind2 = fun.inp(2, "screenfetch - вывод данных о системе с лого в консоли( аналог neofetch )\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S screenfetch  --noconfirm\n")

        ############

        ind2 = fun.inp(2, "vlc - проигрыватель мультимедиа\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S vlc  --noconfirm\n")

        ############

        ind2 = fun.inp(2, "gparted - программа для работы с разделами sdd/hdd\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S gparted  --noconfirm\n")

        ############

        ind2 = fun.inp(2, "telegram - мессенджер\n"
                          "1 - да\n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S telegram-desktop   --noconfirm\n")

        ############

        ind2 = fun.inp(4, "установим программу для создания скриншотов?\n"
                          "spectacle(интегрируется в рабочий стол  Plasma(kde)) и flameshot(универсальна, хорошо работает в KDE и Xfce)\n"
                          "1 - spectacle\n"
                          "2 - flameshot\n"
                          "3 - оба варианта\n"
                          "4 - пропустить\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("pacman -S spectacle   --noconfirm\n")
        if ind2 == 2:
            str += ("pacman -S flameshot --noconfirm\n")
        if ind2 == 3:
            str += ("pacman -S spectacle flameshot --noconfirm\n")

    ########################

    str += (
        "pacman -S  ttf-arphic-ukai git ttf-liberation ttf-dejavu ttf-arphic-uming ttf-fireflysung ttf-sazanami --noconfirm\n")

    ind = fun.inp(6, "Установим браузер?\n"
                     "1 - google-chrome \n"
                     "2 - firefox\n"
                     "3 - chromium\n"
                     "4 - opera ( + pepper-flash )\n"
                     "5 - установить все\n"
                     "6 - пропустить\n"
                     "Выбор: ")
    if ind == 1:
        str += ("cd /home/" + username + "\n")
        str += ("git clone https://aur.archlinux.org/google-chrome.git\n")
        str += ("chown -R " + username + ":users /home/" + username + "/google-chrome\n")
        str += ("chown -R " + username + ":users /home/" + username + "/google-chrome/PKGBUILD\n")
        str += ("cd /home/" + username + "/google-chrome\n")
        str += ("sudo -u " + username + "  makepkg -si --noconfirm\n")
        str += ("rm -Rf /home/" + username + "/google-chrome\n")

    elif ind == 2:
        str += ("pacman -S firefox firefox-i18n-ru --noconfirm\n")
    elif ind == 3:
        str += ("pacman -S chromium --noconfirm\n")
    elif ind == 4:
        str += ("pacman -S opera pepper-flash --noconfirm\n")
    elif ind == 5:
        str += ("pacman -S chromium opera pepper-flash firefox firefox-developer-edition-i18n-ru --noconfirm\n")
        str += ("cd /home/" + username + "\n")
        str += ("git clone https://aur.archlinux.org/google-chrome.git\n")
        str += ("chown -R " + username + ":users /home/" + username + "/google-chrome\n")
        str += ("chown -R " + username + ":users /home/" + username + "/google-chrome/PKGBUILD\n")
        str += ("cd /home/" + username + "/google-chrome\n")
        str += ("sudo -u " + username + "  makepkg -si --noconfirm\n")
        str += ("rm -Rf /home/" + username + "/google-chrome\n")

    ########################

    ind = fun.inp(2, "установим офисный пакет libreoffice  для работы с документами?\n"
                     "1 - да \n"
                     "2 - нет\n"
                     "Выбор: ")
    if ind == 1:
        str += ("pacman -S libreoffice-still libreoffice-still-ru --noconfirm\n")

    ########################

    ind = fun.inp(2, "Установим ssh(клиент) для удаленного доступа\n"
                     "1 - да \n"
                     "2 - нет\n"
                     "Выбор: ")

    if ind == 1:
        str += ("pacman -S openssh --noconfirm\n")
        ind2 = fun.inp(6, "Включим в автозагрузку ssh(server) для удаленного доступа к этому пк?\n"
                          "1 - да \n"
                          "2 - нет\n"
                          "Выбор: ")
        if ind2 == 1:
            str += ("systemctl enable sshd.service\n")

    ########################

    ind = fun.inp(3, "Установим  aur-helper ( pikaur-(идет как зависимость для octopi) или yay ) ?\n"
                     "1 - pikaur \n"
                     "2 - yay\n"
                     "3 - пропустить\n"
                     "Выбор: ")
    if ind == 1:
        str += (""
                "cd /home/$username\n"
                "git clone https://aur.archlinux.org/pikaur.git\n"
                "chown -R " + username + ":users /home/" + username + "/pikaur\n"
                                                                      "chown -R " + username + ":users /home/" + username + "/pikaur/PKGBUILD \n"
                                                                                                                            "cd /home/" + username + "/pikaur\n"
                                                                                                                                                     "sudo -u " + username + "  makepkg -si --noconfirm\n"
                                                                                                                                                                             "rm -Rf /home/" + username + "/pikaur\n")
    if ind == 1:
        str += (""
                "cd /home/" + username + "\n"
                                         "git clone https://aur.archlinux.org/yay.git\n"
                                         "chown -R " + username + ":users /home/" + username + "/yay\n"
                                                                                               "chown -R " + username + ":users /home/" + username + "/yay/PKGBUILD\n"
                                                                                                                                                     "cd /home/" + username + "/yay \n"
                                                                                                                                                                              "sudo -u " + username + "  makepkg -si --noconfirm \n"
                                                                                                                                                                                                      "rm -Rf /home/" + username + "/yay\n")

    ########################

    ind = fun.inp(2, "Установим teamviewer для удаленного доступа ?\n"
                     "1 - да \n"
                     "2 - нет\n"
                     "Выбор: ")
    if ind == 1:
        str += (""
                "cd /home/" + username + " \n"
                                         "git clone https://aur.archlinux.org/teamviewer.git\n"
                                         "chown -R " + username + ":users /home/" + username + "/teamviewer\n"
                                                                                               "chown -R " + username + ":users /home/" + username + "/teamviewer/PKGBUILD \n"
                                                                                                                                                     "cd /home/" + username + "/teamviewer  \n"
                                                                                                                                                                              "sudo -u " + username + "  makepkg -si --noconfirm  \n"
                                                                                                                                                                                                      "rm -Rf /home/" + username + "/teamviewer\n"
                                                                                                                                                                                                                                   "systemctl enable teamviewerd.service\n")

    ########################

    ind = fun.inp(2, "Установим vk-messenger ?\n"
                     "1 - да \n"
                     "2 - нет\n"
                     "Выбор: ")
    if ind == 1:
        str += (""
                "cd /home/" + username + "\n"
                                         "git clone https://aur.archlinux.org/gconf.git \n"
                                         "chown -R " + username + ":users /home/" + username + "/gconf\n"
                                                                                               "chown -R " + username + ":users /home/" + username + "/gconf/PKGBUILD \n"
                                                                                                                                                     "cd /home/" + username + "/gconf  \n"
                                                                                                                                                                              "sudo -u " + username + "  makepkg -si --noconfirm  \n"
                                                                                                                                                                                                      "rm -Rf /home/" + username + "/gconf\n")

    ########################

    str += (""
            "cd /home/" + username + "\n"
            "git clone https://aur.archlinux.org/vk-messenger.git\n"
            "chown -R " + username + ":users /home/" + username + "/vk-messenger\n"
            "chown -R " + username + ":users /home/" + username + "/vk-messenger/PKGBUILD \n"
            "cd /home/" + username + "/vk-messenger  \n"
            "sudo -u " + username + "  makepkg -si --noconfirm  \n"
            "rm -Rf /home/" + username + "/vk-messenger\n")

    ########################

    str += (""
            "cd /home/" + username + "\n"
            "git clone https://aur.archlinux.org/pamac-aur.git\n"
            "chown -R " + username + ":users /home/" + username + "/pamac-aur\n"
            "chown -R " + username + ":users /home/" + username + "/pamac-aur/PKGBUILD \n"
            "sudo -u " + username + "  makepkg -si --noconfirm  \n"
            "rm -Rf /home/" + username + "/pamac-aur\n")
    ########################

    if flag:
        f = open("/etc/mkinitcpio.conf", "w")
        f.write(fun.opt())
        f.close

        f.open("/etc/fstab")
        f.write("tmpfs /tmp   tmpfs   nodev,nosuid   0   0"
                "tmpfs /var/tmp tmpfs defaults 0 0"
                "tmpfs /var/log tmpfs defaults 0 0")
        f.close


    ########################

    str += ("sudo pacman -Su\n"
            "sudo pacman -Syy\n")

    ########################
    ########################
    ########################
    ########################

    print("\n\n\n\n\n\n\n")
    print("генерация скрипта...\n"
          "====================\n")

    # for x in res:
    # 	print(x + "\t\t --> записано\n")
    # 	pass

    print(str + "\n")

    print("Скрипт сгениерирован!")
    ind = fun.inp(3, "Что теперь?\n"
                     "1. Выполнить\n"
                     "2. Сохранить в файл\n"
                     "3. Выйти\n"
                     "Выбор: ")
    if ind == 1:
        ch = 0
        while ch == 0:
            warn = input("Введите число 1451345 для проверки:  ")
            if warn == '1451345':
                ch = 1
                # os.system(str)
            pass
    elif ind == 2:
        f = open("boot.sh", "w")
        f.write(res)  # Сейчас тут ошибка
        f.close()
        print("Записано в файл boot.sh")
    pass
