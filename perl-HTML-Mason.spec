%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Mason perl module
Summary(pl):	Modu³ perla HTML-Mason
Name:		perl-HTML-Mason
Version:	1.01
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Mason-%{version}.tar.gz
Patch0:		%{name}-fix.patch
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MLDBM
BuildRequires:	perl-Time-HiRes
BuildRequires:	mod_perl
%requires_eq	perl
Requires:	%{perl_sitearch}
Provides:	perl(HTML::Mason::Config)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Mason is a full-featured web site development and delivery
system.

%description -l pl
HTML-Mason jest w pe³ni funkcjonalnym systemem tworzenia serwisów www.

%prep
%setup -q -n HTML-Mason-%{version}
%patch0 -p0

%build
find . -type f | xargs -n 200 -r perl -pi -e 's|/local/bin/perl\d*|/bin/perl|g'
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a {samples,eg} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README htdocs/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz htdocs/*
%{perl_sitelib}/Apache/Mason.pm
%{perl_sitelib}/Bundle/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
