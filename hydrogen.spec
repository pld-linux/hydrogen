Summary:	Pattern based drum machine
Summary(pl):	Automat perkusyjny
Name:		hydrogen
Version:	0.9.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/hydrogen/%{name}-%{version}.tar.gz
# Source0-md5:	d5840b5d330d433d00ea1727efb0fc7f
Source1:	%{name}.desktop
Patch0:		%{name}-gcc34.patch
Patch1:		%{name}-flac113.patch
Patch2:		%{name}-lib64.patch
URL:		http://www.hydrogen-music.org/
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	liblrdf-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.2.1
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hydrogen is a "free" pattern based drum machine for GNU/Linux. The
application goal is to allow the simple and fast creation of rhythmic
patterns.

%description -l pl
Hydrogen jest "wolnym" automatem perkusyjnym opartym o paterny dla
GNU/Linuksa. Celem programu jest umo¿liwienie w prosty i szybki sposób
tworzenia paternów rytmicznych.

%package doc
Summary:	Hydrogen manual and tutorial
Summary(pl):	Podrêcznik i tutorial Hydrogena
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Hydrogen manual and tutorial.

%description doc -l pl
Podrêcznik i tutorial Hydrogena.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%if "%{_lib}" == "lib64"
%patch2 -p1
%endif

%build
export QTDIR=%{_prefix}
cp -f /usr/share/automake/config.sub admin

# don't run update-menus (WTF is that?)
sed -i -e 's|update-menus||' Makefile.in

# clean up CVS trash
find . -type d -name CVS -print | xargs rm -rf {} \;

%configure
%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/{man1,ru/man1},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# clean up documentation
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/*.{docbook,sh}
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/img/*.h2song
rm -f $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/i18n/*.{sh,ts}
rm -rf $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/man

install data/doc/man/C/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install data/doc/man/ru/*.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1
install data/doc/img/Tutorial2.h2song \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs
install data/img/gray/icon48.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hydrogen.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so

%dir %{_datadir}/hydrogen
%dir %{_datadir}/hydrogen/data
%dir %{_datadir}/hydrogen/data/demo_songs

%{_datadir}/hydrogen/data/*.conf
%{_datadir}/hydrogen/data/*.h2song
%{_datadir}/hydrogen/data/*.wav
%{_datadir}/hydrogen/data/drumkits
%{_datadir}/hydrogen/data/img
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

# demo songs
%{_datadir}/hydrogen/data/demo_songs/GM_*.h2song
%{_datadir}/hydrogen/data/demo_songs/TR808kit-demo.h2song
%{_datadir}/hydrogen/data/demo_songs/tutorial_georgyporgy.h2song

# translations
%lang(de) %{_datadir}/hydrogen/data/i18n/%{name}.de.qm
%lang(es) %{_datadir}/hydrogen/data/i18n/%{name}.es.qm
%lang(fr) %{_datadir}/hydrogen/data/i18n/%{name}.fr.qm
%lang(hu) %{_datadir}/hydrogen/data/i18n/%{name}.hu_HU.qm
%lang(it) %{_datadir}/hydrogen/data/i18n/%{name}.it.qm
%lang(ja) %{_datadir}/hydrogen/data/i18n/%{name}.ja.qm
%lang(nl) %{_datadir}/hydrogen/data/i18n/%{name}.nl.qm
%lang(pl) %{_datadir}/hydrogen/data/i18n/%{name}.pl.qm
%lang(pt) %{_datadir}/hydrogen/data/i18n/%{name}.pt_BR.qm
%lang(ru) %{_datadir}/hydrogen/data/i18n/%{name}.ru.qm
%{_mandir}/man1/*.1*
%lang(ru) %{_mandir}/ru/man1/*.1*

%files doc
%defattr(644,root,root,755)
%dir %{_datadir}/hydrogen/data/doc
%dir %{_datadir}/hydrogen/data/doc/img

# demo songs
%{_datadir}/hydrogen/data/demo_songs/Tutorial2.h2song

# images
%lang(nl) %{_datadir}/hydrogen/data/doc/img/nl/*.png
%{_datadir}/hydrogen/data/doc/img/*.png
%{_datadir}/hydrogen/data/doc/img_tutorial
%{_datadir}/hydrogen/data/doc/infoSplash

# multilang manual & tutorial
%lang(de) %{_datadir}/hydrogen/data/doc/manual_de.html
%lang(es) %{_datadir}/hydrogen/data/doc/manual_es.html
%lang(fr) %{_datadir}/hydrogen/data/doc/manual_fr.html
%lang(fr) %{_datadir}/hydrogen/data/doc/tutorial_fr.html
%lang(it) %{_datadir}/hydrogen/data/doc/manual_it.html
%lang(it) %{_datadir}/hydrogen/data/doc/tutorial_it.html
%lang(nl) %{_datadir}/hydrogen/data/doc/manual_nl.html
%{_datadir}/hydrogen/data/doc/manual.html
%{_datadir}/hydrogen/data/doc/manual_en.html
%{_datadir}/hydrogen/data/doc/tutorial_en.html
