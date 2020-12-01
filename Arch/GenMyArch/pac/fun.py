def inp(numb, text):

	while(True):
		try:
			var = int(input(text))

			count = 1

			while count != numb+1:
				if var == count:
					print("\n")
					return var
				count += 1

			print("\tОШИБКА: Такого варианта нет\n")

		except ValueError:			
			print("\tОШИБКА: Вы ввели недопустимое значение... \n")
	pass

def opt():
	str = "# vim:set ft=sh\n"
	"# MODULES\n"
	"# The following modules are loaded before any boot hooks are\n"
	"# run.  Advanced users may wish to specify all system modules\n"
	"# in this array.  For instance:\n"
	"#     MODULES=(piix ide_disk reiserfs)\n"
	"MODULES=()\n"

	"# BINARIES\n"
	"# This setting includes any additional binaries a given user may\n"
	"# wish into the CPIO image.  This is run last, so it may be used to\n"
	"# override the actual binaries included by a given hook\n"
	"# BINARIES are dependency parsed, so you may safely ignore libraries\n"
	"BINARIES=()\n"

	"# FILES\n"
	"# This setting is similar to BINARIES above, however, files are added\n"
	"# as-is and are not parsed in any way.  This is useful for config files.\n"
	"FILES=()\n"

	"# HOOKS\n"
	"# This is the most important setting in this file.  The HOOKS control the\n"
	"# modules and scripts added to the image, and what happens at boot time.\n"
	"# Order is important, and it is recommended that you do not change the\n"
	"# order in which HOOKS are added.  Run 'mkinitcpio -H <hook name>' for\n"
	"# help on a given hook.\n"
	"# 'base' is _required_ unless you know precisely what you are doing.\n"
	"# 'udev' is _required_ in order to automatically load modules\n"
	"# 'filesystems' is _required_ unless you specify your fs modules in MODULES\n"
	"# Examples:\n"
	"##   This setup specifies all modules in the MODULES setting above.\n"
	"##   No raid, lvm2, or encrypted root is needed.\n"
	"#    HOOKS=(base)\n"
	"#\n"
	"##   This setup will autodetect all modules for your system and should\n"
	"##   work as a sane default\n"
	"#    HOOKS=(base udev autodetect block filesystems)\n"
	"#\n"
	"##   This setup will generate a 'full' image which supports most systems.\n"
	"##   No autodetection is done.\n"
	"#    HOOKS=(base udev block filesystems)\n"
	"#\n"
	"##   This setup assembles a pata mdadm array with an encrypted root FS.\n"
	"##   Note: See 'mkinitcpio -H mdadm' for more information on raid devices.\n"
	"#    HOOKS=(base udev block mdadm encrypt filesystems)\n"
	"#\n"
	"##   This setup loads an lvm2 volume group on a usb device.\n"
	"#    HOOKS=(base udev block lvm2 filesystems)\n"
	"#\n"
	"##   NOTE: If you have /usr on a separate partition, you MUST include the\n"
	"#    usr, fsck and shutdown hooks.\n"
	"HOOKS=(base udev modconf block filesystems keyboard fsck)\n"

	"# COMPRESSION\n"
	"# Use this to compress the initramfs image. By default, gzip compression\n"
	"# is used. Use 'cat' to create an uncompressed image.\n"
	"#COMPRESSION=\"gzip\"\n"
	"#COMPRESSION=\"bzip2\"\n"
	"#COMPRESSION=\"lzma\"\n"
	"COMPRESSION=\"xz\"\n"
	"#COMPRESSION=\"lzop\"\n"
	"#COMPRESSION=\"lz4\"\n"

	"# COMPRESSION_OPTIONS\n"
	"# Additional options for the compressor\n"
	"#COMPRESSION_OPTIONS=()""\n"
	return str
		