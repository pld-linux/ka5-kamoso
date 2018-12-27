%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kamoso
Summary:	Kamoso
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f4446749b86a5911e3796070208f1aa9
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
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.48.0
BuildRequires:	kf5-kdoctools-devel >= 5.48.0
BuildRequires:	kf5-ki18n-devel >= 5.48.0
BuildRequires:	kf5-kio-devel >= 5.48.0
BuildRequires:	kf5-purpose-devel >= 5.53.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kamoso is an application to take pictures and videos out of your
webcam.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_iconsdir}/hicolor/scalable/actions/burst.svgz
%{_iconsdir}/hicolor/scalable/actions/record.svgz
%{_iconsdir}/hicolor/scalable/actions/shoot.svgz
%{_iconsdir}/hicolor/scalable/apps/kamoso.svgz
%{_datadir}/metainfo/org.kde.kamoso.appdata.xml
