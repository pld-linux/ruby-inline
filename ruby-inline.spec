%define pkgname inline
%define gemname RubyInline
Summary:	Inline allows you to write foreign code within your ruby code
Name:		ruby-%{pkgname}
Version:	3.14.3
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{gemname}-%{version}.gem
# Source0-md5:	2de0e2c2cabc5afe513c15a3951ec910
URL:		http://www.zenspider.com/ZSS/Products/RubyInline/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-ZenTest >= 4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline allows you to write foreign code within your ruby code. It
automatically determines if the code in question has changed and builds
it only when necessary.

%prep
%setup -q -n %{gemname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{gemname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/inline.rb
%{ruby_specdir}/%{gemname}-%{version}.gemspec
