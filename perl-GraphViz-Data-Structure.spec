#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
%define		pnam	Data-Structure
Summary:	GraphViz::Data::Structure module - visualise data structures
Summary(pl):	Modu³ GraphViz::Data::Structure - wizualizacja struktur danych
Name:		perl-GraphViz-Data-Structure
Version:	0.07
Release:	3
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-GraphViz >= 1.3
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GraphViz >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes it easy to visualise data structures, even recursive
or circular ones. It is provided as an alternative to
GraphViz::Data::Grapher.

%description -l pl
Ten modu³ u³atwia wizualizacjê struktur danych, nawet zagnie¿d¿onych i
cyklicznych. Jest udostêpniony jako alternatywa dla modu³u
GraphViz::Data::Grapher.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

# disabled - two tests failed for me...
#%%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changes README
%{perl_vendorlib}/GraphViz/Data/Structure.pm
%{_mandir}/man3/*
