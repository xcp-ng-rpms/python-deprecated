%global package_speccommit c2ba3b2cf2c69dd5e0cf4f6e2c49782800eb872b
%global usver 1.2.14
%global xsver 3
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global srcname Deprecated
%global pkgname deprecated

Name:           python-%{pkgname}
Version:        1.2.14
Release:        %{?xsrel}%{?dist}
Summary:        Python decorator to deprecate old python classes, functions or methods
License:        MIT
URL:            https://github.com/tantale/%{pkgname}
Source0: Deprecated-1.2.14.tar.gz
BuildArch:      noarch

%description
Python @deprecated decorator to deprecate old python classes,
functions or methods.

%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Python @deprecated decorator to deprecate old python classes,
functions or methods.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{pkgname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkgname}
%license LICENSE.rst
%doc README.md
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Mon Aug 19 2024 Marcus Granado <marcus.granado@cloud.com> - 1.2.14-3
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 1.2.14-3
- Bump release and rebuild

* Mon Feb 12 2024 Rachel Yan <rachel.yan@citrix.com> - 1.2.14-1
- Initial import
