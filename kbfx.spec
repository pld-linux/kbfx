#
# Conditional build:
%bcond_with	snap	# build cvs snapshot
#
%define		_snap	20070117
%define		_rel	rc4
%define		_mainver	0.4.9
%if %{with snap}
%define	_ver	.3
%else
%define	_ver	.3
%endif

Summary:	Kicker bar enhancement for KDE
Summary(de):	Eine Kicker Erweiterung für KDE
Summary(pl):	Rozszerzenie paska Kickera dla KDE
Name:		kbfx
Version:	%{_mainver}%{_ver}
Release:	0.%{?with_snap:%{_snap}}%{!?with_snap:%{_rel}}.1
Epoch:		1
License:	GPL
Group:		X11/Applications
%if %{with snap}
Source10:	http://dl.sourceforge.net/kbfx/%{name}-%{_mainver}.3-%{_snap}.tar.bz2
# Source10-md5:	d3a823e2ca0e99ed5596e84b9f9907a8
%else
Source0:	http://dl.sourceforge.net/kbfx/%{name}-%{version}%{_rel}.tar.bz2
# Source0-md5:	52bdd89a284c5d8188898c1d97eb7b48
%endif
Patch0:		%{name}-am110.patch
Patch1:		kde-ac260-lt.patch
URL:		http://www.kbfx.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_snap:BuildRequires: cmake >= 2.4.2}
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
Kbfx ist spontan entstanden und hat als kleines Projekt angefangen. Es
soll den Menuknopf in KDE ersetzen. Der Erfolg von Kbfx ist der guten
Zusammenarbeit der KDE Fans und der Graphikkünstler zu verdanken.

%description -l pl
Kbfx by³ zapocz±tkowany jako ma³y projekt powsta³y ze spontanicznego
pomys³u. Ma byæ zamiennikiem przycisku menu w pasku kickera w KDE.
Sukcesem kbfx by³a wspó³praca ze strony mi³o¶ników KDE i artystów.

%prep
%setup -q -T -b %{?with_snap:1}0 -n %{name}-%{?with_snap:%{version}-%{_snap}}%{!?with_snap:%{version}%{_rel}}
%if !%{with snap}
%patch0 -p0
%patch1 -p1
%endif

%build
%if %{with snap}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%else
%{__make} -f Makefile.cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%endif
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}/kde}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \
%if !%{with snap}
install kbfxspinx/kbfxspinx.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kbfxconfigapp.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
%endif
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files -f %{name}spinx.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbfxconfigapp
%if %{with snap}
%{_libdir}/kbfx/plugins/libkbfxplasmadataplasmoid.la
%attr(755,root,root) %{_libdir}/kbfx/plugins/libkbfxplasmadataplasmoid.so
%{_libdir}/kbfx/plugins/libkbfxplasmadatasettings.la
%attr(755,root,root) %{_libdir}/kbfx/plugins/libkbfxplasmadatasettings.so
%{_libdir}/kbfx/plugins/libkbfxplasmadatastub.la
%attr(755,root,root) %{_libdir}/kbfx/plugins/libkbfxplasmadatastub.so
%{_libdir}/libkbfxplasma.la
%attr(755,root,root) %{_libdir}/libkbfxplasma.so
%{_libdir}/libkbfxspinxtest.la
%attr(755,root,root) %{_libdir}/libkbfxspinxtest.so
%{_datadir}/applnk/Utilities/kbfxconfigapp.desktop
%{_datadir}/apps/kicker/applets/kbfxspinxtest.desktop
%{_datadir}/apps/konqueror/servicemenus/kbfx_prepare_theme.desktop
%else
%attr(755,root,root) %{_libdir}/libkbfxspinx.so
%{_libdir}/libkbfxspinx.la
%{_datadir}/apps/kicker/applets/kbfxspinx.desktop
%{_desktopdir}/kde/kbfxconfigapp.desktop
%{_datadir}/config.kcfg/kbfx.kcfg
%{_datadir}/apps/konqueror/servicemenus/kbfx_prepare_theme.desktop
%endif
%{_datadir}/apps/kbfx
%{_datadir}/apps/kbfxconfigapp
%{_datadir}/apps/konqueror/servicemenus/kbfx_install_theme.desktop
%{_datadir}/applnk/.hidden/kbfx_theme.desktop
%{_datadir}/mimelnk/application/x-kbfxtheme.desktop
%{_iconsdir}/*/*/*/*.png
