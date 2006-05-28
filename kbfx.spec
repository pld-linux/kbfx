%bcond_with	snap	# build cvs snapshot

%define		_snap	20060528cvs
%define		_rel	rc1

Summary:	Kicker bar enhancement for KDE
Summary(de):	Eine Kicker Erweiterung für KDE
Summary(pl):	Rozszerzenie paska Kickera dla KDE
Name:		kbfx
Version:	0.4.9.2
Release:	0.%{?with_snap:%{_snap}}%{!?with_snap:%{_rel}}.1
Epoch:		1
License:	GPL
Group:		X11/Applications
%if %{with snap}
Source10:	http://dl.sourceforge.net/kbfx/%{name}-%{_snap}.tar.gz
# Source10-md5:	dc15f465a6d158ae3596795476800fad
%else
Source0:	http://dl.sourceforge.net/kbfx/%{name}-%{version}%{_rel}.tar.gz
# Source0-md5:	17349a247b5cc4f75eaa6829b92c577c
%endif
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
der guten zusammenarbeit der KDEfans und der Graphikkünstler zu
verdanken.

%description -l pl
Kbfx by³ zapocz±tkowany jako ma³y projekt powsta³y ze spontanicznego
pomys³u. Ma byæ zamiennikiem przycisku menu w pasku kickera w KDE.
Sukcesem kbfx by³a wspó³praca ze strony mi³o¶ników KDE i artystów.

%prep
%setup -q -T -b %{?with_snap:1}0 -n %{name}-%{?with_snap:%{_snap}}%{!?with_snap:%{version}%{_rel}}

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
%attr(755,root,root) %{_bindir}/kbfxconfigapp
%attr(755,root,root) %{_libdir}/libkbfxspinx.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmkbfx.so
%{_libdir}/libkbfxspinx.la
%{_libdir}/kde3/kcm_kcmkbfx.la
%{_datadir}/apps/kicker/applets/kbfxspinx.desktop
%{_desktopdir}/kde/kbfxconfig.desktop
%{_desktopdir}/kde/kcmkbfx.desktop
%{_datadir}/config.kcfg/kbfx.kcfg
%{_iconsdir}/crystalsvg/32x32/apps/*.png
%{_iconsdir}/crystalsvg/32x32/actions/*.png
%{_iconsdir}/crystalsvg/48x48/actions/*.png
%{_datadir}/apps/kbfx
%{_desktopdir}/kbfxspinx.desktop
