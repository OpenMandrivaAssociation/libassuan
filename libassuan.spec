%define major 0

%define libname %mklibname assuan %{major}
%define develname %mklibname assuan -d

Summary:	Assuan - an IPC library for non-persistent servers
Name:		libassuan
Version:	2.0.3
Release:	2
License:	LGPLv3
Group:		System/Libraries
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	libpth-devel
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
Requires:	libpth-devel
Requires(post):	info-install
Requires(preun):	info-install
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

%post -n %{develname}
%_install_info assuan.info

%preun -n %{develname}
%_remove_install_info assuan.info

%files -n %{libname}
%{_libdir}/libassuan.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS README
%{multiarch_bindir}/libassuan-config
%{_bindir}/libassuan-config
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so
%{_libdir}/libassuan.la
%{_libdir}/libassuan.a
%{_infodir}/*.info*
