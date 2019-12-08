Name:		manafirewall
Version:	0.0.1
Release:	0.09.06.2019
Summary:	manatools firewalld configuration tool
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/manatools/manafirewall
Source0:	manafirewall-master.09.06.2019.zip

BuildRequires:	pkgconfig(libyui)
BuildRequires:  pkgconfig(libyui-mga)
BuildRequires:  pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(python)
BuildRequires:  python-libyui
BuildRequires:  python3egg(setuptools)
BuildRequires:  python3egg(pyyaml)

Requires:  python-manatools
Requires:  firewalld
Requires:  python3-distribute
Requires:  python3dist(setuptools)

%description
This is the graphical configuration tool for firewalld based on python manatools and libYui 
(Suse widget abstraction library), to be run using QT, Gtk or ncurses interface.

%prep
%setup -q -n manafirewall-master
%autopatch -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
