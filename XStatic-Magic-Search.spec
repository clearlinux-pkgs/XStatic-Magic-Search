#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Magic-Search
Version  : 0.2.5.1
Release  : 18
URL      : http://pypi.debian.net/XStatic-Magic-Search/XStatic-Magic-Search-0.2.5.1.tar.gz
Source0  : http://pypi.debian.net/XStatic-Magic-Search/XStatic-Magic-Search-0.2.5.1.tar.gz
Summary  : Magic-Search 0.2.5 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-Magic-Search-python3
Requires: XStatic-Magic-Search-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
-------------------
        
        MagicSearch is an AngularJS directive that provides a UI for both faceted
        filtering and as-you-type filtering. It is intended for filtering tables,
        such as an AngularJS smart-table, but it can be used in any situation
        where you can provide it with facets/options and consume its events.
        
        MagicSearch was initially developed by David Kavanagh for Eucalyptus.
        
        
        MagicSearch javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Magic-Search package.
Group: Default
Requires: XStatic-Magic-Search-python3
Provides: xstatic-magic-search-python

%description python
python components for the XStatic-Magic-Search package.


%package python3
Summary: python3 components for the XStatic-Magic-Search package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-Magic-Search package.


%prep
%setup -q -n XStatic-Magic-Search-0.2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532215263
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
