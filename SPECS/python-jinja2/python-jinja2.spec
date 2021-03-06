%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_version: %define python3_version %(python3 -c "import sys; sys.stdout.write(sys.version[:3])")}

Name:           python-jinja2
Version:        2.9.5
Release:        3%{?dist}
Url:            http://jinja.pocoo.org/
Summary:        A fast and easy to use template engine written in pure Python
License:        BSD
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://pypi.python.org/packages/71/59/d7423bd5e7ddaf3a1ce299ab4490e9044e8dfd195420fc83a24de9e60726/Jinja2-2.9.5.tar.gz
%define sha1 	Jinja2=a3129c140d34ae565a556e48db40772df3536b23
BuildRequires:  python2
BuildRequires:  python2-libs
BuildRequires:  python-setuptools
BuildRequires:  python-markupsafe
Requires:       python2
Requires:       python2-libs
Requires:       python-markupsafe
BuildArch:      noarch

%description
Jinja2 is a template engine written in pure Python.  It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%package -n     python3-jinja2
Summary:        A fast and easy to use template engine written in pure Python
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-markupsafe
Requires:       python3
Requires:       python3-libs
Requires:       python3-markupsafe

%description -n python3-jinja2

Python 3 version.

%prep
%setup -q -n Jinja2-%{version}
rm -rf ../p3dir
cp -a . ../p3dir

%build
python setup.py build
sed -i 's/\r$//' LICENSE # Fix wrong EOL encoding
pushd ../p3dir
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
sed -i 's/\r$//' LICENSE # Fix wrong EOL encoding
popd

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
pushd ../p3dir
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES
%license LICENSE
%{python_sitelib}/jinja2
%exclude %{python_sitelib}/*/*.py
%{python_sitelib}/Jinja2-%{version}-py%{python_version}.egg-info

%files -n python3-jinja2
%defattr(-,root,root)
%doc AUTHORS CHANGES
%license LICENSE
%{python3_sitelib}/jinja2
%exclude %{python3_sitelib}/*/*.py
%{python3_sitelib}/Jinja2-%{version}-py%{python3_version}.egg-info

%changelog
*   Wed Apr 26 2017 Dheeraj Shetty <dheerajs@vmware.com> 2.9.5-3
-   BuildRequires python-markupsafe , creating subpackage python3-jinja2
*   Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.9.5-2
-   Fix arch
*   Mon Mar 27 2017 Sarah Choi <sarahc@vmware.com> 2.9.5-1
-   Upgrade version to 2.9.5 
*   Tue Dec 13 2016 Dheeraj Shetty <dheerajs@vmware.com> 2.8-1
-   Initial packaging for Photon
