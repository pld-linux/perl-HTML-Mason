%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Mason perl module
Summary(pl):	Modu� perla HTML-Mason
Name:		perl-HTML-Mason
Version:	0.71
Release:	2
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Mason-%{version}.tar.gz
Patch0:		perl-HTML-Mason-paths.patch
Patch1:		perl-HTML-Mason-fix.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-MLDBM
BuildRequires:	perl-Time-HiRes
BuildRequires:	mod_perl
%requires_eq	perl
Requires:	%{perl_sitearch}
Provides:	perl(HTML::Mason::Config)
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTML-Mason is a full-featured web site development and delivery system.

%description -l pl
HTML-Mason jest w pe�ni funkcjonalnym systemem tworzenia serwis�w www.

%prep
%setup -q -n HTML-Mason-%{version}
%patch0 -p0
%patch1 -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

cp -a {samples,eg} $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Mason
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README htdocs/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz htdocs/*

%{perl_sitelib}/Apache/Mason.pm
%{perl_sitelib}/Bundle/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason
%{perl_sitelib}/HTML/makeconfig.pl

%{perl_sitearch}/auto/HTML/Mason

/usr/src/examples/%{name}-%{version}

%{_mandir}/man3/*
