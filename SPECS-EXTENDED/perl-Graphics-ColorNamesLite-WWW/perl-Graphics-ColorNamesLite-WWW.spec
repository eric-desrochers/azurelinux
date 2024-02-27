Summary:        WWW color names and equivalent RGB values
Name:           perl-Graphics-ColorNamesLite-WWW
Version:        1.14.000
Release:        6%{?dist}
License:        GPL+ OR Artistic
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
URL:            https://metacpan.org/release/Graphics-ColorNamesLite-WWW/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Graphics-ColorNamesLite-WWW-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%if 0%{?with_check}
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
WWW color names and equivalent RGB values (lite version).

%prep
%setup -q -n Graphics-ColorNamesLite-WWW-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 26 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.14.000-6
- Initial CBL-Mariner import from Fedora 36 (license: MIT).
- License verified.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.14.000-4
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Jitka Plesnikova <jplesnik@redhat.com> 1.14.000-1
- Specfile autogenerated by cpanspec 1.78.
