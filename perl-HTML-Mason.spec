%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Mason
Summary:	HTML::Mason Perl module
Summary(cs):	Modul HTML::Mason pro Perl
Summary(da):	Perlmodul HTML::Mason
Summary(de):	HTML::Mason Perl Modul
Summary(es):	M�dulo de Perl HTML::Mason
Summary(fr):	Module Perl HTML::Mason
Summary(it):	Modulo di Perl HTML::Mason
Summary(ja):	HTML::Mason Perl �⥸�塼��
Summary(ko):	HTML::Mason �� ����
Summary(no):	Perlmodul HTML::Mason
Summary(pl):	Modu� Perla HTML::Mason
Summary(pt):	M�dulo de Perl HTML::Mason
Summary(pt_BR):	M�dulo Perl HTML::Mason
Summary(ru):	������ ��� Perl HTML::Mason
Summary(sv):	HTML::Mason Perlmodul
Summary(uk):	������ ��� Perl HTML::Mason
Summary(zh_CN):	HTML::Mason Perl ģ��
Name:		perl-HTML-Mason
Version:	1.11
Release:	3
Epoch:		2
License:	GPL
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#Patch0:	%{name}-fix.patch
BuildRequires:	apache-mod_perl
BuildRequires:	perl >= 5.6
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl-Cache-Cache >= 1.0
BuildRequires:	perl-Class-Container >= 0.02
BuildRequires:	perl-Exception-Class >= 1.01
BuildRequires:	perl-Params-Validate >= 0.18
BuildRequires:	rpm-perlprov >= 3.0.3-26
Requires:	apache-mod_perl >= 1.22
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Apache::Request is in libapreq; it's needed only for Mason+mod_perl
# installation.  Next two are results of broken find-perl-requires.
%define		_noautoreq	'perl(Apache::Request)' 'perl(HTML::Mason::Exceptions()' 'perl(HTML::Mason::MethodMaker(read_write)'

%description
Mason is a tool for building, serving and managing large web sites. Its
features make it an ideal backend for high load sites serving dynamic
content, such as online newspapers or database driven e-commerce sites.

%description -l pl
Mason jest narz�dziem, s�u��cym do budowania, serwowania i zarz�dzania
du�ymi serwisami WWW.  Ze wzgl�du na swoje mo�liwo�ci, jest to idealna
baza pod du�e serwisy o dynamicznie generowanej zawarto�ci, jak gazety
internetowe czy oparte na bazach danych sklepy internetowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch0 -p0

%build
perl Makefile.PL --no-prompts
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_sitelib}/HTML/Mason/*.pod

gzip -9nf samples/README
cp -a {samples,eg} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv bin contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README UPGRADE CREDITS htdocs contrib
%{perl_sitelib}/Apache/Mason.pm
%{perl_sitelib}/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/eg
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/eg/*.pl
%{_examplesdir}/%{name}-%{version}/eg/httpd.conf
%{_examplesdir}/%{name}-%{version}/samples
%{_mandir}/man3/HTML*
