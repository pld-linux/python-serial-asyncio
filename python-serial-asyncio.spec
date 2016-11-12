#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_with	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define		module	serial-asyncio
Summary:	Async I/O extension for pyserial
Name:		python-serial-asyncio
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	https://github.com/pyserial/pyserial-asyncio/archive/v%{version}.tar.gz
# Source0-md5:	52934ac0e69d75ad580cdaac53f605ba
URL:		http://pyserial.wiki.sourceforge.net/pySerial
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%{?with_doc:BuildRequires:	sphinx-pdg}
BuildRequires:	unzip
Requires:	python-serial
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Async I/O extension for python serial module.

%package -n python3-%{module}
Summary:	Async I/O extension for pyserial
Group:		Libraries/Python
Requires:	python3 >= 1:3.4
Requires:	python3-serial

%description -n python3-%{module}
Async I/O extension for pyserial.

%prep
%setup  -q -n pyserial-asyncio-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%if %{with doc}
cd documentation
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst documentation/_build/html/*
%{py_sitescriptdir}/serial_asyncio
%{py_sitescriptdir}/*egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst documentation/_build/html/*
%{py3_sitescriptdir}/serial_asyncio
%{py3_sitescriptdir}/*egg-info
%endif
