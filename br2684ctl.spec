Summary:	Utility for configuring RFC 2684 ATM/Ethernet bridging
Summary(pl.UTF-8):	Narzędzie do konfigurowania mostkowania ATM/Ethernet wg RFC 2684
Name:		br2684ctl
Version:	20040226
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/b/br2684ctl/%{name}_%{version}.orig.tar.gz
# Source0-md5:	6eb4d8cd174e24a7c078eb4f594f5b69
Patch0:		%{name}-debian.patch
URL:		http://home.sch.bme.hu/~cell/br2684/
BuildRequires:	linux-atm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for configuring RFC 2684 ATM/Ethernet bridging.

ATM bridging is a way to extend Ethernet over an ATM network and is
mainly used for DSL connections. This package contains the user space
utility needed to configure the kernel driver.

%description -l pl.UTF-8
Narzędzie do konfigurowania mostkowania ATM/Ethernet wg RFC 2684.

Mostkowanie ATM to sposób rozszerzenia sieci Ethernet po ATM i jest
stosowane głównie przy połączeniach DSL. Ten pakiet zawiera narzędzie
przestrzeni użytkownika potrzebne do skonfigurowania sterownika w
jądrze.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install br2684ctl $RPM_BUILD_ROOT%{_sbindir}
install br2684ctl.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/br2684ctl
%{_mandir}/man8/br2684ctl.8*
