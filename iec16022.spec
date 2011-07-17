#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Library for producing 2D barcodes (known as Data Matrix)
Summary(pl.UTF-8):	Biblioteka do tworzenia kodów kreskowych 2D (znanych jako DataMatrix)
Name:		iec16022
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://datenfreihafen.org/~stefan/iec16022/%{name}-%{version}.tar.gz
# Source0-md5:	9395108f1deaa2c4bd6d05a9e7c91431
URL:		http://datenfreihafen.org/projects/iec16022.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iec16022 is a library for producing 2D barcodes, known as Data Matrix,
defined in ISO/IEC 16022.

%description -l pl.UTF-8
iec16022 jest biblioteką do tworzenia kodów kreskowych 2D, znanych
jako DataMatrix, zdefiniowanych w standardzie ISO/IEC 16022.

%package devel
Summary:	Header files for iec16022 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki iec16022
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for iec16022 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki iec16022.

%package static
Summary:	Static iec16022 library
Summary(pl.UTF-8):	Statyczna biblioteka iec16022
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static iec16022 library.

%description static -l pl.UTF-8
Statyczna biblioteka iec16022.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/iec16022
%attr(755,root,root) %{_libdir}/libiec16022.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiec16022.so.0
%{_mandir}/man1/iec16022.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiec16022.so
# keep .la as there is no Libs.private in pkgconfig file
%{_libdir}/libiec16022.la
%{_includedir}/iec16022
%{_pkgconfigdir}/libiec16022.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libiec16022.a
%endif
