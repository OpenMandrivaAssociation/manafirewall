Name:		manafirewall
Version:	0.0.1
Release:	1.09.06.2019
Summary:	manatools firewalld configuration tool
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/manatools/manafirewall
Source0:	manafirewall-master.09.06.2019.zip
Patch0:   manafirewall-remove-distribute-openmandriva.patch

BuildRequires:	pkgconfig(libyui)
BuildRequires:  pkgconfig(libyui-mga)
BuildRequires:  pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(python)
BuildRequires:  python-libyui
BuildRequires:  python3egg(setuptools)
BuildRequires:  python3egg(pyyaml)

Requires:  python-manatools
Requires:  firewalld
Requires:  python3dist(setuptools)
Requires:  python-yaml

%description
This is the graphical configuration tool for firewalld based on python manatools and libYui 
(Suse widget abstraction library), to be run using QT, Gtk or ncurses interface.

%prep
%setup -q -n manafirewall-master
%autopatch -p0

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
%{python_sitelib}/manafirewall-0.0.1-py*.egg-info/PKG-INFO
%{python_sitelib}/manafirewall-0.0.1-py*.egg-info/SOURCES.txt
%{python_sitelib}/manafirewall-0.0.1-*.egg-info/dependency_links.txt
%{python_sitelib}/manafirewall-0.0.1-py*.egg-info/requires.txt
%{python_sitelib}/manafirewall-0.0.1-py*.egg-info/top_level.txt
%{python_sitelib}/manafirewall/__init__.py
%{python_sitelib}/manafirewall/__pycache__/__init__.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/__init__.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/dialog.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/dialog.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/forwardDialog.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/forwardDialog.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/helpinfo.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/helpinfo.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/portDialog.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/portDialog.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/protocolDialog.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/protocolDialog.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/serviceBaseDialog.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/serviceBaseDialog.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/version.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/version.cpython-*.pyc
%{python_sitelib}/manafirewall/__pycache__/zoneBaseDialog.cpython-*.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/zoneBaseDialog.cpython-*.pyc
%{python_sitelib}/manafirewall/dialog.py
%{python_sitelib}/manafirewall/forwardDialog.py
%{python_sitelib}/manafirewall/helpinfo.py
%{python_sitelib}/manafirewall/portDialog.py
%{python_sitelib}/manafirewall/protocolDialog.py
%{python_sitelib}/manafirewall/serviceBaseDialog.py
%{python_sitelib}/manafirewall/version.py
%{python_sitelib}/manafirewall/zoneBaseDialog.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
