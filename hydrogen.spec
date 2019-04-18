#
# TODO:
#	- fix localized manuals build
#
# Conditional build:
%bcond_without	tests		# build with tests


%define beta	beta1
%define rel	1
Summary:	Pattern based drum machine
Summary(pl.UTF-8):	Automat perkusyjny
Name:		hydrogen
Version:	1.0.0
Release:	0.%{beta}.%{rel}
License:	GPL v2, zlib (TinyXML Library)
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/hydrogen/%{name}-%{version}-%{beta}.tar.gz
# Source0-md5:	788540070d1874473fd1019e9de73f4b
Patch0:		mandir.patch
URL:		http://www.hydrogen-music.org/
# BuildRequires:	portaudio-devel < 19
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	cmake >= 2.8.11
%{?with_tests:BuildRequires:	cppunit-devel}
BuildRequires:	jack-audio-connection-kit-devel >= 0.103.0
BuildRequires:	ladspa-devel
BuildRequires:	lash-devel >= 0.5.0
BuildRequires:	libarchive-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsndfile-devel >= 1.0.18
BuildRequires:	pkgconfig
BuildRequires:	portmidi-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rubberband-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
# for translated manuals
#BuildRequires:	gnome-doc-utils
#BuildRequires:	kde4-poxml
#BuildRequires:	libxml2-progs
#BuildRequires:	xmlto
Obsoletes:	hydrogen-doc
# drumkits can be installed from the application
Obsoletes:	hydrogen-drumkits
Obsoletes:	hydrogen-drumkits-3355606
Obsoletes:	hydrogen-drumkits-DrumkitPack1
Obsoletes:	hydrogen-drumkits-DrumkitPack2
Obsoletes:	hydrogen-drumkits-EasternHop-1
Obsoletes:	hydrogen-drumkits-Electric-Empire-Kit
Obsoletes:	hydrogen-drumkits-ErnysPercussion
Obsoletes:	hydrogen-drumkits-HardElectro1
Obsoletes:	hydrogen-drumkits-Millo-Drums_v.1
Obsoletes:	hydrogen-drumkits-Millo-MultiLayered2
Obsoletes:	hydrogen-drumkits-TD-7
Obsoletes:	hydrogen-drumkits-UltraAcousticKit
Obsoletes:	hydrogen-drumkits-Yamaha-Vintage-Kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hydrogen is a "free" pattern based drum machine for GNU/Linux. The
application goal is to allow the simple and fast creation of rhythmic
patterns.

%description -l pl.UTF-8
Hydrogen jest "wolnym" automatem perkusyjnym opartym o paterny dla
GNU/Linuksa. Celem programu jest umożliwienie w prosty i szybki sposób
tworzenia paternów rytmicznych.

%prep
%setup -q -n %{name}-%{version}-%{beta}
%patch0 -p1

%build
mkdir build
cd build
%cmake .. \
	-DWANT_DEBUG=%{debug} \
	-DWANT_JACK=1 \
	-DWANT_ALSA=1 \
	-DWANT_LIBARCHIVE=1 \
	-DWANT_RUBBERBAND=1 \
	-DWANT_OSS=0 \
	-DWANT_PORTAUDIO=0 \
	-DWANT_PORTMIDI=1 \
	-DWANT_LASH=1 \
	-DWANT_LRDF=1 \
	-DWANT_COREAUDIO=0 \
	-DWANT_COREMIDI=0 \
	-DWANT_LADSPA=1 \
	-DLADSPA_INCLUDE_DIR=/usr/include \
	-DLADSPA_LIBRARIES=%{_libdir}/ladspa

%{__make}
cd ..

%if %{with tests}
%{__make} -C build tests
./build/src/tests/tests
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/img/gray/h2-icon.svg $RPM_BUILD_ROOT%{_pixmapsdir}/h2-icon.svg

rm -rf $RPM_BUILD_ROOT%{_includedir}/hydrogen
rm -rf $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/i18n/{stats.py,updateTranslations.sh}

# clean up documentation
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/{Makefile,README.md,TODO}
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/*.{docbook,po,pot}
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/img/*.h2song
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/i18n/*.ts

%post	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.txt
%attr(755,root,root) %{_bindir}/*
%doc data/doc/README.md
%attr(755,root,root) %{_libdir}/libhydrogen-core-%{version}.so

%dir %{_datadir}/hydrogen
%dir %{_datadir}/hydrogen/data
%dir %{_datadir}/hydrogen/data/demo_songs
%dir %{_datadir}/hydrogen/data/i18n

%{_datadir}/hydrogen/data/*.conf
%{_datadir}/hydrogen/data/*.h2song
%{_datadir}/hydrogen/data/*.wav
%{_datadir}/hydrogen/data/drumkits
%{_datadir}/hydrogen/data/img
%{_datadir}/hydrogen/data/xsd
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.svg

# demo songs
%{_datadir}/hydrogen/data/demo_songs/*.h2song

# translations
%lang(ca) %{_datadir}/hydrogen/data/i18n/%{name}.ca.qm
%lang(cs) %{_datadir}/hydrogen/data/i18n/%{name}.cs.qm
%lang(de) %{_datadir}/hydrogen/data/i18n/%{name}.de.qm
%lang(el) %{_datadir}/hydrogen/data/i18n/%{name}.el.qm
%lang(es) %{_datadir}/hydrogen/data/i18n/%{name}.es.qm
%lang(fr) %{_datadir}/hydrogen/data/i18n/%{name}.fr.qm
%lang(gl) %{_datadir}/hydrogen/data/i18n/%{name}.gl.qm
%lang(hu) %{_datadir}/hydrogen/data/i18n/%{name}.hu_HU.qm
%lang(hr) %{_datadir}/hydrogen/data/i18n/%{name}.hr.qm
%lang(it) %{_datadir}/hydrogen/data/i18n/%{name}.it.qm
%lang(ja) %{_datadir}/hydrogen/data/i18n/%{name}.ja.qm
%lang(nl) %{_datadir}/hydrogen/data/i18n/%{name}.nl.qm
%lang(pl) %{_datadir}/hydrogen/data/i18n/%{name}.pl.qm
%lang(pt_BR) %{_datadir}/hydrogen/data/i18n/%{name}.pt_BR.qm
%lang(ru) %{_datadir}/hydrogen/data/i18n/%{name}.ru.qm
%lang(sr) %{_datadir}/hydrogen/data/i18n/%{name}.sr.qm
%lang(sv) %{_datadir}/hydrogen/data/i18n/%{name}.sv.qm
%lang(uk) %{_datadir}/hydrogen/data/i18n/%{name}.uk.qm

%{_mandir}/man1/hydrogen.1*
%{_datadir}/appdata/*.xml

%dir %{_datadir}/hydrogen/data/doc
%dir %{_datadir}/hydrogen/data/doc/img

%{_datadir}/hydrogen/data/doc/MidiInstrumentMapping.ods

# images
%lang(nl) %{_datadir}/hydrogen/data/doc/img/nl
%{_datadir}/hydrogen/data/doc/img/*.png
%{_datadir}/hydrogen/data/doc/img_tutorial

# multilang manual & tutorial
#%lang(ca) %{_datadir}/hydrogen/data/doc/manual_ca.html
#%lang(es) %{_datadir}/hydrogen/data/doc/manual_es.html
#%lang(fr) %{_datadir}/hydrogen/data/doc/manual_fr.html
#%lang(it) %{_datadir}/hydrogen/data/doc/manual_it.html
#%lang(nl) %{_datadir}/hydrogen/data/doc/manual_nl.html
%{_datadir}/hydrogen/data/doc/manual.html
%{_datadir}/hydrogen/data/doc/manual_en.html

%dir %{_datadir}/hydrogen/data/new_tutorial
%{_datadir}/hydrogen/data/new_tutorial/img_tutorial
%{_datadir}/hydrogen/data/new_tutorial/tutorial_en.html
