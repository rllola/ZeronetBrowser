# -*- mode: ruby -*-
# vi: set ft=ruby :

###############################################################################
#                                                                             #
# Vagrantfile project: ZeroNet Browser                                        #
# Description:                                                                #
# Will start a ubuntu 14.04 box with Zeronet browser starting                 #
# Author: Lola                                                                #
#                                                                             #
###############################################################################

Vagrant.require_version ">= 1.8.0"
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/xenial64"

  # Forwarding zeronet ports
  config.vm.network "forwarded_port", guest: 43110, host: 43110
  config.vm.network "forwarded_port", guest: 15441, host: 15441

  config.vm.provider "virtualbox" do |vb|
     vb.name = "ZeroNet Browser"
     #vb.gui = true
     vb.customize ["modifyvm", :id, "--memory", "1572"]
     vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
  end

  config.vm.synced_folder ".", "/home/vagrant/Browser"

  # Install Zeronet and load all the requirements
  config.vm.provision :shell, path: "provision.sh", privileged: false

end
