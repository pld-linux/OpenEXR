Summary:	High dynamic-range (HDR) image file format support libraries
Summary(pl.UTF-8):	Biblioteki obsługujące format plików obrazu o wysokiej dynamice (HDR)
Name:		OpenEXR
Version:	2.5.8
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/AcademySoftwareFoundation/openexr/releases
Source0:	https://github.com/AcademySoftwareFoundation/openexr/archive/v%{version}/openexr-%{version}.tar.gz
# Source0-md5:	92d87a37660d054516a4a7b10d91dfe7
Patch0:		%{name}-python-install.patch
URL:		https://openexr.com/
BuildRequires:	boost-python-devel
BuildRequires:	boost-python3-devel
BuildRequires:	cmake >= 3.12
BuildRequires:	ilmbase-devel >= 2.3.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numpy-devel
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-numpy-devel
BuildRequires:	zlib-devel
Requires:	ilmbase = %{version}-%{release}
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
Requires:	ilmbase-devel >= 2.3.0
Requires:	libstdc++-devel >= 6:5
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

%package -n ilmbase
Summary:	IlmBase - base math and exception libraries from OpenEXR project
Summary(pl.UTF-8):	IlmBase - podstawowe biblioteki matematyczne i wyjątków z projektu OpenEXR
Group:		Libraries

%description -n ilmbase
IlmBase consists of the following libraries:

Half is a class that encapsulates our 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%description -n ilmbase -l pl.UTF-8
IlmBase składa się z następujących bibliotek:

Half to klasa obudowująca 16-bitowy format zmiennoprzecinkowy.

IlmThread to biblioteka abstrakcji wątków przeznaczona dla OpenEXR i
innych pakietów oprogramowania. Aktualnie obsługuje standard pthreads
oraz wątki Windows.

Imath implementuje wektory 2D i 3D, macierze 3x3 i 4x4, kwaterniony i
inne przydatne funkcje matematyczne 2D i 3D.

Iex to biblioteka obsługi wyjątków.

%package -n ilmbase-devel
Summary:	Header files for IlmBase libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek IlmBase
Group:		Development/Libraries
Requires:	ilmbase = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5
Conflicts:	OpenEXR-devel < 1.5.0

%description -n ilmbase-devel
Header files for IlmBase libraries.

%description -n ilmbase-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek IlmBase.

%package -n ilmbase-static
Summary:	Static IlmBase libraries
Summary(pl.UTF-8):	Statyczne biblioteki IlmBase
Group:		Development/Libraries
Requires:	ilmbase-devel = %{version}-%{release}
Conflicts:	OpenEXR-static < 1.5.0

%description -n ilmbase-static
Static IlmBase libraries.

%description -n ilmbase-static -l pl.UTF-8
Statyczne biblioteki IlmBase.

%package -n pyilmbase-devel
Summary:	Header files for IlmBase Python bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Pyhona do bibliotek IlmBase
Group:		Development/Libraries
Requires:	boost-python-devel
Requires:	ilmbase-devel = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5

%description -n pyilmbase-devel
Header files for IlmBase Python bindings.

%description -n pyilmbase-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Pyhona do bibliotek IlmBase.

%package -n python-pyilmbase
Summary:	Python 2 bindings for the IlmBase libraries
Summary(pl.UTF-8):	Wiązania Pythona 2 do bibliotek IlmBase
Group:		Libraries/Python
Requires:	ilmbase = %{version}-%{release}

%description -n python-pyilmbase
The PyIlmBase package provides python bindings for the IlmBase
libraries.

%description -n python-pyilmbase -l pl.UTF-8
Pakiet PyIlmBase dostarcza wiązania Pythona do bibliotek IlmBase.

%package -n python-pyilmbase-devel
Summary:	Development files for IlmBase Python 2 bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań IlmBase do Pythona 2
Group:		Development/Libraries
Requires:	pyilmbase-devel = %{version}-%{release}
Requires:	python-devel >= 1:2.5
Requires:	python-pyilmbase = %{version}-%{release}

%description -n python-pyilmbase-devel
Development files for IlmBase Python 2 bindings.

%description -n python-pyilmbase-devel -l pl.UTF-8
Pliki programistyczne wiązań IlmBase do Pythona 2.

%package -n python3-pyilmbase
Summary:	Python 3 bindings for the IlmBase libraries
Summary(pl.UTF-8):	Wiązania Pythona 3 do bibliotek IlmBase
Group:		Libraries/Python
Requires:	ilmbase = %{version}-%{release}

%description -n python3-pyilmbase
The PyIlmBase package provides python bindings for the IlmBase
libraries.

%description -n python3-pyilmbase -l pl.UTF-8
Pakiet PyIlmBase dostarcza wiązania Pythona do bibliotek IlmBase.

%package -n python3-pyilmbase-devel
Summary:	Development files for IlmBase Python 3 bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań IlmBase do Pythona 3
Group:		Development/Libraries
Requires:	pyilmbase-devel = %{version}-%{release}
Requires:	python3-devel >= 1:3.2
Requires:	python3-pyilmbase = %{version}-%{release}

%description -n python3-pyilmbase-devel
Development files for IlmBase Python 3 bindings.

%description -n python3-pyilmbase-devel -l pl.UTF-8
Pliki programistyczne wiązań IlmBase do Pythona 3.

%prep
%setup -q -n openexr-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DILMBASE_BUILD_BOTH_STATIC_SHARED=ON \
	-DOPENEXR_BUILD_BOTH_STATIC_SHARED=ON \
	-DPYILMBASE_OVERRIDE_PYTHON2_INSTALL_DIR=%{py_sitedir} \
	-DPYILMBASE_OVERRIDE_PYTHON3_INSTALL_DIR=%{py3_sitedir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/*.pdf
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/examples

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n ilmbase -p /sbin/ldconfig
%postun	-n ilmbase -p /sbin/ldconfig

%post	-n python-pyilmbase -p /sbin/ldconfig
%postun	-n python-pyilmbase -p /sbin/ldconfig

%post	-n python3-pyilmbase -p /sbin/ldconfig
%postun	-n python3-pyilmbase -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.md CONTRIBUTORS.md GOVERNANCE.md LICENSE.md README.md SECURITY.md OpenEXR/PATENTS
%attr(755,root,root) %{_libdir}/libIlmImf-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmImf-2_5.so.26
%attr(755,root,root) %{_libdir}/libIlmImfUtil-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmImfUtil-2_5.so.26

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIlmImf-2_5.so
%attr(755,root,root) %{_libdir}/libIlmImf.so
%attr(755,root,root) %{_libdir}/libIlmImfUtil-2_5.so
%attr(755,root,root) %{_libdir}/libIlmImfUtil.so
%{_includedir}/OpenEXR/Imf*.h
%{_includedir}/OpenEXR/OpenEXRConfig.h
%{_pkgconfigdir}/OpenEXR.pc
%{_libdir}/cmake/OpenEXR

%files static
%defattr(644,root,root,755)
%{_libdir}/libIlmImf-2_5_static.a
%{_libdir}/libIlmImfUtil-2_5_static.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exr2aces
%attr(755,root,root) %{_bindir}/exrenvmap
%attr(755,root,root) %{_bindir}/exrheader
%attr(755,root,root) %{_bindir}/exrmakepreview
%attr(755,root,root) %{_bindir}/exrmaketiled
%attr(755,root,root) %{_bindir}/exrmultipart
%attr(755,root,root) %{_bindir}/exrmultiview
%attr(755,root,root) %{_bindir}/exrstdattr

%files doc
%defattr(644,root,root,755)
%doc OpenEXR/doc/*.pdf

%files -n ilmbase
%defattr(644,root,root,755)
%doc IlmBase/README.md
%attr(755,root,root) %{_libdir}/libHalf-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libHalf-2_5.so.25
%attr(755,root,root) %{_libdir}/libIex-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIex-2_5.so.25
%attr(755,root,root) %{_libdir}/libIexMath-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIexMath-2_5.so.25
%attr(755,root,root) %{_libdir}/libIlmThread-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmThread-2_5.so.25
%attr(755,root,root) %{_libdir}/libImath-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libImath-2_5.so.25

%files -n ilmbase-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libHalf-2_5.so
%attr(755,root,root) %{_libdir}/libHalf.so
%attr(755,root,root) %{_libdir}/libIex-2_5.so
%attr(755,root,root) %{_libdir}/libIex.so
%attr(755,root,root) %{_libdir}/libIexMath-2_5.so
%attr(755,root,root) %{_libdir}/libIexMath.so
%attr(755,root,root) %{_libdir}/libIlmThread-2_5.so
%attr(755,root,root) %{_libdir}/libIlmThread.so
%attr(755,root,root) %{_libdir}/libImath-2_5.so
%attr(755,root,root) %{_libdir}/libImath.so
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/IlmBaseConfig.h
%{_includedir}/OpenEXR/IlmThread*.h
%{_includedir}/OpenEXR/Imath*.h
%{_includedir}/OpenEXR/half*.h
%{_pkgconfigdir}/IlmBase.pc
%{_libdir}/cmake/IlmBase

%files -n ilmbase-static
%defattr(644,root,root,755)
%{_libdir}/libHalf-2_5_static.a
%{_libdir}/libIex-2_5_static.a
%{_libdir}/libIexMath-2_5_static.a
%{_libdir}/libIlmThread-2_5_static.a
%{_libdir}/libImath-2_5_static.a

%files -n pyilmbase-devel
%defattr(644,root,root,755)
%{_includedir}/OpenEXR/PyIex*.h
%{_includedir}/OpenEXR/PyImath*.h
%{_pkgconfigdir}/PyIlmBase.pc
%{_libdir}/cmake/PyIlmBase

%files -n python-pyilmbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPyIex_Python2_*-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libPyIex_Python2_*-2_5.so.25
%attr(755,root,root) %{_libdir}/libPyImath_Python2_*-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libPyImath_Python2_*-2_5.so.25
%attr(755,root,root) %{py_sitedir}/iex.so
%attr(755,root,root) %{py_sitedir}/imath.so
%attr(755,root,root) %{py_sitedir}/imathnumpy.so

%files -n python-pyilmbase-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPyIex_Python2_*.so
%attr(755,root,root) %{_libdir}/libPyImath_Python2_*.so

%files -n python3-pyilmbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPyIex_Python3_*-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libPyIex_Python3_*-2_5.so.25
%attr(755,root,root) %{_libdir}/libPyImath_Python3_*-2_5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libPyImath_Python3_*-2_5.so.25
%attr(755,root,root) %{py3_sitedir}/iex.so
%attr(755,root,root) %{py3_sitedir}/imath.so
%attr(755,root,root) %{py3_sitedir}/imathnumpy.so

%files -n python3-pyilmbase-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPyIex_Python3_*.so
%attr(755,root,root) %{_libdir}/libPyImath_Python3_*.so
