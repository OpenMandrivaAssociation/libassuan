%define major 0
%define libname %mklibname assuan %{major}
%define devname %mklibname assuan -d

Summary:	Assuan - an IPC library for non-persistent servers
Name:		libassuan
Version:	2.5.5
Release:	1
License:	LGPLv3
Group:		System/Libraries
Url:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	hostname

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

%prep
%autosetup -p1

%build
%configure \
	--with-pic \
	--enable-static

%make_build

%install
%make_install

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
%{_infodir}/*.info*
