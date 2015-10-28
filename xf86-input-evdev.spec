#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-input-evdev
Version  : 2.10.0
Release  : 7
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-2.10.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-2.10.0.tar.gz
Summary  : X.Org evdev input driver.
Group    : Development/Tools
License  : MIT
Requires: xf86-input-evdev-lib
Requires: xf86-input-evdev-data
Requires: xf86-input-evdev-doc
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mtdev)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)

%description
xf86-input-evdev - Generic Linux input driver for the Xorg X server
Please submit bugs & patches to the Xorg bugzilla:

%package data
Summary: data components for the xf86-input-evdev package.
Group: Data

%description data
data components for the xf86-input-evdev package.


%package dev
Summary: dev components for the xf86-input-evdev package.
Group: Development
Requires: xf86-input-evdev-lib
Requires: xf86-input-evdev-data
Provides: xf86-input-evdev-devel

%description dev
dev components for the xf86-input-evdev package.


%package doc
Summary: doc components for the xf86-input-evdev package.
Group: Documentation

%description doc
doc components for the xf86-input-evdev package.


%package lib
Summary: lib components for the xf86-input-evdev package.
Group: Libraries
Requires: xf86-input-evdev-data

%description lib
lib components for the xf86-input-evdev package.


%prep
%setup -q -n xf86-input-evdev-2.10.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-evdev.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/evdev-properties.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/evdev_drv.so
