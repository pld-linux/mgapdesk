%define		beta	beta3
Summary:	Configuration utility for Matrox Graphics adapters
Summary(pl):	Narzêdzie do konfiguracji kart graficznych firmy Matrox
Name:		mgapdesk
Version:	1.00
Release:	0.%{beta}.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.matrox.com/pub/mga/archive/linux/2001/powerdesk_1_00_7/%{name}-1_00-7beta_src.tgz
# Source0-md5:	3d18363a518ba9fd4e8bed9b2e250f28
URL:		http://www.matrox.com/mga/support/drivers/files/lnx_30.cfm
BuildRequires:	gtk+-devel >= 1.2.0
Vendor:		Matrox Graphics Inc.
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matrox Linux Powerdesk. Utility for configuring Matrox Graphic
adapters under XFree86.

%description -l pl
Narzêdzie do konfiguracji kart graficznych firmy Matrox pod XFree86.

%prep
%setup -q -n mgapdesk

%build
%{__aclocal}
%{__automake}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*
