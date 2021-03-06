Name:           fdupes
Version:        1.40
Release:        0
License:        MIT
Summary:        Identifying or deleting duplicate files
Url:            http://premium.caribe.net/~adrian2/fdupes.html
Group:          Base/Compression
Source0:        %{name}-%{version}.tar.bz2
Source1:        macros.fdupes
Source1001:     fdupes.manifest

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories

%prep
%setup -q
cp %{SOURCE1001} .

%build
make

%install
install -D -m755 fdupes %{buildroot}%{_bindir}/fdupes
install -D -m644 fdupes.1 %{buildroot}%{_mandir}/man1/fdupes.1
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.fdupes

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%doc CHANGES
%{_bindir}/fdupes
%{_mandir}/*/*
%config %{_sysconfdir}/rpm
