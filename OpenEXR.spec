#
# Conditional build:
%bcond_without	apidocs		# API documentation in HTML format
%bcond_without	python3		# CPython 3.x bindings
%bcond_with	tbb		# TBB threading in IlmThreadPool

Summary:	High dynamic-range (HDR) image file format support libraries
Summary(pl.UTF-8):	Biblioteki obsługujące format plików obrazu o wysokiej dynamice (HDR)
Name:		OpenEXR
Version:	3.4.4
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/AcademySoftwareFoundation/openexr/releases
Source0:	https://github.com/AcademySoftwareFoundation/openexr/archive/v%{version}/openexr-%{version}.tar.gz
# Source0-md5:	ad8587c4a64bf423c387734e85d17432
URL:		https://openexr.com/
BuildRequires:	Imath-devel >= 3.1
BuildRequires:	cmake >= 3.17
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	help2man
BuildRequires:	libdeflate-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	openjph-devel >= 0.21.0
BuildRequires:	pkgconfig
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-numpy-devel >= 1.7.0
BuildRequires:	python3-pybind11
%endif
%{?with_apidocs:BuildRequires:	python3-breathe}
%{?with_apidocs:BuildRequires:	python3-sphinx_press_theme}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
%{?with_apidocs:BuildRequires:	sphinx-pdg >= 2}
%{?with_tbb:BuildRequires:	tbb-devel}
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
Requires:	libdeflate-devel
Requires:	libstdc++-devel >= 6:7
Requires:	openjph-devel >= 0.21.0
Requires:	zlib-devel
Provides:	ilmbase-devel = %{version}-%{release}
Obsoletes:	OpenEXR-static < 3
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

%package -n python3-OpenEXR
Summary:	Python bindings for OpenEXR library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki OpenEXR
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-numpy >= 1.7.0

%description -n python3-OpenEXR
Python bindings for OpenEXR library.

%description -n python3-OpenEXR -l pl.UTF-8
Wiązania Pythona do biblioteki OpenEXR.

%prep
%setup -q -n openexr-%{version}

%build
%cmake -B build \
	%{?with_apidocs:-DBUILD_WEBSITE=ON} \
	-DOPENEXR_INSTALL_DOCS=ON \
	%{?with_tbb:-DOPENEXR_USE_TBB=ON} \
%if %{with python3}
	-DOPENEXR_BUILD_PYTHON=ON \
	-DSKBUILD=ON \
	-DSKBUILD_PLATLIB_DIR=%{py3_sitedir}
%endif

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/examples

%if %{with python3}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.md CODEOWNERS LICENSE.md PATENTS README.md SECURITY.md
%{_libdir}/libIex-3_4.so.*.*.*
%ghost %{_libdir}/libIex-3_4.so.33
%{_libdir}/libIlmThread-3_4.so.*.*.*
%ghost %{_libdir}/libIlmThread-3_4.so.33
%{_libdir}/libOpenEXR-3_4.so.*.*.*
%ghost %{_libdir}/libOpenEXR-3_4.so.33
%{_libdir}/libOpenEXRCore-3_4.so.*.*.*
%ghost %{_libdir}/libOpenEXRCore-3_4.so.33
%{_libdir}/libOpenEXRUtil-3_4.so.*.*.*
%ghost %{_libdir}/libOpenEXRUtil-3_4.so.33

%files devel
%defattr(644,root,root,755)
%{_libdir}/libIex*.so
%{_libdir}/libIlmThread*.so
%{_libdir}/libOpenEXR*.so
%{_includedir}/OpenEXR
%{_pkgconfigdir}/OpenEXR.pc
%{_libdir}/cmake/OpenEXR

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exrmanifest
%attr(755,root,root) %{_bindir}/exrmetrics
%attr(755,root,root) %{_bindir}/exrenvmap
%attr(755,root,root) %{_bindir}/exrheader
%attr(755,root,root) %{_bindir}/exrmakepreview
%attr(755,root,root) %{_bindir}/exrmaketiled
%attr(755,root,root) %{_bindir}/exrmultipart
%attr(755,root,root) %{_bindir}/exrmultiview
%attr(755,root,root) %{_bindir}/exrstdattr
%attr(755,root,root) %{_bindir}/exr2aces
%attr(755,root,root) %{_bindir}/exrinfo
%{_mandir}/man1/exr2aces.1*
%{_mandir}/man1/exrcheck.1*
%{_mandir}/man1/exrenvmap.1*
%{_mandir}/man1/exrheader.1*
%{_mandir}/man1/exrinfo.1*
%{_mandir}/man1/exrmakepreview.1*
%{_mandir}/man1/exrmaketiled.1*
%{_mandir}/man1/exrmanifest.1*
%{_mandir}/man1/exrmetrics.1*
%{_mandir}/man1/exrmultipart.1*
%{_mandir}/man1/exrmultiview.1*
%{_mandir}/man1/exrstdattr.1*

%if %{with apidocs}
%files doc
%defattr(644,root,root,755)
%doc build/website/sphinx/{_downloads,_images,_static,bin,test_images,*.html,*.js}
%endif

%if %{with python3}
%files -n python3-OpenEXR
%defattr(644,root,root,755)
%{py3_sitedir}/Imath.py
%{py3_sitedir}/OpenEXR.cpython-*.so
%{py3_sitedir}/__pycache__/Imath.cpython-*.py[co]
%endif
