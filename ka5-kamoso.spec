#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.1
%define		kframever	5.56
%define		qtver		5.9.0
%define		kaname		kamoso
Summary:	Kamoso
Name:		ka5-%{kaname}
Version:	22.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c77b08dbfde9c3b178284f2d69fabc9f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-devel >= 1.1.90
BuildRequires:	gstreamer-gl-devel >= 1.1.90
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-purpose-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kamoso is an application to take pictures and videos out of your
webcam.

%description -l pl.UTF-8
Kamoso jest aplikacją do robienia zdjęć i ściągania video z
Twojej kamery internetowej.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/zh_CN

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kamoso
%attr(755,root,root) %{_libdir}/gstreamer-1.0/gstkamosoqt5videosink.so
%{_iconsdir}/hicolor/16x16/apps/kamoso.png
%{_iconsdir}/hicolor/22x22/apps/kamoso.png
%{_iconsdir}/hicolor/32x32/apps/kamoso.png
%{_iconsdir}/hicolor/48x48/apps/kamoso.png
%{_iconsdir}/hicolor/64x64/apps/kamoso.png
%{_iconsdir}/hicolor/128x128/apps/kamoso.png
%{_iconsdir}/hicolor/scalable/actions/burst.svgz
%{_iconsdir}/hicolor/scalable/apps/kamoso.svgz
%{_datadir}/metainfo/org.kde.kamoso.appdata.xml
%{_desktopdir}/org.kde.kamoso.desktop
%{_datadir}/knotifications5/kamoso.notifyrc
%{_datadir}/sounds/kamoso-shutter.wav
