Summary:	Pattern based drum machine
Summary(pl):	Automat perkusyjny
Name:		hydrogen
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/hydrogen/%{name}-%{version}.tar.gz
# Source0-md5:	73573d3fec305a71dfae8a1892eb655a
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://hydrogen.sourceforge.net/
BuildRequires:  alsa-lib-devel >= 0.9.0
BuildRequires:  audiofile-devel >= 0.2.3
BuildRequires:  jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 3.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hydrogen is a "free" pattern based drum machine for GNU/Linux. The
application goal is to allow the simple and fast creation of rhythmic
patterns.

%description -l pl
Hydrogen jest "wolnym" automatem perkusyjnym opartym o paterny dla
GNU/Linuksa. Celem programu jest umo�liwienie w prosty i szybki spos�b
tworzenia patern�w rytmicznych.

%prep
%setup -q

%build
%configure \
	--disable-debug-messages

%{__make} \
	CXXFLAGS="$CXXFLAGS %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/hydrogen
%dir %{_datadir}/hydrogen/i18n
%lang(fr) %{_datadir}/hydrogen/i18n/%{name}.fr.qm
%lang(es) %{_datadir}/hydrogen/i18n/%{name}.es.qm
%lang(it) %{_datadir}/hydrogen/i18n/%{name}.it.qm
%lang(ru) %{_datadir}/hydrogen/i18n/%{name}.ru.qm
%{_datadir}/hydrogen/data
%{_datadir}/hydrogen/img
%{_datadir}/hydrogen/manual
%{_mandir}/man1/hydrogen*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
