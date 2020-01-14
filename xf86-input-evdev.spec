#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-input-evdev
Version  : 2.10.6
Release  : 36
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-2.10.6.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-2.10.6.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-2.10.6.tar.gz.sig
Summary  : X.org evdev input driver
Group    : Development/Tools
License  : MIT
Requires: xf86-input-evdev-data = %{version}-%{release}
Requires: xf86-input-evdev-lib = %{version}-%{release}
Requires: xf86-input-evdev-license = %{version}-%{release}
Requires: xf86-input-evdev-man = %{version}-%{release}
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mtdev)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

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
Requires: xf86-input-evdev-lib = %{version}-%{release}
Requires: xf86-input-evdev-data = %{version}-%{release}
Provides: xf86-input-evdev-devel = %{version}-%{release}
Requires: xf86-input-evdev = %{version}-%{release}

%description dev
dev components for the xf86-input-evdev package.


%package lib
Summary: lib components for the xf86-input-evdev package.
Group: Libraries
Requires: xf86-input-evdev-data = %{version}-%{release}
Requires: xf86-input-evdev-license = %{version}-%{release}

%description lib
lib components for the xf86-input-evdev package.


%package license
Summary: license components for the xf86-input-evdev package.
Group: Default

%description license
license components for the xf86-input-evdev package.


%package man
Summary: man components for the xf86-input-evdev package.
Group: Default

%description man
man components for the xf86-input-evdev package.


%prep
%setup -q -n xf86-input-evdev-2.10.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557104996
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557104996
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-input-evdev
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-input-evdev/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-evdev.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/evdev-properties.h
/usr/lib64/pkgconfig/xorg-evdev.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/evdev_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-input-evdev/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/evdev.4
