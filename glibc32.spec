%define debug_package %{nil}
Summary: The GNU libc 32-bit libraries.
Name: glibc32
Version: 2.11.1
Release: 2.R
License: LGPL
Group: System Environment/Libraries
Source: http://download.rfremix.ru/storage/glibc32/glibc32-%{version}-%{release}.tar.bz2
Buildroot: %{_tmppath}/glibc-%{PACKAGE_VERSION}-root
ExclusiveArch: x86_64 ppc64

%description
The glibc package contains standard libraries which are used by
multiple programs on the system. In order to save disk space and
memory, as well as to make upgrading easier, common system code is
kept in one place and shared between programs. This particular package
contains the most important sets of shared libraries: the standard C
library and the standard math library. Without these two libraries, a
Linux system will not function.

%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cp -a %{_target_cpu}/* $RPM_BUILD_ROOT/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
/lib/*
/usr/lib/*
/usr/include/*

%changelog
* Sat Jan 12 2013 Arkady L. Shane <ashejn@russianfedora.ru>
- added libstdc++

* Fri Feb 24 2012 Arkady L. Shane <ashejn@russianfedora.ru>
- added zlib and libgcc files

* Thu Jan 28 2010 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.11.1-1 and nss-softokn-3.12.4-10.fc12

* Tue Jul 11 2006 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.4.90-13

* Sat Feb  4 2006 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.90-36

* Wed Feb 16 2005 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.4-10
  - also include /usr/include/gnu/stubs-32.h

* Fri Oct 15 2004 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.3-68

* Thu Jan 22 2004 Jakub Jelinek <jakub@redhat.com>
- updated from glibc-2.3.3-4

* Tue Apr 15 2003 Elliot Lee <sopwith@redhat.com>
- Update, add ppc64, cleanup install section

* Tue Mar  4 2003 Jakub Jelinek <jakub@redhat.com>
- update

* Sun Nov 10 2002 Jakub Jelinek <jakub@redhat.com>
- temporary package
