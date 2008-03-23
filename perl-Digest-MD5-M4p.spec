%define realname Digest-MD5-M4p

Summary: Perl interface to a variant of the MD5 algorithm
Name: perl-Digest-MD5-M4p
Version: 0.01
Release: %mkrel 1
License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/dist/Digest-MD5-M4p/
Source: http://www.cpan.org/modules/by-module/Digest/Digest-MD5-M4p-%{version}.tar.bz2
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl-devel

%description
he Digest::MD5 module is cloned from the Digest::MD5 module to support a
variant  Apple iTunes implementation of the MD5 algorithm. If you don't know 
why this is so, don't bother with this module! It is incompatible with RSA 
and RFC standards!

%prep
%setup -q -n %{realname}-%{version}

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
