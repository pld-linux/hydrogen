# TODO:
# - pass __cxx and rpmldflags
Summary:	Pattern based drum machine
Summary(pl.UTF-8):	Automat perkusyjny
Name:		hydrogen
Version:	0.9.5.1
Release:	1
License:	GPL v2, zlib (TinyXML Library)
Group:		X11/Applications/Sound
Source0:	http://download.sourceforge.net/hydrogen/%{name}-%{version}.tar.gz
# Source0-md5:	52f3a528705818c65acf546a3be4c6fb
Patch0:		%{name}.desktop.patch
Patch1:		%{name}-flags.patch
URL:		http://www.hydrogen-music.org/
BuildRequires:	QtGui-devel >= 4.4.0
BuildRequires:	QtNetwork-devel >= 4.4.0
BuildRequires:	QtXml-devel >= 4.4.0
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	flac-c++-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.103.0
BuildRequires:	lash-devel >= 0.5.0
BuildRequires:	liblrdf-devel
BuildRequires:	libsndfile-devel >= 1.0.17
BuildRequires:	libtar-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	scons >= 0.98
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hydrogen is a "free" pattern based drum machine for GNU/Linux. The
application goal is to allow the simple and fast creation of rhythmic
patterns.

%description -l pl.UTF-8
Hydrogen jest "wolnym" automatem perkusyjnym opartym o paterny dla
GNU/Linuksa. Celem programu jest umożliwienie w prosty i szybki
sposób tworzenia paternów rytmicznych.

%package doc
Summary:	Hydrogen manual and tutorial
Summary(pl.UTF-8):	Podręcznik i tutorial Hydrogena
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Hydrogen manual and tutorial.

%description doc -l pl.UTF-8
Podręcznik i tutorial Hydrogena.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%{__patch} -p0 -s < patches/portaudio.patch

%build
%{__scons} \
	prefix=%{_prefix} \
	portaudio=1 \
	portmidi=1 \
	optflags="%{rpmcxxflags}" \
	ldflags="%{rpmldflags}" \
	lash=1

%install
rm -rf $RPM_BUILD_ROOT

# Temporary fix. Scons install breaks on inexistance of directory below
# It should be fixed inside scons, but don't know how
install -d $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/img/gray

%{__scons} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/doc/img/Tutorial2.h2song \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs

# clean up documentation
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/{Makefile,README.DOCUMENTATION.txt}
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/*.{docbook,po,pot}
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/img/*.h2song
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/i18n/*.ts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.txt
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/hydrogen
%dir %{_datadir}/hydrogen/data
%dir %{_datadir}/hydrogen/data/demo_songs
%dir %{_datadir}/hydrogen/data/i18n

%{_datadir}/hydrogen/data/*.conf
%{_datadir}/hydrogen/data/*.h2song
%{_datadir}/hydrogen/data/*.wav
%{_datadir}/hydrogen/data/drumkits
%{_datadir}/hydrogen/data/img
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.svg

# demo songs
%{_datadir}/hydrogen/data/demo_songs/GM_*.h2song
%{_datadir}/hydrogen/data/demo_songs/TR808kit-demo.h2song
%{_datadir}/hydrogen/data/demo_songs/tutorial_georgyporgy.h2song

# translations
%lang(ca) %{_datadir}/hydrogen/data/i18n/%{name}.ca.qm
%lang(cs) %{_datadir}/hydrogen/data/i18n/%{name}.cs.qm
%lang(de) %{_datadir}/hydrogen/data/i18n/%{name}.de.qm
%lang(el) %{_datadir}/hydrogen/data/i18n/%{name}.el.qm
%lang(es) %{_datadir}/hydrogen/data/i18n/%{name}.es.qm
%lang(fr) %{_datadir}/hydrogen/data/i18n/%{name}.fr.qm
%lang(hu) %{_datadir}/hydrogen/data/i18n/%{name}.hu_HU.qm
%lang(hr) %{_datadir}/hydrogen/data/i18n/%{name}.hr.qm
%lang(it) %{_datadir}/hydrogen/data/i18n/%{name}.it.qm
%lang(ja) %{_datadir}/hydrogen/data/i18n/%{name}.ja.qm
%lang(nl) %{_datadir}/hydrogen/data/i18n/%{name}.nl.qm
%lang(pl) %{_datadir}/hydrogen/data/i18n/%{name}.pl.qm
%lang(pt_BR) %{_datadir}/hydrogen/data/i18n/%{name}.pt_BR.qm
%lang(ru) %{_datadir}/hydrogen/data/i18n/%{name}.ru.qm
%lang(sv) %{_datadir}/hydrogen/data/i18n/%{name}.sv.qm

%files doc
%defattr(644,root,root,755)
%doc data/doc/README.DOCUMENTATION.txt
%dir %{_datadir}/hydrogen/data/doc
%dir %{_datadir}/hydrogen/data/doc/img

# demo songs
%{_datadir}/hydrogen/data/demo_songs/Tutorial2.h2song

# images
%lang(nl) %{_datadir}/hydrogen/data/doc/img/nl
%{_datadir}/hydrogen/data/doc/img/*.png
%{_datadir}/hydrogen/data/doc/img/*.svg
%{_datadir}/hydrogen/data/doc/img_tutorial
%{_datadir}/hydrogen/data/doc/infoSplash

# multilang manual & tutorial
%lang(ca) %{_datadir}/hydrogen/data/doc/manual_ca.html
%lang(es) %{_datadir}/hydrogen/data/doc/manual_es.html
%lang(es) %{_datadir}/hydrogen/data/doc/tutorial_es.html
%lang(fr) %{_datadir}/hydrogen/data/doc/manual_fr.html
%lang(fr) %{_datadir}/hydrogen/data/doc/tutorial_fr.html
%lang(it) %{_datadir}/hydrogen/data/doc/manual_it.html
%lang(it) %{_datadir}/hydrogen/data/doc/tutorial_it.html
%lang(nl) %{_datadir}/hydrogen/data/doc/manual_nl.html
%{_datadir}/hydrogen/data/doc/manual.html
%{_datadir}/hydrogen/data/doc/manual_en.html
%{_datadir}/hydrogen/data/doc/tutorial_en.html
