Summary:	High dynamic-range (HDR) image file format support libraries
Summary(pl):	Biblioteki obs³uguj±ce format plików obrazu o wysokiej dynamice (HDR)
Name:		OpenEXR
Version:	1.1.0
Release:	0.1
License:	Industrial Light & Magic
Group:		Libraries
Source0:	http://www.openexr.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	716e74c740ef23433ef24bb515afb14f
URL:		http://www.openexr.com/
BuildRequires:	automake
BuildRequires:	fltk-gl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.
OpenEXR is used by ILM on all motion pictures currently in production.
The first movies to employ OpenEXR were Harry Potter and the Sorcerers
Stone, Men in Black II, Gangs of New York, and Signs. Since then,
OpenEXR has become ILM's main image file format. 

%description -l pl
OpenEXR to format plików obrazu o wysokiej dynamice (HDR - High
Dynamic-Range) stworzony przez Industrial Light & Magic do u¿ywania w
aplikacjach do grafiki komputerowej. OpenEXR jest u¿ywany przez ILM do
wszystkich aktualnie produkowanych obrazów ruchomych. Pierwszymi
filmami wykorzystuj±cymi OpenEXR by³y Harry Potter and the Sorcerers
Stone, Men in Black II, Gangs of New York oraz Signs. Od tamtego czasu
OpenEXR sta³ siê g³ównym formatem obrazu ILM.

%package devel
Summary:	Header files for OpenEXR libraries
Summary(pl):	Pliki nag³ówkowe bibliotek OpenEXR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenEXR libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek OpenEXR.

%package static
Summary:	Static OpenEXR libraries
Summary(pl):	Statyczne biblioteki OpenEXR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenEXR libraries.

%description static
Statyczne biblioteki OpenEXR.

%package progs
Summary:	OpenEXR utilities
Summary(pl):	Narzêdzia do obrazów OpenEXR
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
OpenEXR utilities.

%description progs
Narzêdzia do obrazów OpenEXR.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}

%configure

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
%doc AUTHORS COPYING ChangeLog NEWS README ReleaseNotes
%attr(755,root,root) %{_libdir}/libHalf.so.*.*.*
%attr(755,root,root) %{_libdir}/libIex.so.*.*.*
%attr(755,root,root) %{_libdir}/libIlmImf.so.*.*.*
%attr(755,root,root) %{_libdir}/libImath.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_aclocaldir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exrdisplay
%attr(755,root,root) %{_bindir}/exrenvmap
%attr(755,root,root) %{_bindir}/exrheader
%attr(755,root,root) %{_bindir}/exrmakepreview
%attr(755,root,root) %{_bindir}/exrmaketiled
%attr(755,root,root) %{_bindir}/exrstdattr

%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: OpenEXR.spec,v $
Revision 1.2  2004-03-15 20:28:19  qboosh
- pl, cosmetics

Revision 1.1  2004/03/15 19:56:59  adgor
- Initial
