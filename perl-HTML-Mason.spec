%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	HTML-Mason perl module
Summary(pl):	Modu³ perla HTML-Mason
Name:		perl-HTML-Mason
Version:	0.4
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Mason-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-File-Tools
%requires_eq	perl
Requires:	perl-File-Tools
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTML-Mason is a full-featured web site development and delivery system.

%description -l pl
HTML-Mason jest w pe³ni funkcjonalnym systemem tworzenia serwisów www.

%prep
%setup -q -n HTML-Mason-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
%doc {Changes,README}.gz
%doc htdocs/* samples eg

%{perl_sitelib}/HTML/Mason.pm
%{perl_sitelib}/HTML/Mason/*.pm
%{perl_sitearch}/auto/HTML/Mason

%{_mandir}/man3/*
