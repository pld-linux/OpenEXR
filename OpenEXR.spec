
Summary:	High dynamic-range (HDR) image file format 
Summary(pl):	TODO
Name:		OpenEXR
Version:	1.1.0
Release:	0.1
License:	Industrial Light & Magic
Group:		Libraries
Source0:	http://www.openexr.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	716e74c740ef23433ef24bb515afb14f
URL:		http://www.openexr.com/
BuildRequires:	fltk-gl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.
OpenEXR is used by ILM on all motion pictures currently in production.
The first movies to employ OpenEXR were Harry Potter and the Sorcerers Stone,
Men in Black II, Gangs of New York, and Signs. Since then, OpenEXR has become
ILM's main image file format. 

%description -l pl
TODO.

%package devel
Summary:	TODO
Summary(pl):	TODO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
TODO.

%description devel -l pl
TODO

%package static
Summary:	TODO
Summary(pl):	TODO
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
TODO.

%description static
TODO

%package progs
Summary:	TODO
Summary(pl):	TODO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
TODO.

%description progs
TODO

%prep
%setup -q

%build
cp /usr/share/automake/config.sub admin

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
%{_includedir}/%{name}
%{_libdir}/lib*.la
%{_libdir}/lib*.so
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
Revision 1.1  2004-03-15 19:56:59  adgor
- Initial
