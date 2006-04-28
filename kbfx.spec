
Summary:	Kicker bar enhancement for KDE
Summary(de):	Eine Kicker Erweiterung f�r KDE
Summary(pl):	Rozszerzenie paska Kickera dla KDE
Name:		kbfx
Version:	0.4.9.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://www.linuxlots.com/~siraj/kde/plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	c0141ec96588ca0aa9b12bb8bda88ebc
Patch0:		%{name}_automake_patch.diff
URL:		http://www.linuxlots.com/~siraj/kde/plugin/home/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kbfx started as a small hobby project born out of a spontaneous idea.
Kbfx is meant to be a kicker bar menu button replacement on KDE (K
Desktop Env). The success of kbfx has been the contributions of many
KDE lovers and Artists. From the current feedback from the community
the button is to go a long way from what is now! So Every one Lets
Build Button that Rocks KDE!

%description -l de
Kbfx ist spontan entstanden und hat als kleines Projekt angefangen.
Es soll den Menuknopf in KDE ersetzen. Der Erfolg von Kbfx ist
der guten zusammenarbeit der KDEfans und der Graphikk�nstler zu
verdanken.

%description -l pl
Kbfx by� zapocz�tkowany jako ma�y projekt powsta�y ze spontanicznego
pomys�u. Ma by� zamiennikiem przycisku menu w pasku kickera w KDE.
Sukcesem kbfx by�a wsp�praca ze strony mi�o�nik�w KDE i artyst�w.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build

%{__make} -f Makefile.cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

install kbfxspinx/kbfxspinx.desktop $RPM_BUILD_ROOT%{_desktopdir}

#%find_lang %{name}spinx --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files -f %{name}spinx.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbfxspinx.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmkbfx.so
%attr(755,root,root) %{_bindir}/kbfxconfigapp
%{_libdir}/libkbfxspinx.la
%{_libdir}/kde3/kcm_kcmkbfx.la
%{_datadir}/apps/kicker/applets/kbfxspinx.desktop
%{_datadir}/applications/kde/kbfxconfig.desktop
%{_datadir}/applications/kde/kcmkbfx.desktop
%{_datadir}/config.kcfg/kbfx.kcfg
%{_datadir}/icons/crystalsvg/32x32/apps/*.png
%{_datadir}/icons/crystalsvg/32x32/actions/*.png
%{_datadir}/icons/crystalsvg/48x48/actions/*.png
%{_datadir}/apps/kbfx/*
%{_datadir}/apps/kbfx/images/*.png
%{_datadir}/apps/kbfx/skins/default/*.png
%{_desktopdir}/kbfxspinx.desktop
