#
# Project Kimchi
#
# Copyright IBM, Corp. 2013
#
# Authors:
#  Aline Manera <alinefm@linux.vnet.ibm.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import gettext

_ = gettext.gettext


messages = {
    "KCHAPI0001E": _("Unkown parameter specified %(value)s"),
    "KCHAPI0002E": _("Delete is not allowed for %(resource)s"),
    "KCHAPI0003E": _("%(resource)s does not implement update method"),
    "KCHAPI0004E": _("Parameters %(params)s are not allowed to be updated in %(resource)s"),
    "KCHAPI0005E": _("Create is not allowed for %(resource)s"),
    "KCHAPI0006E": _("Unable to parse JSON request"),
    "KCHAPI0007E": _("This API only supports"),

    "KCHASYNC0001E": _("Datastore is not initiated in the model object."),

    "KCHAUTH0001E": _("Authentication failed for user '%(userid)s'. [Error code: %(code)s]"),
    "KCHAUTH0002E": _("You are not authorized to access Kimchi"),
    "KCHAUTH0003E": _("Specify %(item)s to login into Kimchi"),

    "KCHDISKS0001E": _("Error while getting block devices. Details: %(err)s"),
    "KCHDISKS0002E": _("Error while getting block device information for %(device)s."),

    "KCHDL0001E": _("Unable to find distro file: %(filename)s"),
    "KCHDL0002E": _("Unable to parse distro file: %(filename)s. Make sure, it is a JSON file."),

    "KCHISCSI0001E": _("Unable to login to iSCSI host target %(portal)s. Details: %(err)s"),
    "KCHISCSI0002E": _("Unable to login to iSCSI host %(host)s target %(target)s"),

    "KCHISO0001E": _("Unable to find ISO file ISO %(filename)s"),
    "KCHISO0002E": _("The ISO file %(filename)s is not bootable"),
    "KCHISO0003E": _("The ISO file %(filename)s does not have a valid El Torito boot record"),
    "KCHISO0004E": _("Invalid El Torito validation entry in ISO %(filename)s"),
    "KCHISO0005E": _("Invalid El Torito boot indicator in ISO %(filename)s"),
    "KCHISO0006E": _("Unexpected volume type for primary volume in ISO %(filename)s"),
    "KCHISO0007E": _("Bad format while reading volume descriptor in ISO %(filename)s"),

    "KCHVM0001E": _("Virtual machine $(name)s already exists"),
    "KCHVM0002E": _("Virtual machine %(name)s does not exist"),
    "KCHVM0003E": _("Unable to rename virtual machine %(name)s. The name %(new_name)s already exists or it is not powered off."),
    "KCHVM0004E": _("Unable to retrieve screenshot for stopped virtual machine %(name)s"),
    "KCHVM0005E": _("Remote ISO image is not supported by this server."),
    "KCHVM0006E": _("Screenshot not supported for virtual machine %(name)s"),
    "KCHVM0007E": _("Unable to create virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0008E": _("Unable to rename virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0009E": _("Unable to retrieve virtual machine %(name)s. Details: %(err)"),
    "KCHVM0010E": _("Unable to connect to powered off machine %(name)s."),
    "KCHVM0011E": _("Virtual machine name must be a string"),
    "KCHVM0012E": _("Invalid template URI: %(value)s specified for virtual machine"),
    "KCHVM0013E": _("Invalid storage pool URI: %(value)s specified for virtual machine"),
    "KCHVM0014E": _("Supported virtual machine graphics are spice or VNC"),
    "KCHVM0015E": _("Graphics address to listen on must be IPv4 or IPv6"),
    "KCHVM0016E": _("Specify a template to create a virtual machine from"),

    "KCHVMIF0001E": _("Interface %(iface)s does not exist in virtual machine %(name)s"),
    "KCHVMIF0002E": _("Network %(network)s specified for virtual machine %(name)s does not exist"),
    "KCHVMIF0003E": _("Do not support guest interface hot plug attachment"),
    "KCHVMIF0004E": _("Supported virtual machine interfaces type is only network"),
    "KCHVMIF0005E": _("Network name for virtual machine interface must be a string"),
    "KCHVMIF0006E": _("Invalid network model card specified for virtual machine interface"),
    "KCHVMIF0007E": _("Specify type and network to add a new virtual machine interface"),

    "KCHTMPL0001E": _("Template %(name)s already exists"),
    "KCHTMPL0002E": _("Template %(name)s does not exist"),
    "KCHTMPL0003E": _("Network '%(network)s' specified for template %(template)s does not exist"),
    "KCHTMPL0004E": _("Storage pool %(pool)s specified for template %(template)s does not exist"),
    "KCHTMPL0005E": _("Storage pool %(pool)s specified for template %(template)s is not active"),
    "KCHTMPL0006E": _("Invalid parameter '%(param)s' specified for CDROM."),
    "KCHTMPL0007E": _("Network %(network)s specified for template %(template)s is not active"),
    "KCHTMPL0008E": _("Template name must be a string"),
    "KCHTMPL0009E": _("Template icon must be a path to the image"),
    "KCHTMPL0010E": _("Template distribution must be a string"),
    "KCHTMPL0011E": _("Template distribution version must be a string"),
    "KCHTMPL0012E": _("The number of CPUs must be a integer"),
    "KCHTMPL0013E": _("Amount of memory (MB) must be an integer greater than 512"),
    "KCHTMPL0014E": _("Template CDROM must be a local or remote ISO file"),
    "KCHTMPL0015E": _("Invalid storage pool URI %(value)s specified for template"),
    "KCHTMPL0016E": _("Specify an ISO image as CDROM to create a template"),
    "KCHTMPL0017E": _("All networks for the template must be specified in a list."),

    "KCHPOOL0001E": _("Storage pool %(name)s already exists"),
    "KCHPOOL0002E": _("Storage pool %(name)s does not exist"),
    "KCHPOOL0003E": _("Autostart flag must be true or false"),
    "KCHPOOL0004E": _("Specify %(item)s in order to create the storage pool %(name)s"),
    "KCHPOOL0005E": _("Unable to delete active storage pool %(name)s"),
    "KCHPOOL0006E": _("Unable to list storage pools. Details: %(err)s"),
    "KCHPOOL0007E": _("Unable to create storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0008E": _("Unable to get number of storage volumes in storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0009E": _("Unable to activate storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0010E": _("Unable to deactivate storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0011E": _("Unable to delete storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0012E": _("Unable to create NFS Pool as export path %(path)s may block during mount"),
    "KCHPOOL0013E": _("Unable to create NFS Pool as export path %(path)s mount failed"),
    "KCHPOOL0014E": _("Unsupported storage pool type: %(type)s"),
    "KCHPOOL0015E": _("Error while getting xml for storage pool %(pool)s"),
    "KCHPOOL0016E": _("Storage pool name must be a string"),
    "KCHPOOL0017E": _("Supported storage pool types are dir, netfs, logical and kimchi-iso"),
    "KCHPOOL0018E": _("Storage pool path must be a string"),
    "KCHPOOL0019E": _("Storage pool host must be a IP or hostname"),
    "KCHPOOL0020E": _("Storage pool devices must be the full path to the block device"),
    "KCHPOOL0021E": _("Storage pool devices parameter must be a list"),
    "KCHPOOL0022E": _("Target IQN of an iSCSI pool must be a string"),
    "KCHPOOL0023E": _("Port of a remote storage server must be an integer between 1 and 65535"),
    "KCHPOOL0024E": _("Login username of the iSCSI target must be a string"),
    "KCHPOOL0025E": _("Login password of the iSCSI target must be a string"),
    "KCHPOOL0026E": _("Specify name and type to create a storage pool"),
    "KCHPOOL0027E": _("%(disk)s is not a valid disk/partition. Could not add it to the pool %(pool)s."),
    "KCHPOOL0028E": _("Error while extending logical pool %(pool)s. Details: %(err)s"),
    "KCHPOOL0029E": _("The parameter disks only can be updated for logical storage pool."),

    "KCHVOL0001E": _("Storage volume %(name)s already exists"),
    "KCHVOL0002E": _("Storage volume %(name)s does not exist in storage pool %(pool)s"),
    "KCHVOL0003E": _("Unable to create storage volume %(volume)s becuase storage pool %(pool)s is not active"),
    "KCHVOL0004E": _("Specify %(item)s in order to create storage volume %(volume)s"),
    "KCHVOL0005E": _("Unable to retrieve storage volume %(volume)s because storage pool %(pool)s is not active"),
    "KCHVOL0006E": _("Unable to list storage volumes because storage pool %(pool)s is not active"),
    "KCHVOL0007E": _("Unable to create storage volume %(name)s in storage pool %(pool)s. Details: %(err)s"),
    "KCHVOL0008E": _("Unable to list storage volumes in storage pool %(pool)s. Details: %(err)s"),
    "KCHVOL0009E": _("Unable to wipe storage volumes %(name)s. Details: %(err)s"),
    "KCHVOL0010E": _("Unable to delete storage volume %(name)s. Details: %(err)s"),
    "KCHVOL0011E": _("Unable to resize storage volume %(name)s. Details: %(err)s"),

    "KCHIFACE0001E": _("Interface %(name)s does not exist"),

    "KCHNET0001E": _("Network %(name)s already exists"),
    "KCHNET0002E": _("Network %(name)s does not exist"),
    "KCHNET0003E": _("Subnet %(subnet)s specified for network %(network)s  is not valid."),
    "KCHNET0004E": _("Specify a network interface to create bridged network %(name)s"),
    "KCHNET0005E": _("Unable to delete active network %(name)s"),
    "KCHNET0006E": _("Interface %(iface)s specified for network %(network)s is already in use"),
    "KCHNET0007E": _("Interface should be bare NIC, bonding or bridge device."),
    "KCHNET0008E": _("Unable to create network %(name)s. Details: %(err)s"),
    "KCHNET0009E": _("Unable to find a free IP address for network '%(name)s'"),
    "KCHNET0010E": _("Unable to create VLAN tagged bridge using interface %(iface)s. Details: %(err)"),
    "KCHNET0011E": _("Network name must be a string"),
    "KCHNET0012E": _("Supported network types are isolated, NAT and bridge"),
    "KCHNET0013E": _("Network subnet must be a string with IP address and prefix or netmask"),
    "KCHNET0014E": _("Network interface must be a string"),
    "KCHNET0015E": _("Network VLAN ID must be an integer between 1 and 4094"),
    "KCHNET0016E": _("Specify name and type to create a Network"),

    "KCHDR0001E": _("Debug report %(name)s does not exist"),
    "KCHDR0002E": _("Debug report tool not found in system"),
    "KCHDR0003E": _("Unable to create debug report %(name)s. Details: %(err)s."),
    "KCHDR0004E": _("Can not find generated debug report named %(name)s"),
    "KCHDR0005E": _("Unable to generate debug report %(name)s. Details: %(err)s"),

    "KCHSR0001E": _("Storage server %(server)s was not used by Kimchi"),

    "KCHDISTRO0001E": _("Distro '%(name)s' does not exist"),

    "KCHPART0001E": _("Partition %(name)s does not exist in the host"),

    "KCHHOST0001E": _("Unable to shutdown host machine as there are running virtual machines"),
    "KCHHOST0002E": _("Unable to reboot host machine as there are running virtual machines"),

    "KCHOBJST0001E": _("Unable to find %(item)s in datastore"),

    "KCHUTILS0001E": _("Invalid URI %(uri)s"),
    "KCHUTILS0002E": _("Timeout while running command '%(cmd)s' after %(seconds)s seconds"),
    "KCHUTILS0003E": _("Unable to choose a virutal machine name"),
}
