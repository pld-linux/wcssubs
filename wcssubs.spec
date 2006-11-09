Summary:	WCSLIB - an implementation of the FITS WCS proposal
Summary(pl):	WCSLIB - implementacja propozycji standardu FITS WCS
Name:		wcssubs
Version:	3.4.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://cfa-ftp.harvard.edu/pub/gsc/SAOimage/%{name}-%{version}.tar.gz
# Source0-md5:	4a40caea6c222cd91fceeca8b61b4730
URL:		http://tdc-www.harvard.edu/software/wcstools/libwcs.wcs.html
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These subroutines, developed as part of the WCSTools software package,
constitute a self-contained package for accessing the world coordinate
systems of FITS or IRAF(.imh) images.

%description -l pl
Te funkcje, stworzone jako czê¶æ projektu WCSTools, tworz± samodzielny
pakiet s³u¿±cy do dostêpu do globalnych uk³adów wspó³rzêdnych (WCS -
world coordinate systems) w obrazach FITS lub IRAF (.imh).

%package devel
Summary:	Header files for WCS library
Summary(pl):	Pliki nag³ówkowe biblioteki WCS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for WCS library.

%description devel -l pl
Pliki nag³ówkowe biblioteki WCS.

%package static
Summary:	Static WCS library
Summary(pl):	Statyczna biblioteka WCS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WCS library.

%description static -l pl
Statyczna biblioteka WCS.

%prep
%setup -q

%build
%{__make} \
	CC="libtool --mode=compile %{__cc}" \
	CFLAGS="%{rpmcflags}"

libtool --mode=link %{__cc} %{rpmldflags} -o libwcs.la *.lo -rpath %{_libdir} -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/wcssubs}

libtool --mode=install install libwcs.la $RPM_BUILD_ROOT%{_libdir}
install fitsfile.h fitshead.h wcs.h wcslib.h $RPM_BUILD_ROOT%{_includedir}/wcssubs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Files NEWS Readme
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/wcssubs

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
