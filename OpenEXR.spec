Summary:	High dynamic-range (HDR) image file format support libraries
Summary(pl.UTF-8):	Biblioteki obsługujące format plików obrazu o wysokiej dynamice (HDR)
Name:		OpenEXR
Version:	3.1.12
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/AcademySoftwareFoundation/openexr/releases
Source0:	https://github.com/AcademySoftwareFoundation/openexr/archive/v%{version}/openexr-%{version}.tar.gz
# Source0-md5:	c1289f32d5de63934ed7cf2f124e45be
URL:		https://openexr.com/
BuildRequires:	Imath-devel >= 3.1
BuildRequires:	cmake >= 3.12
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	pkgconfig
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx_press_theme
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sphinx-pdg >= 2
BuildRequires:	zlib-devel
Obsoletes:	ilmbase < 3
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
Requires:	Imath-devel >= 3.1
Requires:	libstdc++-devel >= 6:5
Requires:	zlib-devel
Provides:	ilmbase-devel = %{version}-%{release}
Obsoletes:	ilmbase-devel < 3

%description devel
Header files for OpenEXR libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OpenEXR.

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
BuildArch:	noarch

%description doc
OpenEXR documentation describing file format, library etc.

%description doc -l pl.UTF-8
Dokumentacja do OpenEXR, opisująca format pliku, bibliotekę itd.

%prep
%setup -q -n openexr-%{version}

%build
mkdir -p build
cd build
%cmake .. \
	-DBUILD_DOCS=ON \
	-DINSTALL_DOCS=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/examples

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.md CODEOWNERS LICENSE.md PATENTS README.md SECURITY.md
%attr(755,root,root) %{_libdir}/libIex-3_1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIex-3_1.so.30
%attr(755,root,root) %{_libdir}/libIlmThread-3_1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmThread-3_1.so.30
%attr(755,root,root) %{_libdir}/libOpenEXR-3_1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenEXR-3_1.so.30
%attr(755,root,root) %{_libdir}/libOpenEXRCore-3_1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenEXRCore-3_1.so.30
%attr(755,root,root) %{_libdir}/libOpenEXRUtil-3_1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenEXRUtil-3_1.so.30

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIex*.so
%attr(755,root,root) %{_libdir}/libIlmThread*.so
%attr(755,root,root) %{_libdir}/libOpenEXR*.so
%{_includedir}/OpenEXR
%{_pkgconfigdir}/OpenEXR.pc
%{_libdir}/cmake/OpenEXR

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exrenvmap
%attr(755,root,root) %{_bindir}/exrheader
%attr(755,root,root) %{_bindir}/exrmakepreview
%attr(755,root,root) %{_bindir}/exrmaketiled
%attr(755,root,root) %{_bindir}/exrmultipart
%attr(755,root,root) %{_bindir}/exrmultiview
%attr(755,root,root) %{_bindir}/exrstdattr
%attr(755,root,root) %{_bindir}/exr2aces
%attr(755,root,root) %{_bindir}/exrinfo

%files doc
%defattr(644,root,root,755)
%doc build/docs/sphinx/{_images,_static,*.html,*.js}
