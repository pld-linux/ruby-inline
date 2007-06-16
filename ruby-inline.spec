Summary:	Allow embedding of C inline to Ruby
Name:		ruby-inline
Version:	3.6.3
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/20111/RubyInline-%{version}.gem
# Source0-md5:	2daaa20b5b188c8f0ea5d503a0644432
URL:		http://www.zenspider.com/ZSS/Products/RubyInline/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby Inline is an analog to Perl's Inline::C. Out of the box, it
allows you to embed C/++ external module code in your ruby script
directly. By writing simple builder classes, you can teach how to cope
with new languages (fortran, perl, whatever).

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_ridir}/CompilationError
%{ruby_ridir}/Inline
%attr(755,root,root) %{_bindir}/inline_package
%{ruby_rubylibdir}/inline.rb
