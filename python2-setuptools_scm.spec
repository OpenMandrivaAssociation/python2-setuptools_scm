Summary:	Tool to manage python package versions by scm tags
Name:		python2-setuptools_scm
Version:	3.3.3
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/setuptools_scm/#files
# See also	https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/83/44/53cad68ce686585d12222e6769682c4bdb9686808d2739671f9175e2938b/setuptools_scm-3.3.3.tar.gz
BuildRequires:	pkgconfig(python2)
BuildRequires:	pythonegg(setuptools)
BuildArch:	noarch

%description
Tool to manage python package versions by scm tags

%files
%{py2_puresitedir}/setuptools_scm*

%prep
%setup -qn setuptools_scm-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root %{buildroot}

