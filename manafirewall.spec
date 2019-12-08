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
Requires:  python-yaml

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
%{_bindir}/manafirewall
%{python_sitelib}/manafirewall-0.0.1-py3.7.egg-info/PKG-INFO
%{python_sitelib}/manafirewall-0.0.1-py3.7.egg-info/SOURCES.txt
%{python_sitelib}/manafirewall-0.0.1-py3.7.egg-info/dependency_links.txt
%{python_sitelib}/manafirewall-0.0.1-py3.7.egg-info/requires.txt
%{python_sitelib}/manafirewall-0.0.1-py3.7.egg-info/top_level.txt
%{python_sitelib}/manafirewall/__init__.py
%{python_sitelib}/manafirewall/__pycache__/__init__.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/__init__.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/dialog.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/dialog.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/forwardDialog.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/forwardDialog.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/helpinfo.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/helpinfo.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/portDialog.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/portDialog.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/protocolDialog.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/protocolDialog.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/serviceBaseDialog.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/serviceBaseDialog.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/version.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/version.cpython-37.pyc
%{python_sitelib}/manafirewall/__pycache__/zoneBaseDialog.cpython-37.opt-1.pyc
%{python_sitelib}/manafirewall/__pycache__/zoneBaseDialog.cpython-37.pyc
%{python_sitelib}/manafirewall/dialog.py
%{python_sitelib}/manafirewall/forwardDialog.py
%{python_sitelib}/manafirewall/helpinfo.py
%{python_sitelib}/manafirewall/portDialog.py
%{python_sitelib}/manafirewall/protocolDialog.py
%{python_sitelib}/manafirewall/serviceBaseDialog.py
%{python_sitelib}/manafirewall/version.py
%{python_sitelib}/manafirewall/zoneBaseDialog.py
