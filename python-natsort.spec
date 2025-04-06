Name:		python-natsort
Version:	8.4.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/n/natsort/natsort-%{version}.tar.gz
Summary:	Simple yet flexible natural sorting in Python.
URL:		https://pypi.org/project/natsort/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Simple yet flexible natural sorting in Python.

%files
%{_bindir}/natsort
%{py_sitedir}/natsort
%{py_sitedir}/natsort-*.*-info
