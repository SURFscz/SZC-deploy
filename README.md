# Science Collaboration Zone
[![Build Status](https://travis-ci.com/SURFscz/SCZ-deploy.svg?branch=travis-docker)](https://travis-ci.org/SURFscz/SCZ-deploy)


The Science Collaboration Zone (SCZ) project offers an Identity Management solution
for research collaborations.  It is a middleware solution for
researchers, which allows them to

- log in using credentials from their university, as well as support (international) 'guests';
- handle (Identity and) Access Management (IAM) for their collaborations;
- allow members of their collaborations easy access to services (like web
  applications, databases, storage solutions, compute facilities, etc.);

More information can be obtained from <https://wiki.surfnet.nl/display/SCZ>.

## Technical

The SCZ is comprised of a number of existing, open source components:

### SBS
<https://github.com/SURFscz/SBS>

### Satosa
<https://github.com/IdentityPython/SATOSA>

### Pyff
<https://github.com/leifj/pyFF>

### LSC (LDAP Synchronisation Connector)
<https://github.com/lsc-project>


## SCZ-deploy
This repository consists of an Ansible playbook to install a complete
SCZ-platform.  The easiest way to get started is using Vagrant, which will
create a number of VMs on your local machine, en run the Ansible playbook to
install the different components onto the VMs.

We support this on both Linux (tested on Ubuntu 17.10 and 18.04, experimental on
openSUSE Tumbleweed) and OSX/MacOS (tested on High Sierra).
You can either deploy to full VMs (libvirt/qemu and Virtualbox are supported), or to container (using docker).

We _strongly_ recommend using the container/docker-based deploy, because it requires much less resources (should run
easily on a dual core machine with 8GB memory). To deploy to VMs, we recommend a quad-core CPU and at least 16GB of
memory, as the script will create 6 VMs with 768MB of memory each.

To get started, do the following:

- install Docker (>=19.03) and Ansible (>=2.7)
    - Ubuntu/Debian: `apt install ansible docker.io docker-compose`
    - OpenSUSE Tumbleweed: `zypper install ansible docker docker-compose`
    - MacOS: see
      <http://docs.ansible.com/ansible/latest/intro_installation.html#latest-releases-on-mac-osx>
      and <https://docs.docker.com/docker-for-mac/>

- Supply the vm secret to decrypt the vault
    - `echo [vault-secret] > secret_vm`
    - OR replace the encrypted vault secrets `google_client_id` and `google_client_secret`
    in environment/vm/secrets/all.yml.
    But you still need to insert a dummy secret in secret_vm.

    The `[vault-secret]` can be found on the SURFnet SRAM wiki.

- Install the required Ansible modules
    - `ansible-galaxy collection install -r requirements.yml`

- set up the containers and start the deploy:
    - `./start-vm`

    This will boot 8 containers/VMs and run ansible to deploy SCZ to these 8 hosts.

- when the deploy finishes, you should be able to browse to
  <https://sbs.scz-vm.net> and login using the default platform admin
  credentials `baas`/`baas`

