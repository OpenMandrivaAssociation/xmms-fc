%define version 0.5.4
%define release %mkrel 3

Name: xmms-fc
Summary: Future Composer plugin for XMMS
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Sound
URL: http://xmms-fc.sourceforge.net/
Source:	http://prdownloads.sourceforge.net/xmms-fc/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxmms-devel
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
rm -f %buildroot%{_libdir}/xmms/Input/libfc.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README src/FC.README ChangeLog
%{_libdir}/xmms/Input/libfc.so


