Summary:	High dynamic-range (HDR) image file format support libraries
Summary(pl.UTF-8):	Biblioteki obsługujące format plików obrazu o wysokiej dynamice (HDR)
Name:		OpenEXR
Version:	2.2.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/openexr/openexr-%{version}.tar.gz
# Source0-md5:	b64e931c82aa3790329c21418373db4e
Patch0:		%{name}-build.patch
URL:		http://www.openexr.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
BuildRequires:	ilmbase-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	ilmbase >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.
OpenEXR is used by ILM on all motion pictures currently in production.
The first movies to employ OpenEXR were Harry Potter and the Sorcerers
Stone, Men in Black II, Gangs of New York, and Signs. Since then,
OpenEXR has become ILM's main image file format.

%description -l pl.UTF-8
OpenEXR to format plików obrazu o wysokiej dynamice (HDR - High
Dynamic-Range) stworzony przez Industrial Light & Magic do używania w
aplikacjach do grafiki komputerowej. OpenEXR jest używany przez ILM do
wszystkich aktualnie produkowanych obrazów ruchomych. Pierwszymi
filmami wykorzystującymi OpenEXR były Harry Potter and the Sorcerers
Stone, Men in Black II, Gangs of New York oraz Signs. Od tamtego czasu
OpenEXR stał się głównym formatem obrazu ILM.

%package devel
Summary:	Header files for OpenEXR libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OpenEXR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ilmbase-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
Header files for OpenEXR libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OpenEXR.

%package static
Summary:	Static OpenEXR libraries
Summary(pl.UTF-8):	Statyczne biblioteki OpenEXR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenEXR libraries.

%description static -l pl.UTF-8
Statyczne biblioteki OpenEXR.

%package progs
Summary:	OpenEXR utilities
Summary(pl.UTF-8):	Narzędzia do obrazów OpenEXR
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
OpenEXR utilities.

%description progs -l pl.UTF-8
Narzędzia do obrazów OpenEXR.

%package doc
Summary:	OpenEXR documentation
Summary(pl.UTF-8):	Dokumentacja do OpenEXR
Group:		Documentation

%description doc
OpenEXR documentation describing file format, library etc.

%description doc -l pl.UTF-8
Dokumentacja do OpenEXR, opisująca format pliku, bibliotekę itd.

%prep
%setup -q -n openexr-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# PDFs packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libIlmImf-2_2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmImf-2_2.so.22
%attr(755,root,root) %{_libdir}/libIlmImfUtil-2_2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmImfUtil-2_2.so.22

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIlmImf.so
%attr(755,root,root) %{_libdir}/libIlmImfUtil.so
%{_libdir}/libIlmImf.la
%{_libdir}/libIlmImfUtil.la
%{_includedir}/OpenEXR/Imf*.h
%{_includedir}/OpenEXR/OpenEXRConfig.h
%{_aclocaldir}/openexr.m4
%{_pkgconfigdir}/OpenEXR.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libIlmImf.a
%{_libdir}/libIlmImfUtil.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exrenvmap
%attr(755,root,root) %{_bindir}/exrheader
%attr(755,root,root) %{_bindir}/exrmakepreview
%attr(755,root,root) %{_bindir}/exrmaketiled
%attr(755,root,root) %{_bindir}/exrmultipart
%attr(755,root,root) %{_bindir}/exrmultiview
%attr(755,root,root) %{_bindir}/exrstdattr

%files doc
%defattr(644,root,root,755)
%doc doc/*.pdf
