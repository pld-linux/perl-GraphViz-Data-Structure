#
# Conditional build:
%bcond_with	tests	# perform "make test" (one meaningless test fails)

%define		pdir	GraphViz
%define		pnam	Data-Structure
Summary:	GraphViz::Data::Structure module - visualise data structures
Summary(pl.UTF-8):	Moduł GraphViz::Data::Structure - wizualizacja struktur danych
Name:		perl-GraphViz-Data-Structure
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ba386e9052d3592c92b953742e18438
URL:		http://search.cpan.org/dist/GraphViz-Data-Structure/
BuildRequires:	perl-GraphViz >= 2.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GraphViz >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes it easy to visualise data structures, even recursive
or circular ones. It is provided as an alternative to
GraphViz::Data::Grapher.

%description -l pl.UTF-8
Ten moduł ułatwia wizualizację struktur danych, nawet zagnieżdżonych i
cyklicznych. Jest udostępniony jako alternatywa dla modułu
GraphViz::Data::Grapher.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changes README
%{perl_vendorlib}/GraphViz/Data/*.pm
%{_mandir}/man3/*
