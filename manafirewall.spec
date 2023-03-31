%global debug_package %{nil}

Name:		manafirewall
Version:	0.0.3
Release:	2
Summary:	manatools firewalld configuration tool
Group:		System/Libraries
License:	GPLv2
URL:		https://github.com/manatools/manafirewall
Source0:	https://github.com/manatools/manafirewall/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	pkgconfig(libyui)
BuildRequires:	pkgconfig(libyui-mga)
BuildRequires:	pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-libyui
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pyyaml)
Requires:	python-manatools
Requires:	firewalld
Requires:	python3dist(setuptools)
Requires:	python-yaml
Requires:	python-libyui
Requires:	libyui-ncurses
Requires:	libyui-mga-ncurses
Requires:	libyui-mga-qt

%description
This is the graphical configuration tool for firewalld based on python manatools and libYui 
(Suse widget abstraction library), to be run using QT, Gtk or ncurses interface.

%prep
%autosetup -n manafirewall-%{version} -p1

%build
%cmake	-DCHECK_RUNTIME_DEPENDENCIES=ON	\
	-Wno-dev
%make_build


%install
%make_install -C build

%find_lang %{name}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=manafirewall
Comment=Firewall
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Settings;Security;Internet
EOF

%files -f %{name}.lang
%{_bindir}/manafirewall
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/*.py
%{python_sitelib}/%{name}/__pycache__
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/org.mageia.manafirewall.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/metainfo/org.mageia.manafirewall.metainfo.xml
