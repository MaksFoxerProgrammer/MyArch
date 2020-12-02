import os
from pac import fun

def standart():

    os.system('lsblk')

    root = input("Введите раздел для root (ошибки быть не должно, не предусмотрено!): ")
    boot = input("Введите раздел для boot (ошибки быть не должно, не предусмотрено!): ")

    os.system('mkfs.ext4 /dev/' + root + ' -L root')
    os.system('mount /dev/' + root + ' /mnt')

    if (boot != '0'):
        os.system('mkfs.ext2  /dev/' + boot + ' -L boot')
        os.system('mkdir /mnt/boot')
        os.system('mount /dev/' + boot + ' /mnt/boot')

    os.system('pacstrap /mnt base linux linux-headers dhcpcd which netctl inetutils  base-devel  wget linux-firmware nano wpa_supplicant dialog')

    os.system('genfstab -pU /mnt >> /mnt/etc/fstab')

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
    """)

    os.system('arch-chroot /mnt')
    """Судя по всему все остальное
    в отдельный файл, который скопировать
    и запустить в arch-chroot..."""

    
 


