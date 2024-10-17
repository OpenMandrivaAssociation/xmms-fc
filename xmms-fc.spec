%define version 0.6
%define release %mkrel 1

Name: xmms-fc
Summary: Future Composer plugin for XMMS
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Sound
URL: https://xmms-fc.sourceforge.net/
Source:	http://prdownloads.sourceforge.net/xmms-fc/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxmms-devel
BuildRequires: libfc14audiodecoder-devel
Requires: xmms

%description
This is an input plugin for XMMS which can play back Future Composer
music files from AMIGA.

%prep
%setup -q

%build
export CPPFLAGS=-DFC_HAVE_IOS_BINARY
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%{_libdir}/xmms/Input/fcdecoder.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_libdir}/xmms/Input/fcdecoder.so


