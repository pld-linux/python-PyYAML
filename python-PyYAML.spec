#
# TODO:
#	- the name should be python-yaml (used via 'import yaml')
#

%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define		module		PyYAML
%define		module_dir	yaml
#
Summary:	YAML parser and emitter module for Python
Summary(pl.UTF-8):	Analizator i generator formatu YAML dla języka Python
Name:		python-%{module}
Version:	3.11
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://pyyaml.org/download/pyyaml/%{module}-%{version}.tar.gz
# Source0-md5:	f50e08ef0fe55178479d3a618efe21db
URL:		http://pyyaml.org/
BuildRequires:	yaml-devel
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package -n python3-%{module}
Summary:	YAML parser and emitter module for Python
Summary(pl.UTF-8):	Analizator i generator formatu YAML dla języka Python
Group:		Libraries/Python

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

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py --with-libyaml build --build-base build-2 %{?with_tests:test}
%endif
%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} setup.py --with-libyaml build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%{__python} setup.py \
        build --build-base build-2 \
        install --skip-build \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT
%py_postclean
%endif
%if %{with python3}
%{__python3} setup.py \
        build --build-base build-3 \
        install --skip-build \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT
%endif
%py_postclean
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/yaml-highlight/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/%{module_dir}
%attr(755,root,root) %{py_sitedir}/_yaml.so
%{py_sitedir}/%{module_dir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README
%dir %{py3_sitedir}/%{module_dir}
%{py3_sitedir}/%{module_dir}/*.py
%{py3_sitedir}/%{module_dir}//__pycache__
%attr(755,root,root) %{py3_sitedir}/_yaml.cpython-*m.so
%{py3_sitedir}/PyYAML-3.11-py*.egg-info
%endif
