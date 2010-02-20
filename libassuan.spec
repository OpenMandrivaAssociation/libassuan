%define version 2.0.0
%define release %mkrel 4

%define libname %mklibname assuan

Summary:	Assuan - an IPC library for non-persistent servers
Name:		libassuan
Version:	%{version}
Release:	%{release}
License:	LGPLv3
Group:		System/Libraries
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	libpth-devel
BuildRequires:	%{_lib}gpg-error-devel
Provides:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to separated it out to a standalone library.

%package -n %{libname}-devel
Summary:	Header files and static library for assuan
Group:		Development/C
Provides:	libassuan-devel = %{version}-%{release}
Requires:	libassuan >= %{version}-%{release}
Requires:	libpth-devel
Requires(post):  info-install
Requires(preun): info-install
Obsoletes: %{libname}0-devel < 1.0.4
Obsoletes: %{libname}0-static-devel < 1.0.4

%description -n %{libname}-devel
Header files and static library for assuan.

%prep
%setup -q

%build
%configure2_5x \
	--with-pic \
	--enable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libassuan-config

%clean
rm -rf %{buildroot}

%post -n %{libname}-devel
%_install_info assuan.info

%preun -n %{libname}-devel
%_remove_install_info assuan.info

%files
%doc ChangeLog AUTHORS NEWS README
%{_libdir}/libassuan.so.*
%{_infodir}/*.info*

%files -n %{libname}-devel
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/libassuan-config
%{_bindir}/libassuan-config
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%{_libdir}/libassuan.so
%{_libdir}/libassuan.la
%{_libdir}/libassuan.a
