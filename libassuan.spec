%define version 1.0.2
%define rel 1
%define release %mkrel %rel

%define libname %mklibname assuan

Summary:	Assuan - an IPC library for non-persistent servers
Name:		libassuan
Version:	%{version}
Release:	%{release}
License:	LGPLv3
Group:		System/Libraries
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnupg.org/gcrypt/alpha/%{name}/%{name}-%{version}.tar.bz2.sig
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires: libpth-devel
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to separated it out to a standalone library.

%package -n %{libname}-devel
Summary:	Header files and static library for assuan
Group:		Development/C
Provides:	libassuan-devel = %{version}-%{release}
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
Obsoletes: %{libname}0-devel < 1.0.1

%description -n %{libname}-devel
Header files and static library for assuan.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure \
	--with-pth-prefix=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/libassuan-config
%endif

%clean
rm -rf %{buildroot}

%post -n %{libname}-devel
%_install_info assuan.info

%preun -n %{libname}-devel
%_remove_install_info assuan.info

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS README
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/libassuan-config
%endif
%{_bindir}/libassuan-config
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%{_infodir}/*.info*
%{_libdir}/lib*.a


