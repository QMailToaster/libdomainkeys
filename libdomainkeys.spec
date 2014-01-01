Name:      libdomainkeys
Summary:   DomainKey library
Version:   0.69
Release:   0%{?dist}
License:   Yahoo! DomainKeys Public License
Group:	   System Environment/Libraries
Vendor:    QmailToaster
Packager:  Eric Shubert <qmt-build@datamatters.us>
URL:       http://domainkeys.sourceforge.net/
Source0:   http://downloads.sourceforge.net/project/domainkeys/%{name}/0.69/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel
Obsoletes: libdomainkeys-toaster
BuildRoot: %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%define debug_package %{nil}

#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
DomainKey Implementor's library.

#-------------------------------------------------------------------------------
%package -n %{name}-devel
#-------------------------------------------------------------------------------
Summary:	DomainKey library development
Group:		System Environment/Libraries
Provides:	libdomainkeys-static = %{version}-%{release}

%description -n %{name}-devel
Headers and libraries for building packages which use the DomainKey library.

#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q

perl -pi -e's/CFLAGS=/CFLAGS=%{optflags} -fPIC /' Makefile
echo -- "-lresolv" > dns.lib

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

make UNAME=Linux

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
rm -rf %{buildroot}

# install directories
#-------------------------------------------------------------------------------
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}

# install files
#-------------------------------------------------------------------------------
install -p domainkeys.h \
           dktrace.h        %{buildroot}%{_includedir}
install -p libdomainkeys.a  %{buildroot}%{_libdir}
install -p dknewkey dktest  %{buildroot}%{_bindir}

#-------------------------------------------------------------------------------
%clean
#-------------------------------------------------------------------------------
rm -rf %{buildroot}

#-------------------------------------------------------------------------------
%files -n %{name}-devel
#-------------------------------------------------------------------------------
%defattr(-,root,root,-)
%doc README CHANGES *.html
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libdomainkeys.a

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Fri Nov 15 2013 Eric Shubert <eric@datamatters.us> 0.69-0.qt
- Migrated to github
- Removed -toaster designation
- Added CentOS 6 support
- Removed unsupported cruft
- Updated to upstream version
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 0.68-1.3.6
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Tue Jun 02 2009 Jake Vickers <jake@qmailtoaster.com> 0.68-1.3.6
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 0.68-1.3.5
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 0.68-1.3.4
- Added Suse 11.1 support
* Sun Feb 08 2009 Jake Vickers <jake@qmailtoaster.com> 0.68-1.3.4
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 0.68-1.3.3
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.68-1.3.2
- Added Fedora Core 6 support
* Fri Jun 02 2006 Nick Hemmesch <nick@ndhsoft.com> 0.68-1.3.1
- Make compatible with all supported distros
- Add SuSE 10.1 support
* Sun May 07 2006 Nick Hemmesch <nick@ndhsoft.com> 0.68-1.0.1
- Initial build
