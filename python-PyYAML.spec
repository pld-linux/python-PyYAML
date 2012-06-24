#
%define		module		PyYAML
%define		module_dir	yaml
#
Summary:	YAML parser and emitter module for Python
Summary(pl.UTF8):	Analizator i generator formatu YAML dla j�0�1zyka Python
Name:		python-%{module}
Version:	3.09
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://pyyaml.org/download/pyyaml/%{module}-%{version}.tar.gz
# Source0-md5:	f219af2361e87fdc5e85e95b84c11d87
URL:		http://pyyaml.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
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
YAML jest formatem serializacji danych czytelnym dla cz�0�0owieka,
zaprojektowanym do interakcji w j�0�1zykach skryptowych. PyYAML jest
analizatorem i generatorem tego formatu dla j�0�1zyka Python.

PyYAML posiada obs�0�0ug�0�1 pe�0�0nej analizy YAML 1.1, Unicode,
serializacj�0�1 poprzez piklowanie, rozszerzalne API oraz
zrozumia�0�0e komunikaty b�0�0�0�1d��w. Obs�0�0uguje standardowe
znaczniki YAML i dostarcza nowe, specyficzne dla j�0�1zyka Python,
pozwalaj�0�2ce na reprezentacj�0�1 jego obiekt��w.

PyYAML mo�0�4e by�0�4 u�0�4yty w szerokiej gamie zastosowa��, od
z�0�0o�0�4onych plik��w konfiguracyjnych po serializacj�0�1 i
przechowywanie obiekt��w.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
install examples/yaml-highlight/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/%{module_dir}
%{py_sitedir}/%{module_dir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
