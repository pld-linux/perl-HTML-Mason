#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Mason
Summary:	Mason - High-performance, dynamic web site authoring system
Summary(pl):	Mason - Wysokowydajny system do tworzenia dynamicznych stron WWW
Name:		perl-HTML-Mason
Version:	1.15
Release:	1
Epoch:		3
License:	GPL/Artistic
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl-Cache-Cache >= 1.0
BuildRequires:	perl-Class-Container >= 0.07
BuildRequires:	perl-Exception-Class >= 1.01
BuildRequires:	perl-Params-Validate >= 0.24
BuildRequires:	perl-HTML-Parser
%endif
Requires:	perl(File::Spec) >= 0.8
Requires:	perl-Class-Container >= 0.07
Requires:	perl-Exception-Class >= 1.01
Requires:	perl-Params-Validate >= 0.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Cache::Cache)' 'perl(HTML::Mason::Exceptions()' 'perl(HTML::Mason::MethodMaker(read_write)'

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
perl Makefile.PL --no-prompts
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_sitelib}/HTML/Mason/*.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf samples/README
cp -a {samples,eg} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv bin contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README UPGRADE CREDITS contrib install
%{perl_sitelib}/Apache/Mason.pm
%{perl_sitelib}/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/eg
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/eg/*.pl
%{_examplesdir}/%{name}-%{version}/eg/httpd.conf
%{_examplesdir}/%{name}-%{version}/samples
%{_mandir}/man3/HTML*
