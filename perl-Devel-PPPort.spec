
%define realname   Devel-PPPort
%define version    3.17
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Portability aid for your XS code
Source:     http://www.cpan.org/modules/by-module/Devel/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel




%description
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C namespace
environment (reduced pollution). The header file written by this module,
typically _ppport.h_, attempts to bring some of the newer Perl API features
to older versions of Perl, so that you can worry less about keeping track
of old releases, but users can still reap the benefit.

'Devel::PPPort' contains a single function, called 'WriteFile'. Its only
purpose is to write the _ppport.h_ C header file. This file contains a
series of macros and, if explicitly requested, functions that allow XS
modules to be built using older versions of Perl. Currently, Perl versions
from 5.003 to 5.10.0 are supported.

This module is used by 'h2xs' to write the file _ppport.h_.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


