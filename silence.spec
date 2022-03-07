Name:		silence
Version:	1.0
Release:	1%{?dist}
Summary:	Text base RPG

License:	GPLv2+
URL:		http://example.com/
Source0:	http://example.com/%{name}-%{version}.tar.gz

BuildRequires:	python3-devel
BuildArch:	noarch

%description
Text base RPG

%prep
%setup -qn %{name}-%{version}


%build
%py3_build

%install
%py3_install '--install-scripts=%{_bindir}'


%files
%{_bindir}/silence
%{python3_sitelib}/*
%{_mandir}/man1/*
%license LICENSE

%changelog
* Wed Oct 20 2021 Andrew Heath <anheath at redhat dot com> - 1.0-1
- inital package build
