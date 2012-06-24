Summary:	Kicker bar enhancement for KDE
Summary(pl):	Rozszerzenie paska Kickera dla KDE
Name:		kbfx
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.linuxlots.com/~siraj/kde/plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	2709e4bf4d7a332603f210a1650b6fa1
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

%description -l pl
Kbfx by� zapocz�tkowany jako ma�y projekt powsta�y ze spontanicznego
pomys�u. Ma by� zamiennikiem przycisku menu w pasku kickera w KDE.
Sukcesem kbfx by�a wsp�praca ze strony mi�o�nik�w KDE i artyst�w.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin

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

install src/kbfx.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbfx.so
%{_libdir}/libkbfx.la
%{_datadir}/apps/kicker/applets/kbfx.desktop
%{_desktopdir}/kbfx.desktop
