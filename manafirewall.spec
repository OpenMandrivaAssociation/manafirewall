%global debug_package %{nil}

Name:		manafirewall
Version:	0.0.1
Release:	3
Summary:	manatools firewalld configuration tool
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/manatools/manafirewall
Source0:	https://github.com/manatools/manafirewall/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		manafirewall-remove-distribute-openmandriva.patch
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
Requires:	libyui-mga-ncurses
Requires:	libyui-mga-qt

%description
This is the graphical configuration tool for firewalld based on python manatools and libYui 
(Suse widget abstraction library), to be run using QT, Gtk or ncurses interface.

%prep
%autosetup -n manafirewall-%{version} -p0

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

install -p -D -m644 share/images/256x256/manafirewall.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

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

%files
%{_bindir}/manafirewall
%dir %{python_sitelib}/%{name}-0.0.1-py%{py_ver}.egg-info
%{python_sitelib}/%{name}-0.0.1-py%{py_ver}.egg-info/PKG-INFO
%{python_sitelib}/%{name}-0.0.1-py*.egg-info/*.txt
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/*.py
%{python_sitelib}/%{name}/__pycache__
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
