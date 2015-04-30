# gamine-rpm

If you want to build an rpm for Fedora , you will need a spec file and patch.

Below is how to do this on Fedora 22.

Try something like this:

    sudo dnf groupinstall "RPM Development Tools" "C Development Tools and Libraries"
    sudo dnf install libxml2-devel gtk2-devel gstreamer-devel 
    rpmdev-setuptree
    cd ~/rpmbuild/SOURCES/
    wget https://github.com/btong/gamine/releases/download/gamine-1.1/gamine-1.1.tar.gz

Ensure the following files from this repo exist:

    ~/rpmbuild/SPECS/gamine.spec
    ~/rpmbuild/SOURCES/gamine-1.1.patch

Now build the rpm:

     rpmbuild -ba ~/rpmbuild/SPECS/gamine.spec

You will find the rpm under:

     ~/rpmbuild/RPMS/x86_64/

