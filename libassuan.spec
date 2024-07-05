%define major 9
%define libname %mklibname assuan
%define devname %mklibname assuan -d

Summary:	Assuan - an IPC library for non-persistent servers
Name:		libassuan
Version:	3.0.1
Release:	1
License:	LGPLv3
Group:		System/Libraries
Url:		https://www.gnupg.org/
Source0:	https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	hostname
BuildSystem:	autotools
BuildOption:	--with-pic
BuildOption:	--enable-static

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

%package -n %{devname}
Summary:	Header files and static library for assuan
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files and static library for assuan.

%files -n %{libname}
%{_libdir}/libassuan.so.%{major}*

%files -n %{devname}
%doc ChangeLog AUTHORS NEWS README
%{_bindir}/libassuan-config
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so
%{_libdir}/libassuan.a
%{_libdir}/pkgconfig/libassuan.pc
%doc %{_infodir}/*.info*
