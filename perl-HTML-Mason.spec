#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Mason
Summary:	Mason Perl module - high-performance, dynamic web site authoring system
Summary(pl):	Modu³ Perla Mason - wysokowydajny system do tworzenia dynamicznych stron WWW
Name:		perl-HTML-Mason
Version:	1.33
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22c2cd76ed068630708175d570f97277
URL:		http://www.masonhq.com/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl(Scalar::Util) >= 1.01
BuildRequires:	perl-CGI >= 2.46
BuildRequires:	perl-Cache-Cache >= 1.0
BuildRequires:	perl-Class-Container >= 0.07
BuildRequires:	perl-Exception-Class >= 1.14
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Params-Validate >= 0.70
%endif
Requires:	perl(File::Spec) >= 0.8
Requires:	perl-Class-Container >= 0.07
Requires:	perl-Exception-Class >= 1.14
Requires:	perl-Params-Validate >= 0.70
Conflicts:	perl-Apache-Filter < 1.021
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Cache::Cache)' 'perl(HTML::Mason::Exceptions()' 'perl(HTML::Mason::MethodMaker(read_write)' 'perl(Apache)' 'perl(Apache::Constants)'

%description
Mason is a tool for building, serving and managing large web sites.
Its features make it an ideal backend for high load sites serving
dynamic content, such as online newspapers or database driven
e-commerce sites.

%description -l pl
Mason jest narzêdziem s³u¿±cym do budowania i udostêpniania du¿ych
serwisów WWW oraz do zarz±dzania nimi. Ze wzglêdu na swe mo¿liwo¶ci,
jest idealn± baz± dla du¿ych serwisów o dynamicznie generowanej
zawarto¶ci, np. gazet internetowych czy sklepów internetowych opartych
na bazach danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/MasonX

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/Mason/*.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf samples/README
cp -a {samples,eg} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv bin contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README UPGRADE CREDITS contrib
%{perl_vendorlib}/Bundle/HTML/Mason.pm
%{perl_vendorlib}/Apache/Mason.pm
%{perl_vendorlib}/HTML/Mason.pm
%{perl_vendorlib}/HTML/Mason
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/HTML*
%{_mandir}/man3/Bundle*
%{perl_vendorlib}/MasonX
