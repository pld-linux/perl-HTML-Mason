%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Mason
Summary:	HTML::Mason perl module
Summary(pl):	Modu³ perla HTML::Mason
Name:		perl-HTML-Mason
Version:	1.11
Release:	1
Epoch:		2
License:	GPL
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#Patch0:		%{name}-fix.patch
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRequires:	perl >= 5.6
BuildRequires:	perl(File::Spec)       >= 0.8
BuildRequires:	perl-Params-Validate >= 0.18
BuildRequires:	perl-Exception-Class >= 1.01
BuildRequires:	perl-Cache-Cache >= 1.0
BuildRequires:	perl-Class-Container >= 0.02
BuildRequires:	apache-mod_perl
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
Mason jest narzêdziem, s³u¿±cym do budowania, serwowania i zarz±dzania
du¿ymi serwisami WWW.  Ze wzglêdu na swoje mo¿liwo¶ci, jest to idealna
baza pod du¿e serwisy o dynamicznie generowanej zawarto¶ci, jak gazety
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
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/HTML*
