#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.event
Version  : 4.5.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/30/00/94ed30bfec18edbabfcbd503fcf7482c5031b0fbbc9bc361f046cb79781c/zope.event-4.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/00/94ed30bfec18edbabfcbd503fcf7482c5031b0fbbc9bc361f046cb79781c/zope.event-4.5.0.tar.gz
Summary  : Very basic event publishing system
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.event-license = %{version}-%{release}
Requires: pypi-zope.event-python = %{version}-%{release}
Requires: pypi-zope.event-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
``zope.event`` README
        =======================

%package license
Summary: license components for the pypi-zope.event package.
Group: Default

%description license
license components for the pypi-zope.event package.


%package python
Summary: python components for the pypi-zope.event package.
Group: Default
Requires: pypi-zope.event-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.event package.


%package python3
Summary: python3 components for the pypi-zope.event package.
Group: Default
Requires: python3-core
Provides: pypi(zope.event)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-zope.event package.


%prep
%setup -q -n zope.event-4.5.0
cd %{_builddir}/zope.event-4.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649799883
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.event
cp %{_builddir}/zope.event-4.5.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.event/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.event/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
