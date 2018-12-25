Summary:	Tool to manage python package versions by scm tags
Name:		python2-setuptools_scm
Version:	2.1.0
Release:	2
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/setuptools_scm/#files
# See also	https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/e5/62/f9e1ac314464eb5945c97542acb6bf6f3381dfa5d7a658de7730c36f31a1/setuptools_scm-%{version}.tar.gz
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

