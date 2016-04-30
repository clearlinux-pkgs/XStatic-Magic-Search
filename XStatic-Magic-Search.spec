#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Magic-Search
Version  : 0.2.5.1
Release  : 12
URL      : https://pypi.python.org/packages/source/X/XStatic-Magic-Search/XStatic-Magic-Search-0.2.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Magic-Search/XStatic-Magic-Search-0.2.5.1.tar.gz
Summary  : Magic-Search 0.2.5 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-Magic-Search-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-MagicSearch
-------------------
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%package python
Summary: python components for the XStatic-Magic-Search package.
Group: Default
Provides: xstatic-magic-search-python

%description python
python components for the XStatic-Magic-Search package.


%prep
%setup -q -n XStatic-Magic-Search-0.2.5.1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
