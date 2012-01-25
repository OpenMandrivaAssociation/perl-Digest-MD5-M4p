%define upstream_name    Digest-MD5-M4p
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

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
