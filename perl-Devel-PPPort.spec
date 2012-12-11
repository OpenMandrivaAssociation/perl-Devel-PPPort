%define upstream_name Devel-PPPort
%define upstream_version 3.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Portability aid for your XS code
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.200.0-1
+ Revision: 773527
- clean out spec
- new version
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 3.190.0-4
+ Revision: 681403
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 3.190.0-3mdv2011.0
+ Revision: 555239
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.190.0-2mdv2011.0
+ Revision: 552001
- rebuild

* Thu Jun 18 2009 Jérôme Quelin <jquelin@mandriva.org> 3.190.0-1mdv2010.0
+ Revision: 386976
- forgot to commit the new tarball
- update to 3.19
- using %%perl_convert_version
- fix license tag

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 3.17-2mdv2010.0
+ Revision: 374416
- rebuild
- import perl-Devel-PPPort


* Mon May 11 2009 cpan2dist 3.17-1mdv
- initial mdv release, generated with cpan2dist

