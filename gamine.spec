Name:           gamine
Version:        1.1
Release:        6
Summary:        An interactive game for young children
License:        GPLv2
Group:          Education
#http://gitorious.org/gamine/gamine
URL:            http://www.gnunux.info/projets/gamine
Source0:        http://www.gnunux.info/projets/gamine/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gstreamer-0.10)
 
%description
Gamine is a game designed for 2 years old children who
are not able to use a keyboard. The child uses the mouse
to draw coloured dots and lines on the screen.
 
%prep
%setup -q
pushd locale
tar -xf %{SOURCE0}
popd
%patch0 -p1
sed -i 's/^LDLIBS = /LDLIBS = -lX11 -lm /' Makefile
sed -i 's|printf(gettext(.*), cursorfile);||g' %{name}.c
sed -i 's|sounds/README|README.sounds|g' COPYING
 
%build
make PREFIX=%{_prefix}
 
%install
mkdir -p %{buildroot}/%{_prefix}
%makeinstall PREFIX=%{buildroot}/%{_prefix}
rm -f %{buildroot}%{_datadir}/%{name}/pencil.png
rm -f %{buildroot}%{_datadir}/doc/%{name}/README.pencil
 
#menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Gamine
GenericName=Gamine
Comment=Educational game for young children
Comment[ru]=Обучающая игра для маленьких детей
Comment[cs]=Vzdělávací hra pro malé děti
Comment[es]=Juego educativo para niños pequeños
Comment[it]=Gioco educativo per bambini
Comment[ms]=Permainan pendidikan untuk kanak-kanak
Comment[pt]=Jogo educacionais para crianças
Comment[pt_BR]=Jogo educativos para crianças
Comment[uk]=Розвиваюча гра для дітей молодшого віку
Comment[fr]=Jeu éducatif pour jeunes enfants
Comment[de]=Lernspiel für Kinder
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;KidsGame;
EOF
 
%find_lang %{name}
 
%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
/usr/share/gamine/gamine.png
/usr/share/icons/hicolor/scalable/apps/%{name}.svg
 
