%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Mason
Summary:	HTML::Mason Perl module
Summary(cs):	Modul HTML::Mason pro Perl
Summary(da):	Perlmodul HTML::Mason
Summary(de):	HTML::Mason Perl Modul
Summary(es):	Módulo de Perl HTML::Mason
Summary(fr):	Module Perl HTML::Mason
Summary(it):	Modulo di Perl HTML::Mason
Summary(ja):	HTML::Mason Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	HTML::Mason ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul HTML::Mason
Summary(pl):	Modu³ Perla HTML::Mason
Summary(pt):	Módulo de Perl HTML::Mason
Summary(pt_BR):	Módulo Perl HTML::Mason
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl HTML::Mason
Summary(sv):	HTML::Mason Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl HTML::Mason
Summary(zh_CN):	HTML::Mason Perl Ä£¿é
Name:		perl-HTML-Mason
Version:	1.1201
Release:	1
Epoch:		2
License:	GPL/Artistic
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#Patch0:	%{name}-fix.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
Requires:	perl(File::Spec) >= 0.8
Requires:	perl-Cache-Cache >= 1.0
Requires:	perl-Class-Container >= 0.07
Requires:	perl-Exception-Class >= 1.01
Requires:	perl-Params-Validate >= 0.18
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
Mason jest narzêdziem, s³u¿±cym do budowania, serwowania i zarz±dzania
du¿ymi serwisami WWW.  Ze wzglêdu na swe mo¿liwo¶ci, jest idealn± baz±
dla du¿ych serwisów o dynamicznie generowanej zawarto¶ci, np. gazet
internetowych czy oparte na bazach danych e-sklepów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch0 -p0

%build
perl Makefile.PL --no-prompts
%{__make}
#%{__make} test

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
