# TODO: documentation? (submodule: https://github.com/hydrogen-music/documentation)
#
# Conditional build:
%bcond_with	rubberband	# RubberBand support (unadvised as of 1.2.3)
%bcond_with	tests		# test suite (need real sound drivers)

Summary:	Pattern based drum machine
Summary(pl.UTF-8):	Automat perkusyjny
Name:		hydrogen
Version:	1.2.6
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://downloads.sourceforge.net/hydrogen/%{name}-%{version}.tar.gz
# Source0-md5:	b0a93b00e303a463183ba01ae395e45e
URL:		http://hydrogen-music.org/
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Svg-devel >= 5
BuildRequires:	Qt5Test-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	Qt5XmlPatterns-devel >= 5
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	cmake >= 3.8
%{?with_tests:BuildRequires:	cppunit-devel}
BuildRequires:	jack-audio-connection-kit-devel >= 0.103.0
BuildRequires:	ladspa-devel
BuildRequires:	lash-devel >= 0.5.0
# or libtar-devel, but libarchive is preferred
BuildRequires:	libarchive-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsndfile-devel >= 1.0.18
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	portmidi-devel
BuildRequires:	pulseaudio-devel
%{?with_rubberband:BuildRequires:	rubberband-devel}
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-linguist >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
%if %{with tests} && %(grep -q ' /dev/shm ' /proc/mounts ; echo $?)
# tests fail without /dev/shm
BuildRequires:	mounted(/dev/shm)
%endif
Obsoletes:	hydrogen-doc < 1
# drumkits can be installed from the application
Obsoletes:	hydrogen-drumkits < 1.0-5
Obsoletes:	hydrogen-drumkits-3355606 < 1.0-5
Obsoletes:	hydrogen-drumkits-DrumkitPack1 < 1.0-5
Obsoletes:	hydrogen-drumkits-DrumkitPack2 < 1.0-5
Obsoletes:	hydrogen-drumkits-EasternHop-1 < 1.0-5
Obsoletes:	hydrogen-drumkits-Electric-Empire-Kit < 1.0-5
Obsoletes:	hydrogen-drumkits-ErnysPercussion < 1.0-5
Obsoletes:	hydrogen-drumkits-HardElectro1 < 1.0-5
Obsoletes:	hydrogen-drumkits-Millo-Drums_v.1 < 1.0-5
Obsoletes:	hydrogen-drumkits-Millo-MultiLayered2 < 1.0-5
Obsoletes:	hydrogen-drumkits-TD-7 < 1.0-5
Obsoletes:	hydrogen-drumkits-UltraAcousticKit < 1.0-5
Obsoletes:	hydrogen-drumkits-Yamaha-Vintage-Kit < 1.0-5
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
%setup -q

%build
mkdir build
cd build
%cmake .. \
	-DLADSPA_INCLUDE_DIR=/usr/include \
	-DLADSPA_LIBRARIES=%{_libdir}/ladspa \
	-DWANT_ALSA=ON \
	-DWANT_COREAUDIO=OFF \
	-DWANT_COREMIDI=OFF \
	-DWANT_DEBUG=%{debug} \
	-DWANT_JACK=ON \
	-DWANT_LADSPA=ON \
	-DWANT_LASH=ON \
	-DWANT_LIBARCHIVE=ON \
	-DWANT_LRDF=ON \
	-DWANT_OSS=ON \
	-DWANT_PORTAUDIO=ON \
	-DWANT_PORTMIDI=ON \
	%{?with_rubberband:-DWANT_RUBBERBAND=ON}

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

%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/hydrogen

# unify
%{__mv} $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/i18n/hydrogen_{hu_HU,hu}.qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/h2cli
%attr(755,root,root) %{_bindir}/h2player
%attr(755,root,root) %{_bindir}/hydrogen
%attr(755,root,root) %{_libdir}/libhydrogen-core-%{version}.so
%dir %{_datadir}/hydrogen
%dir %{_datadir}/hydrogen/data
%{_datadir}/hydrogen/data/*.conf
%{_datadir}/hydrogen/data/*.wav
%{_datadir}/hydrogen/data/drumkits
%{_datadir}/hydrogen/data/img
%{_datadir}/hydrogen/data/new_tutorial
%{_datadir}/hydrogen/data/themes
%{_datadir}/hydrogen/data/xsd
%{_datadir}/metainfo/org.hydrogenmusic.Hydrogen.metainfo.xml
%{_desktopdir}/org.hydrogenmusic.Hydrogen.desktop
%{_iconsdir}/hicolor/scalable/apps/org.hydrogenmusic.Hydrogen.svg
%{_mandir}/man1/hydrogen.1*

# demo songs
%{_datadir}/hydrogen/data/demo_songs

# translations
%dir %{_datadir}/hydrogen/data/i18n
%lang(ca) %{_datadir}/hydrogen/data/i18n/%{name}_ca.qm
%lang(cs) %{_datadir}/hydrogen/data/i18n/%{name}_cs.qm
%lang(de) %{_datadir}/hydrogen/data/i18n/%{name}_de.qm
%lang(el) %{_datadir}/hydrogen/data/i18n/%{name}_el.qm
%lang(en) %{_datadir}/hydrogen/data/i18n/%{name}_en.qm
%lang(en) %{_datadir}/hydrogen/data/i18n/%{name}_en_GB.qm
%lang(es) %{_datadir}/hydrogen/data/i18n/%{name}_es.qm
%lang(fr) %{_datadir}/hydrogen/data/i18n/%{name}_fr.qm
%lang(gl) %{_datadir}/hydrogen/data/i18n/%{name}_gl.qm
%lang(hr) %{_datadir}/hydrogen/data/i18n/%{name}_hr.qm
%lang(hu) %{_datadir}/hydrogen/data/i18n/%{name}_hu.qm
%lang(it) %{_datadir}/hydrogen/data/i18n/%{name}_it.qm
%lang(ja) %{_datadir}/hydrogen/data/i18n/%{name}_ja.qm
%lang(nl) %{_datadir}/hydrogen/data/i18n/%{name}_nl.qm
%lang(pl) %{_datadir}/hydrogen/data/i18n/%{name}_pl.qm
%lang(pt_BR) %{_datadir}/hydrogen/data/i18n/%{name}_pt_BR.qm
%lang(ru) %{_datadir}/hydrogen/data/i18n/%{name}_ru.qm
%lang(sr) %{_datadir}/hydrogen/data/i18n/%{name}_sr.qm
%lang(sv) %{_datadir}/hydrogen/data/i18n/%{name}_sv.qm
%lang(uk) %{_datadir}/hydrogen/data/i18n/%{name}_uk.qm
%lang(zh_CN) %{_datadir}/hydrogen/data/i18n/%{name}_zh_CN.qm
