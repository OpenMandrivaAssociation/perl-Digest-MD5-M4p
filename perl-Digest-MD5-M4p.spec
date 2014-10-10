%define upstream_name    Digest-MD5-M4p
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary:    Perl interface to a variant of the MD5 algorithm
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Digest/Digest-MD5-M4p-%{upstream_version}.tar.bz2

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
he Digest::MD5 module is cloned from the Digest::MD5 module to support a
variant  Apple iTunes implementation of the MD5 algorithm. If you don't know 
why this is so, don't bother with this module! It is incompatible with RSA 
and RFC standards!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Digest/MD5/M4p.pm
%{perl_vendorarch}/auto/Digest/MD5/M4p


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.10.0-3
+ Revision: 681423
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 555244
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 403151
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-3mdv2009.0
+ Revision: 256685
- rebuild

* Sun Mar 23 2008 Stefan van der Eijk <stefan@mandriva.org> 0.01-1mdv2008.1
+ Revision: 189577
- import perl-Digest-MD5-M4p


