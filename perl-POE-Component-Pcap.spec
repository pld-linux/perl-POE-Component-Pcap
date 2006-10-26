#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test"
#				  (need root access to open a network device)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Pcap
Summary:	POE::Component::Pcap - POE interface to Net::Pcap
Summary(pl):	POE::Component::Pcap - interfejs POE do Net::Pcap
Name:		perl-POE-Component-Pcap
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11c6e6babcb8ee0b6a3c247c04059dc1
URL:		http://search.cpan.org/dist/POE-Component-Pcap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-Pcap >= 0.04
BuildRequires:	perl-NetPacket >= 0.01
BuildRequires:	perl-POE >= 0.26
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Pcap provides a wrapper for using the Net::Pcap module
from POE programs. The component creates a separate session which
posts events to a specified session and state when packets are
available.

%description -l pl
POE::Component::Pcap dostarcza wrapper do u¿ywania modu³u Net::Pcap z
poziomu programów POE. Komponent ten tworzy oddzieln± sesjê wysy³aj±c±
zdarzenia do okre¶lonej sesji i stanu, kiedy pakiety s± dostêpne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/POE/Component/Pcap.pm
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%{_mandir}/man3/*
