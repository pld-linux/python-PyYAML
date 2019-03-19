# note: uses name after egg/pypi; import name is "yaml", source is "pyyaml"
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define		module		PyYAML
Summary:	YAML parser and emitter module for Python 2
Summary(pl.UTF-8):	Analizator i generator formatu YAML dla języka Python 2
Name:		python-%{module}
Version:	5.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/yaml/pyyaml/releases
Source0:	https://github.com/yaml/pyyaml/archive/%{version}/pyyaml-%{version}.tar.gz
# Source0-md5:	7d201eec206eb8d78261bfc1d4a98691
URL:		https://github.com/yaml/pyyaml
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	yaml-devel >= 0.2.2
%if %{with python2}
BuildRequires:	python-Cython
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
%endif
Requires:	python-modules >= 1:2.7
Requires:	yaml >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages. PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%description -l pl.UTF-8
YAML jest formatem serializacji danych czytelnym dla człowieka,
zaprojektowanym do interakcji w językach skryptowych. PyYAML jest
analizatorem i generatorem tego formatu dla języka Python.

PyYAML posiada obsługę pełnej analizy YAML 1.1, Unicode, serializację
poprzez piklowanie, rozszerzalne API oraz zrozumiałe komunikaty
błędów. Obsługuje standardowe znaczniki YAML i dostarcza nowe,
specyficzne dla języka Python, pozwalające na reprezentację jego
obiektów.

PyYAML może być użyty w szerokiej gamie zastosowań, od złożonych
plików konfiguracyjnych po serializację i przechowywanie obiektów.

%package -n python3-%{module}
Summary:	YAML parser and emitter module for Python 3
Summary(pl.UTF-8):	Analizator i generator formatu YAML dla języka Python 3
Group:		Libraries/Python
Requires:	yaml >= 0.2.2
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

%description -n python3-%{module} -l pl.UTF-8
PyYAML posiada obsługę pełnej analizy YAML 1.1, Unicode, serializację
poprzez piklowanie, rozszerzalne API oraz zrozumiałe komunikaty
błędów. Obsługuje standardowe znaczniki YAML i dostarcza nowe,
specyficzne dla języka Python, pozwalające na reprezentację jego
obiektów.

%prep
%setup -q -n pyyaml-%{version}

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py --with-libyaml \
	build --build-base build-2 %{?with_tests:test}
%endif
%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} setup.py --with-libyaml \
	build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/yaml-highlight/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-PyYAML-%{version}
cp -p examples/yaml-highlight/* $RPM_BUILD_ROOT%{_examplesdir}/python3-PyYAML-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{py_sitedir}/_yaml.so
%{py_sitedir}/yaml
%{py_sitedir}/PyYAML-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{py3_sitedir}/_yaml.cpython-*.so
%{py3_sitedir}/yaml
%{py3_sitedir}/PyYAML-%{version}-py*.egg-info
%{_examplesdir}/python3-PyYAML-%{version}
%endif
