%define major 0

%define libname %mklibname assuan %{major}
%define develname %mklibname assuan -d

Summary:	Assuan - an IPC library for non-persistent servers
Name:		libassuan
Version:	2.0.3
Release:	4
License:	LGPLv3
Group:		System/Libraries
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	pth-devel
BuildRequires:	libgpg-error-devel

%description
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to separated it out to a standalone library.

%package -n %{libname}
Summary:	An IPC library for non-persistent servers
Group:		System/Libraries
Obsoletes:	libassuan < 2.0.0-4
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to separated it out to a standalone library.

%package -n %{develname}
Summary:	Header files and static library for assuan
Group:		Development/C
Provides:	libassuan-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	pth-devel
Obsoletes:	%{libname}0-devel < 1.0.4
Obsoletes:	%{libname}0-static-devel < 1.0.4

%description -n %{develname}
Header files and static library for assuan.

%prep
%setup -q

%build
%configure2_5x \
	--with-pic \
	--enable-static
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libassuan-config

%files -n %{libname}
%{_libdir}/libassuan.so.%{major}*

%files -n %{develname}
%doc ChangeLog AUTHORS NEWS README
%{multiarch_bindir}/libassuan-config
%{_bindir}/libassuan-config
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so
%{_libdir}/libassuan.a
%{_infodir}/*.info*


%changelog
* Thu Jun 14 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.3-3
+ Revision: 805567
- Drop some legacy junk

* Sun Feb 12 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 2.0.3-2
+ Revision: 773529
- rebuild for updated libtool .la file references..

* Tue Dec 27 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.0.3-1
+ Revision: 745525
- version update 2.0.3

* Tue Jul 05 2011 Lonyai Gergely <aleph@mandriva.org> 2.0.2-1
+ Revision: 688722
- 2.0.2

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 2.0.1-2
+ Revision: 660596
- fix multiarch usage

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Aug 15 2010 Emmanuel Andry <eandry@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 570206
- New version 2.0.1

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.0-4mdv2010.1
+ Revision: 508847
- apply a library policy here
- protect major
- obsolete old library
- enable build of static library

  + Lonyai Gergely <aleph@mandriva.org>
    - (re)fix libgpg-error-devel

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.1
+ Revision: 489637
- fix BR

  + Lonyai Gergely <aleph@mandriva.org>
    - Add new dependency libgpg-error
    - 2.0.0

* Sun Aug 10 2008 Emmanuel Andry <eandry@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 270354
- New version

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 1.0.4-1mdv2008.1
+ Revision: 120427
- New version
- drop obsoleted mdkversion conditionnals

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.0
+ Revision: 70305
- kill file require on info-install

* Sun Jul 22 2007 Funda Wang <fwang@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 54430
- Obsoletes old static-devel

* Fri Jul 06 2007 Andreas Hasenack <andreas@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 49174
- updated to version 1.0.2
- updated license tag to LGPLv3


* Wed Nov 29 2006 Andreas Hasenack <andreas@mandriva.com> 1.0.1-2mdv2007.0
+ Revision: 88682
- make double sure we use pth
- enabled pth support

* Wed Nov 29 2006 Andreas Hasenack <andreas@mandriva.com> 1.0.1-1mdv2007.1
+ Revision: 88652
- work on x86_64 provides/requires/obsoletes/names
- updated to version 1.0.1
- drop dynamic library patch, follow upstream which only
  has a static one
- rearranged packaging because of the above
- Import libassuan

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.6.10-2mdk
- Rebuild

* Wed Aug 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.10-1mdk
- New release 0.6.10

* Wed Jun 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.9-1mdk 
- new release

* Sat Apr 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.6.8-2mdk
- fix deps and conditional %%multiarch
- fix requires-on-release

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrake.org> 0.6.8-1mdk
- New release 0.6.8

* Thu Aug 19 2004 Abel Cheung <deaddog@mandrakesoft.com> 0.6.6-1mdk
- New release 0.6.6

* Fri May 21 2004 Abel Cheung <deaddog@deaddog.org> 0.6.5-1mdk
- New version
- Drop old patch1, use autoreconf instead
- Patch1: No m4 dir in source, remove such reference in Makefile.am,
  otherwise autoreconf won't work

* Sat Jan 24 2004 Abel Cheung <deaddog@deaddog.org> 0.6.2-1mdk
- New version

* Fri Jan 23 2004 Abel Cheung <deaddog@deaddog.org> 0.6.1-2mdk
- Revert many stuff back
- Remove patch1 (info)
- New Patch1: fix configure script generated by autoconf > 2.57
- Add back info files
- Include file signature

* Thu Dec 11 2003 Abel Cheung <deaddog@deaddog.org> 0.6.1-1mdk
- 0.6.1
- (mistakenly overwritten Florin's package)

